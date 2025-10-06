import pandas as pd
import numpy as np
from datetime import datetime
import random
import time
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import warnings
warnings.filterwarnings('ignore')


def load_and_preprocess_data(csv_file_path):
    """Load CSV data and perform preprocessing"""
    df = pd.read_csv(csv_file_path)

    df['DateTime'] = pd.to_datetime(df['DateTime'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    df['Year'] = df['DateTime'].dt.year
    df['Month'] = df['DateTime'].dt.month
    df['Day'] = df['DateTime'].dt.day
    df['DayOfWeek'] = df['DateTime'].dt.dayofweek
    df['Hour'] = df['DateTime'].dt.hour
    
    df['SameHomeAndTransaction'] = (df['HomeCity'] == df['TransactionLocationCity']).astype(int)
    df['SameHomeAndLogin'] = (df['HomeCity'] == df['LoginLocationCity']).astype(int)
    df['SameTransactionAndLogin'] = (df['TransactionLocationCity'] == df['LoginLocationCity']).astype(int)
    df['SameCountryHomeTransaction'] = (df['HomeCountry'] == df['TransactionLocationCountry']).astype(int)
    
    df['AmountLog'] = np.log1p(df['Amount'])
    df['AmountZScore'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()
    
    customer_stats = df.groupby('CustomerID').agg({
        'Amount': ['mean', 'std', 'max', 'min', 'count'],
        'AvgDailyBalance': 'mean'
    }).round(2)
    
    customer_stats.columns = ['AvgAmount', 'StdAmount', 'MaxAmount', 'MinAmount', 'TxnCount', 'AvgBalance']
    df = df.merge(customer_stats, on='CustomerID', how='left')
    
    df['AmountToBalance'] = df['Amount'] / (df['BalanceAfter'] + 1) 
    df['AmountToAvgAmount'] = df['Amount'] / (df['AvgAmount'] + 1)
    df['AmountToMaxAmount'] = df['Amount'] / (df['MaxAmount'] + 1)
    
    return df


def prepare_features(df):
    """Prepare features for model training"""
    
    boolean_columns = ['IsByCheck']
    for col in boolean_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.upper()
            df[col] = df[col].map({'TRUE': 1, 'FALSE': 0, '1': 1, '0': 0}).fillna(0).astype(int)
    
    if 'Legitimate' in df.columns:
        df['Legitimate'] = df['Legitimate'].astype(str).str.upper()
        df['Legitimate'] = df['Legitimate'].map({'TRUE': 1, 'FALSE': 0, '1': 1, '0': 0}).fillna(1).astype(int)
    
    label_encoders = {}
    categorical_columns = ['Gender', 'Type', 'Currency', 'Category', 'HomeCountry', 
                          'TransactionLocationCountry', 'LoginLocationCountry']
    
    for col in categorical_columns:
        if col in df.columns:
            le = LabelEncoder()
            df[col + '_encoded'] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
    
    feature_columns = [
        'Amount', 'AmountLog', 'AmountZScore', 'AmountToBalance', 
        'AmountToAvgAmount', 'AmountToMaxAmount',
        
        'Year', 'Month', 'Day', 'DayOfWeek',
        'SameHomeAndTransaction', 'SameHomeAndLogin', 'SameTransactionAndLogin',
        'SameCountryHomeTransaction',
        
        'AvgAmount', 'StdAmount', 'MaxAmount', 'MinAmount', 'TxnCount',
        'AvgDailyBalance', 'BalanceAfter',
        
        'Gender_encoded', 'Type_encoded', 'Currency_encoded', 'Category_encoded',
        'HomeCountry_encoded', 'TransactionLocationCountry_encoded', 
        'LoginLocationCountry_encoded',
        'IsByCheck'
    ]

    available_features = [col for col in feature_columns if col in df.columns]
    
    X = df[available_features].copy()
    for col in X.columns:
        X[col] = pd.to_numeric(X[col], errors='coerce')
    
    X = X.fillna(0)  
    y = 1 - df['Legitimate'] 
    
    return X, y, available_features, label_encoders


def train_ensemble_models(X, y):
    """Train XGBoost and Random Forest models with ensemble voting"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    xgb_params = {
        'objective': 'binary:logistic',
        'eval_metric': 'auc',
        'max_depth': 4,
        'learning_rate': 0.1,
        'n_estimators': 20,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'random_state': 42,
        'scale_pos_weight': len(y_train[y_train == 0]) / len(y_train[y_train == 1])
    }
    xgb_model = xgb.XGBClassifier(**xgb_params)
    xgb_model.fit(X_train_scaled, y_train)

    rf_model = RandomForestClassifier(
        n_estimators=100, 
        max_depth=10, 
        random_state=42,
        class_weight='balanced'
    )
    rf_model.fit(X_train_scaled, y_train)
    y_proba_xgb = xgb_model.predict_proba(X_test_scaled)[:, 1]
    y_proba_rf = rf_model.predict_proba(X_test_scaled)[:, 1]
    
    y_proba_ensemble = (y_proba_xgb + y_proba_rf) / 2
    y_pred_ensemble = (y_proba_ensemble >= 0.5).astype(int)
    y_pred_xgb = (y_proba_xgb >= 0.5).astype(int)
    y_pred_rf = (y_proba_rf >= 0.5).astype(int)
    
    print("Model Performance:")
    print(f"XGBoost Accuracy: {accuracy_score(y_test, y_pred_xgb):.4f}")
    print(f"Random Forest Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
    print(f"Ensemble Accuracy: {accuracy_score(y_test, y_pred_ensemble):.4f}")
    
    print("\nEnsemble Classification Report:")
    print(classification_report(y_test, y_pred_ensemble, target_names=['Legitimate', 'Fraud']))
    print("\nEnsemble Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred_ensemble))
    
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'xgb_importance': xgb_model.feature_importances_,
        'rf_importance': rf_model.feature_importances_
    })
    feature_importance['combined_importance'] = (
        feature_importance['xgb_importance'] + feature_importance['rf_importance']
    ) / 2
    feature_importance = feature_importance.sort_values('combined_importance', ascending=False)
    
    print("\nTop 10 Most Important Features (Combined):")
    print(feature_importance[['feature', 'combined_importance']].head(10))
    
    return xgb_model, rf_model, scaler, feature_importance


def save_model_components(xgb_model, rf_model, scaler, feature_columns, label_encoders):
    """Save all model components for Streamlit app"""
    joblib.dump(xgb_model, 'xgb_fraud_model.pkl')
    joblib.dump(rf_model, 'rf_fraud_model.pkl')
    joblib.dump(scaler, 'feature_scaler.pkl')
    joblib.dump(label_encoders, 'label_encoders.pkl')
    joblib.dump(feature_columns, 'feature_columns.pkl')
    print("All model components saved successfully!")


def load_trained_model():
    """Load the pre-trained models"""
    try:
        xgb_model = joblib.load('xgb_fraud_model.pkl')
        rf_model = joblib.load('rf_fraud_model.pkl')
        scaler = joblib.load('feature_scaler.pkl')
        label_encoders = joblib.load('label_encoders.pkl')
        feature_columns = joblib.load('feature_columns.pkl')
        return xgb_model, rf_model, scaler, label_encoders, feature_columns
    except FileNotFoundError as e:
        print(f"Model files not found: {e}")
        return None, None, None, None, None

def preprocess_transaction_data(transaction_data):
    """Convert Streamlit form data to model-ready format"""
    df = pd.DataFrame([{
        'TransactionID': f'WEB_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
        'CustomerID': transaction_data.get('account_number', 'UNKNOWN'),
        'Amount': float(transaction_data.get('amount', 0)),
        'DateTime': datetime.now().strftime('%m/%d/%Y %I:%M:%S %p'),
        'Type': transaction_data.get('type', 'Transfer'),
        'Currency': 'USD',
        'Category': get_category_from_merchant(transaction_data.get('merchant', '')),
        'IsByCheck': False,
        'BalanceAfter': 5000,  
        'AvgDailyBalance': 5000,  
        'HomeCity': 'Unknown',
        'HomeCountry': 'USA',
        'TransactionLocationCity': extract_city_from_location(transaction_data.get('location', 'Unknown')),
        'TransactionLocationCountry': 'USA',
        'LoginLocationCity': 'Unknown',
        'LoginLocationCountry': 'USA',
        'Gender': 'Unknown',
        'Legitimate': 1  
    }])
    
    return df


def get_category_from_merchant(merchant):
    """Map merchant to category"""
    merchant_lower = merchant.lower()
    if any(word in merchant_lower for word in ['atm', 'cash']):
        return 'ATM'
    elif any(word in merchant_lower for word in ['restaurant', 'food', 'cafe', 'starbucks']):
        return 'Food'
    elif any(word in merchant_lower for word in ['store', 'shop', 'retail']):
        return 'Shopping'
    else:
        return 'Other'


def extract_city_from_location(location):
    """Extract city from location"""
    if ',' in location:
        return location.split(',')[0].strip()
    return location


def apply_feature_engineering(df):
    """Apply the same feature engineering as in training"""
    df['DateTime'] = pd.to_datetime(df['DateTime'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    df['Year'] = df['DateTime'].dt.year
    df['Month'] = df['DateTime'].dt.month
    df['Day'] = df['DateTime'].dt.day
    df['DayOfWeek'] = df['DateTime'].dt.dayofweek
    df['Hour'] = df['DateTime'].dt.hour
   
    df['SameHomeAndTransaction'] = (df['HomeCity'] == df['TransactionLocationCity']).astype(int)
    df['SameHomeAndLogin'] = (df['HomeCity'] == df['LoginLocationCity']).astype(int)
    df['SameTransactionAndLogin'] = (df['TransactionLocationCity'] == df['LoginLocationCity']).astype(int)
    df['SameCountryHomeTransaction'] = (df['HomeCountry'] == df['TransactionLocationCountry']).astype(int)
    
    df['AmountLog'] = np.log1p(df['Amount'])
    df['AmountZScore'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()
    
    df['AvgAmount'] = df['Amount']
    df['StdAmount'] = 0
    df['MaxAmount'] = df['Amount']
    df['MinAmount'] = df['Amount']
    df['TxnCount'] = 1
    df['AvgBalance'] = df['AvgDailyBalance']
    
    df['AmountToBalance'] = df['Amount'] / (df['BalanceAfter'] + 1)
    df['AmountToAvgAmount'] = df['Amount'] / (df['Amount'] + 1)
    df['AmountToMaxAmount'] = 1.0
    
    return df

def prepare_features_for_prediction(df, label_encoders):
    """Prepare features for prediction using saved encoders - SAFE VERSION"""
    df['IsByCheck'] = df['IsByCheck'].astype(int)

    categorical_columns = ['Gender', 'Type', 'Currency', 'Category', 'HomeCountry', 
                          'TransactionLocationCountry', 'LoginLocationCountry']
    
    for col in categorical_columns:
        if col in df.columns and col in label_encoders:
            le = label_encoders[col]
            
            df[col] = df[col].fillna('Unknown')  
            df[col] = df[col].astype(str)       
            
            try:
                df[col + '_encoded'] = le.transform(df[col])
            except ValueError:
                #print(f"Warning: Unknown category in {col}: {df[col].values}")
                df[col + '_encoded'] = 0 
        else:
            df[col + '_encoded'] = 0
    
    feature_columns = [
        'Amount', 'AmountLog', 'AmountZScore', 'AmountToBalance', 
        'AmountToAvgAmount', 'AmountToMaxAmount',
        'Year', 'Month', 'Day', 'DayOfWeek',
        'SameHomeAndTransaction', 'SameHomeAndLogin', 'SameTransactionAndLogin',
        'SameCountryHomeTransaction',
        'AvgAmount', 'StdAmount', 'MaxAmount', 'MinAmount', 'TxnCount',
        'AvgDailyBalance', 'BalanceAfter',
        'Gender_encoded', 'Type_encoded', 'Currency_encoded', 'Category_encoded',
        'HomeCountry_encoded', 'TransactionLocationCountry_encoded', 
        'LoginLocationCountry_encoded',
        'IsByCheck'
    ]
    
    available_features = [col for col in feature_columns if col in df.columns]
    X = df[available_features].copy()
    
    for col in X.columns:
        X[col] = pd.to_numeric(X[col], errors='coerce')
    
    X = X.fillna(0)
    return X, None, available_features, label_encoders

def ml_transaction_analysis(transaction_data):
    """Use trained ensemble models for fraud prediction"""
    xgb_model, rf_model, scaler, label_encoders, feature_columns = load_trained_model()
    
    if xgb_model is None or rf_model is None:
        return mock_transaction_analysis(transaction_data)
    try:
        df = preprocess_transaction_data(transaction_data)
        processed_df = apply_feature_engineering(df)
        
        X, _, _, _ = prepare_features_for_prediction(processed_df, label_encoders)
        missing_features = set(feature_columns) - set(X.columns)
        for feature in missing_features:
            X[feature] = 0
        
        X = X[feature_columns].fillna(0)
        X_scaled = scaler.transform(X)
       
        xgb_prob = float(xgb_model.predict_proba(X_scaled)[:, 1][0])
        rf_prob = float(rf_model.predict_proba(X_scaled)[:, 1])
        ensemble_prob=(xgb_prob*0.65 + rf_prob*0.35)
        
        return {
            'xgb_probability': float(xgb_prob),
            'rf_probability': float(rf_prob),
            'ensemble_probability': float(ensemble_prob),
            'risk_level': get_risk_level(ensemble_prob)
        }
        
    except Exception as e:
        print(f"Error in ensemble analysis: {str(e)}")
        return mock_transaction_analysis(transaction_data)

def get_risk_level(probability):
    """Convert probability to risk level"""
    if probability < 0.4:
        return "LOW"
    elif probability < 0.7:
        return "MEDIUM"
    else:
        return "HIGH"


def mock_transaction_analysis(transaction_data):
    """Fallback mock analysis"""
    
    time.sleep(1) 
    amount = float(transaction_data.get("amount", 0))
    if amount > 10000:
        fraud_score = random.uniform(0.6, 0.9)
    elif amount > 5000:
        fraud_score = random.uniform(0.3, 0.7)
    else:
        fraud_score = random.uniform(0.1, 0.4)
    return fraud_score


def train_and_save_model(csv_file_path='Dataset_F.csv'):
    """Complete training pipeline"""
    print("Loading and preprocessing data...")
    df = load_and_preprocess_data(csv_file_path)
    
    print(f"Dataset shape: {df.shape}")
    print(f"Fraud rate: {(1 - df['Legitimate'].mean()) * 100:.2f}%")
    
    print("\nPreparing features...")
    X, y, feature_columns, label_encoders = prepare_features(df)
    
    print(f"Features shape: {X.shape}")
    print(f"Selected features: {len(feature_columns)}")
    
    print("\nTraining XGBoost model...")
    xgb_model, rf_model, scaler, feature_importance = train_ensemble_models(X, y)

    print("\nSaving model components...")
    save_model_components(xgb_model, rf_model, scaler, feature_columns, label_encoders)
    return xgb_model, rf_model, scaler, feature_importance, label_encoders

if __name__ == "__main__":

    trained_xgb_model, trained_rf_model, trained_scaler, importance_df, encoders = train_and_save_model()
    print("\nEnsemble model training completed successfully!")
