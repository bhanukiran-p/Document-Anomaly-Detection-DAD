import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
import pathlib
from geopy.geocoders import Nominatim
from splash_screen import show_splash
from top_usa_cities_f import load_usa_cities_coordinates
import time
import base64

if "show_splash" not in st.session_state:
    st.session_state.show_splash = False


if st.session_state.show_splash:
    show_splash()  
    st.stop()     


st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    /* Remove all top padding/margin */
    .main .block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    
    /* Extra safety for newer Streamlit versions */
    .css-18e3th9 {padding-top: 0rem !important;}
    .css-1outpf7 {margin-top: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

def add_fixed_logo():
    cwd = pathlib.Path(os.getcwd())
    here = pathlib.Path(__file__).parent if "__file__" in globals() else cwd
    
    # Search for logo in multiple locations
    candidates = [
        cwd / "FDN.png", 
        here / "FDN.png", 
        here / "assets" / "FDN.png", 
        cwd / "assets" / "FDN.png",
        cwd / "FD.png",
        here / "FD.png"
    ]
    
    logo_path = next((p for p in candidates if p.exists()), None)
    
    if not logo_path:
        st.warning("Logo file 'FDN.png' or 'FD.png' not found.")
        return
    
    encoded = base64.b64encode(logo_path.read_bytes()).decode()
    
    st.markdown(f"""
        <style>
        .fixed-logo {{
            position: fixed;
            top: 12px;
            left: 60px;
            z-index: 2147482000;
            background: rgba(255,255,255,0.95);
            border-radius: 6px;
            padding: 4px 6px;
        }}
        .fixed-logo img {{
            width: 150px;
            height: 50px;
            display: block;
            cursor: pointer;
        }}
        @media (max-width: 768px) {{
            .fixed-logo {{
                left: 56px;
                top: 10px;
            }}
        }}
        </style>
        <div class="fixed-logo">
            <a href="/" target="_self">
                <img src="data:image/png;base64,{encoded}" alt="FDN Logo" />
            </a>
        </div>
    """, unsafe_allow_html=True)

# Call this function immediately after imports
add_fixed_logo()

st.set_page_config(
    page_title="AI Anomaly Insights ",
    page_icon="📈",
    layout="wide"
)

if st.session_state.show_splash:
    show_splash()
    st.stop()

st.markdown("""
    <style>
    .main-content {
        padding-bottom: 80px; /* Space for fixed footer */
    }
    .fixed-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #2d5282;
        color: white;
        text-align: center;
        padding: 20px;
        z-index: 1000;
        box-shadow: 0 -4px 20px rgba(45, 82, 130, 0.4);
        font-size: 0.95em;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .detail-card {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

CSV_FILE = r"C:\Users\bhanukaranP\Desktop\DOC_AN_DET\Dataset_F_2.csv"

@st.cache_data
def get_city_coordinates(cities):
    """Get latitude and longitude for cities using GeoPy"""
    geolocator = Nominatim(user_agent="fraud_dashboard")
    coordinates = {}
    
    for city in cities:
        try:
            location = geolocator.geocode(f"{city}, USA")
            if location:
                coordinates[city] = {
                    'lat': location.latitude,
                    'lon': location.longitude
                }
            time.sleep(0.1)  
        except:
            continue
    
    return coordinates

def load_csv_data():
    """Load your CSV data"""
    try:
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
            df['DateTime'] = pd.to_datetime(df['DateTime'])
            df['Month-Year'] = df['DateTime'].dt.to_period('M').astype(str)
            return df
        else:
            st.warning(f"CSV file '{CSV_FILE}' not found.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading CSV: {str(e)}")
        return pd.DataFrame()
    
# Initialize session state for interactivity
if 'selected_detail' not in st.session_state:
    st.session_state.selected_detail = None
if 'show_customer_details' not in st.session_state:
    st.session_state.show_customer_details = False
if 'show_transaction_details' not in st.session_state:
    st.session_state.show_transaction_details = False


# Dashboard Header
st.markdown('<h1 style="margin-bottom:20px;"><i class="fas fa-chart-line"></i> AI Anomaly Insights</h1>', unsafe_allow_html=True)

df = load_csv_data()

if not df.empty:
    min_date = df['DateTime'].min().date()
    max_date = df['DateTime'].max().date()
    if 'date_reset_counter' not in st.session_state:
        st.session_state.date_reset_counter = 0

    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1.2, 1])

    with col5:
        st.markdown("<div style='font-size:18px; font-weight:bold; margin-bottom:8px'><i class='fas fa-calendar-alt'></i> Start Date</div>", unsafe_allow_html=True)
        start_date = st.date_input("Start", min_date, min_value=min_date, max_value=max_date, key=f"start_date_{st.session_state.date_reset_counter}", label_visibility="collapsed")

    with col6:
        col6a, col6b = st.columns([3, 1])
        with col6a:
            st.markdown("<div style='font-size:18px; font-weight:bold; margin-bottom:8px'><i class='fas fa-calendar-alt'></i> End Date</div>", unsafe_allow_html=True)
            end_date = st.date_input("End", max_date, min_value=min_date, max_value=max_date, key=f"end_date_{st.session_state.date_reset_counter}", label_visibility="collapsed")
        with col6b:
            st.markdown("<div style='font-size:18px; font-weight:bold; margin-bottom:8px; color:transparent;'>.</div>", unsafe_allow_html=True)
            if st.button("🔄", key="reset_dates", help="Reset to default date range", use_container_width=True):
                st.session_state.date_reset_counter += 1
                st.rerun()

    filtered_df = df[(df['DateTime'].dt.date >= start_date) & (df['DateTime'].dt.date <= end_date)]
    fraud_df = filtered_df[filtered_df['Legitimate'] == 0]

    with col1:
        total_users = filtered_df['CustomerID'].nunique()
        st.markdown(f"<div style='font-size:18px; font-weight:bold; margin:0'><i class='fas fa-users'></i> Customers</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:26px;  margin:0'>{total_users:,}</div>", unsafe_allow_html=True)

    with col2:
        total_transactions = len(filtered_df)
        st.markdown(f"<div style='font-size:18px; font-weight:bold; margin:0'><i class='fas fa-credit-card'></i> Transactions</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:26px;  margin:0'>{total_transactions:,}</div>", unsafe_allow_html=True)

    with col3:
        legit_count = filtered_df['Legitimate'].sum()
        st.markdown(f"<div style='font-size:18px; font-weight:bold; margin-bottom:4px'><i class='fas fa-check-circle' style='color:#00CC96'></i> Legit</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:26px;  margin:0'>{legit_count}</div>", unsafe_allow_html=True)

    with col4:
        fraud_count = len(fraud_df)
        st.markdown(f"<div style='font-size:18px; font-weight:bold; margin-bottom:4px'><i class='fas fa-exclamation-triangle' style='color:#FF4C4C'></i> Fraud</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:26px;  margin:0'>{fraud_count}</div>", unsafe_allow_html=True)

    with col7:
        if st.button("Customer Details", key="customers_btn"):
            st.session_state.show_customer_details = not st.session_state.show_customer_details

        st.markdown("""
            <style>
            div.stButton > button:first-child {
                font-weight:bold;
                font-size:16px;
                width:100%;
                padding:8px;
                border-radius:6px;
                background-color:#667eea;
                color:white;
                border:none;
                margin-top:20px;
            }
            div.stButton > button:first-child:hover {
                background-color:#5a67d8;
            }
            </style>
        """, unsafe_allow_html=True)

    if st.session_state.show_customer_details:
        with st.expander("**Customer Analysis Details**", expanded=True):
            st.markdown('<h4><i class="fas fa-users"></i> Customer Analysis Details</h4>', unsafe_allow_html=True)
            customer_stats = filtered_df.groupby('CustomerID').agg({
                'Amount': ['count', 'sum', 'mean'],
                'Legitimate': lambda x: (x == 0).sum(),  
                'TransactionLocationCity': 'nunique'
            }).round(2)
            customer_stats.columns = ['Transactions', 'Total_Amount', 'Avg_Amount', 'Fraud_Count', 'Cities']
            customer_stats['Fraud_Rate'] = (customer_stats['Fraud_Count'] / customer_stats['Transactions'] * 100).round(1)
            customer_stats = customer_stats.sort_values('Total_Amount', ascending=False).head(20)
            
            st.write("**Top 20 Customers by Transaction Volume:**")
            st.dataframe(customer_stats, use_container_width=True)
            
            # Quick stats
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Highest Spender", f"${customer_stats['Total_Amount'].max():,.2f}")
            with col2:
                st.metric("Most Active", f"{customer_stats['Transactions'].max()} transactions")
            with col3:
                avg_fraud_rate = customer_stats['Fraud_Rate'].mean()
                st.metric("Avg Fraud Rate", f"{avg_fraud_rate:.1f}%")

    if st.session_state.show_transaction_details:
        with st.expander("**Transaction Timeline Analysis**", expanded=True):
            st.markdown('<h4><i class="fas fa-credit-card"></i> Transaction Timeline Analysis</h4>', unsafe_allow_html=True)
            daily_stats = filtered_df.groupby(filtered_df['DateTime'].dt.date).agg({
                'Amount': ['count', 'sum'],
                'Legitimate': lambda x: (x == 0).sum()
            }).round(2)
            daily_stats.columns = ['Transaction_Count', 'Total_Amount', 'Fraud_Count']
            daily_stats['Fraud_Rate'] = (daily_stats['Fraud_Count'] / daily_stats['Transaction_Count'] * 100).round(1)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Daily Transaction Volume:**")
                st.line_chart(daily_stats['Transaction_Count'])
            with col2:
                st.write("**Daily Fraud Rate (%):**")
                st.line_chart(daily_stats['Fraud_Rate'])

    if filtered_df['DateTime'].dtype != 'datetime64[ns]':
        filtered_df['DateTime'] = pd.to_datetime(filtered_df['DateTime'])
    if 'fraud_df' in globals():
        if fraud_df['DateTime'].dtype != 'datetime64[ns]':
            fraud_df['DateTime'] = pd.to_datetime(fraud_df['DateTime'])

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        status_counts = filtered_df['Legitimate'].value_counts()
        labels = ['Fraud', 'Legitimate']
        values = [status_counts.get(0, 0), status_counts.get(1, 0)]

        fig1 = px.pie(
            names=labels,
            values=values,
            color=labels, 
            hole=0.4,
            color_discrete_map={'Fraud': '#FF4C4C', 'Legitimate': '#00CC96'}
        )

        fig1.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=14
        )
        fig1.update_layout(height=400, title_font_size=16,title=dict(
                        text="Fraud vs Legitimate Transactions",          
                        font=dict(size=20, color='black', family='Arial Black'), 
                        x=0.5,                                 
                        xanchor='center'),)

        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        if not fraud_df.empty:
            line_df = fraud_df.copy()
            line_df['Month'] = line_df['DateTime'].dt.to_period('M').astype(str)
            monthly_trend = line_df.groupby('Month')['Amount'].sum().reset_index()
            fig2 = px.line(
                monthly_trend,
                x='Month',
                y='Amount',
                markers=True,
                labels={'Amount':'Total Fraud Amount'},
                color_discrete_sequence=['#FF5733']
            )
            fig2.update_layout(height=400, xaxis_tickangle=-45,title=dict(
                        text="Monthly Fraud Amount Trend",          
                        font=dict(size=20, color='black', family='Arial Black'), 
                        x=0.5,                                 
                        xanchor='center'),)
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No fraud transactions for trend chart")

    with col3:
        numeric_cols = ['Amount','BalanceAfter','AvgDailyBalance','Legitimate']
        possible_cols = [col for col in filtered_df.columns if filtered_df[col].dtype in [np.int64,np.float64]]
        extra_cols = [c for c in possible_cols if c not in numeric_cols][:6]
        numeric_cols.extend(extra_cols)
        
        if len(numeric_cols) >= 2:
            corr_df = filtered_df[numeric_cols].corr()
            fig3 = px.imshow(
                corr_df,
                color_continuous_scale='RdBu',  
                aspect='auto'
            )
            fig3.update_layout(height=400, title_font_size=16,title=dict(
                        text="Fraud Data Correlation Heatmap",          
                        font=dict(size=20, color='black', family='Arial Black'), 
                        x=0.5,                                 
                        xanchor='center'),)
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("Not enough numeric columns for heatmap")

    col4, col5, col6 = st.columns(3)

    with col4:
        if not fraud_df.empty:
            usa_cities = load_usa_cities_coordinates()
            city_counts = fraud_df['TransactionLocationCity'].value_counts()
            map_data = []
            for city, count in city_counts.items():
                if city in usa_cities:
                    lat, lon = usa_cities[city]
                    map_data.append({'City':city,'Count':count,'lat':lat,'lon':lon})
            if map_data:
                df_map = pd.DataFrame(map_data)
                fig4 = px.scatter_mapbox(
                    df_map,
                    lat='lat',
                    lon='lon',
                    size='Count',
                    color='Count',
                    hover_name='City',
                    hover_data={'Count':True,'lat':False,'lon':False},
                    color_continuous_scale='Reds',
                    size_max=20,
                    zoom=2.2,
                    center={'lat':39.5,'lon':-98.35},
                    mapbox_style='open-street-map'
                )
                fig4.update_layout(height=400, margin={"r":0,"t":50,"l":0,"b":0},title=dict(
                        text="Fraud Transactions by Cities",          
                        font=dict(size=20, color='black', family='Arial Black'), 
                        x=0.5,                                 
                        xanchor='center'),)
                st.plotly_chart(fig4, use_container_width=True)
            else:
                st.info("No USA cities found in fraud data")
        else:
            st.info("No fraud transactions found for selected period")

    with col5:
        if not fraud_df.empty:
            fraud_reasons = fraud_df['FraudReason'].value_counts().head(10)
            if not fraud_reasons.empty:
                fraud_df_plot = pd.DataFrame({'FraudReason':fraud_reasons.index,'Count':fraud_reasons.values})
                fraud_df_plot['ShortReason'] = fraud_df_plot['FraudReason'].apply(lambda x: x if len(x)<=25 else x[:22]+'...')
                fig5 = px.bar(
                    fraud_df_plot,
                    x='Count',
                    y='ShortReason',
                    orientation='h',
                    color_discrete_sequence=["#E05A5A"],
                    hover_name='FraudReason',
                    hover_data={'ShortReason':False,'Count':True}
                )
                fig5.update_layout(
                    yaxis_title="Fraud Reason",
                    height=400,
                    title=dict(
                        text="Top Fraud Reasons",          
                        font=dict(size=20, color='black', family='Arial Black'), 
                        x=0.5,                                 
                        xanchor='center'),
                    
                    yaxis={'categoryorder':'total ascending'},
                    xaxis_type='log'
                )
                st.plotly_chart(fig5, use_container_width=True)
            else:
                st.info("No fraud reason data available")
        else:
            st.info("No fraud transactions found for selected period")

    with col6:
        if not fraud_df.empty:
            sankey_df = fraud_df.copy()
            sankey_df['LegitStr'] = sankey_df['Legitimate'].map({1:'Legitimate',0:'Fraud'})
            sankey_cols = ['Type','Merchant','LegitStr','Gender']
            labels = []
            for col in sankey_cols:
                labels.extend(list(sankey_df[col].unique()))
            labels = list(dict.fromkeys(labels))  
            label_to_idx = {label:i for i,label in enumerate(labels)}

            source = []
            target = []
            value = []

            for i in range(len(sankey_cols)-1):
                group = sankey_df.groupby([sankey_cols[i], sankey_cols[i+1]]).size().reset_index(name='count')
                for _, row in group.iterrows():
                    source.append(label_to_idx[row[sankey_cols[i]]])
                    target.append(label_to_idx[row[sankey_cols[i+1]]])
                    value.append(row['count'])

            fig6 = go.Figure(data=[go.Sankey(
                node=dict(label=labels, pad=15, thickness=10, color='skyblue',line=dict(color='black', width=0.5)),
                link=dict(source=source, target=target, value=value)
            )])
            fig6.update_layout(
                    title=dict(
                        text="Fraud Flow Sankey Diagram",          
                        font=dict(size=20, color='black', family='Arial Black'), 
                        x=0.5,                                    
                        xanchor='center'
                    ),
                    height=400,
                    width=1000,
                    font=dict(size=14, color='black', family='Arial'),
                    template=None
                )

            st.plotly_chart(fig6)
        else:
            st.info("No fraud transactions found for Sankey diagram")

else:
    st.warning("No data available. Please upload your CSV file in the main fraud detection app.")
    
    uploaded_file = st.file_uploader(
        "Upload your fraud detection CSV file",
        type=['csv']
    )
    
    if uploaded_file is not None:
        with open(CSV_FILE, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("CSV file uploaded successfully!")
        st.rerun()
st.markdown("""
    <div class='fixed-footer'>
        Where Innovation Meets Security &nbsp; | &nbsp;  Zero Tolerance for Fraud &nbsp; | &nbsp; © 2025 Xforia DAD 
    </div>
""", unsafe_allow_html=True)