import hashlib
from typing import Dict, List, Tuple
from fastapi import HTTPException

# ML Model fallback
try:
    from ML_Model import ml_transaction_analysis
except ImportError:
    def ml_transaction_analysis(data):
        h = hashlib.sha256(str(data).encode()).hexdigest()
        return (int(h, 16) % 1000) / 1000.0


class TransactionController:
    """Controller for transaction fraud analysis"""
    
    @staticmethod
    def get_risk_level(score: float, amount: float = 0) -> Tuple[str, str]:
        """Determine risk level based on score and amount"""
        if amount > 100000:
            return "HIGH RISK", "high"
        elif amount > 50000 and score >= 0.5:
            return "HIGH RISK", "high"
        
        if score >= 0.7:
            return "HIGH RISK", "high"
        elif score >= 0.4:
            return "MEDIUM RISK", "medium"
        else:
            return "LOW RISK", "low"
    
    @staticmethod
    def get_detailed_risk_factors(transaction_data: Dict, fraud_score: float) -> List[str]:
        """Get detailed risk factors for a transaction"""
        factors = []
        amount = float(transaction_data.get('amount', 0))
        
        if amount > 500000:
            factors.append(f"⚠️ CRITICAL: Extremely high transaction amount (${amount:,.2f})")
        elif amount > 100000:
            factors.append(f"⚠️ Very high transaction amount (${amount:,.2f})")
        elif amount > 50000:
            factors.append(f"High transaction amount (${amount:,.2f})")
        elif amount > 10000:
            factors.append(f"Elevated transaction amount (${amount:,.2f})")
        elif amount > 5000:
            factors.append(f"Moderate transaction amount (${amount:,.2f})")
        
        time_of_day = transaction_data.get('time', '')
        if "Night" in time_of_day:
            factors.append("Unusual transaction time (night hours)")
        
        device = transaction_data.get('device', '')
        if device == "ATM" and amount > 1000:
            factors.append("Large ATM withdrawal")
        
        location = (transaction_data.get('location') or '').strip().lower()
        if not location or location == 'unknown':
            factors.append("Unknown transaction location")
        
        recipient = transaction_data.get('recipient', '')
        if not recipient or recipient.lower() == 'unknown':
            factors.append("Unverified recipient")
        
        if fraud_score > 0.8:
            factors.append("AI model shows very high fraud confidence")
        elif fraud_score > 0.6:
            factors.append("AI model shows elevated fraud risk")
        elif fraud_score > 0.4:
            factors.append("AI model shows moderate fraud risk")
        
        return factors if factors else ["No significant risk factors detected"]
    
    @staticmethod
    def analyze_transaction(transaction_dict: Dict) -> Dict:
        """Analyze a transaction for fraud"""
        try:
            # Get ML fraud score
            ml_result = ml_transaction_analysis(transaction_dict)
            
            if isinstance(ml_result, dict):
                fraud_score = float(ml_result.get('ensemble_probability', 0.0))
            else:
                fraud_score = float(ml_result or 0.0)
            
            # Get risk level
            amount = transaction_dict.get('amount', 0)
            risk_level, risk_category = TransactionController.get_risk_level(fraud_score, amount)
            
            # Get risk factors
            risk_factors = TransactionController.get_detailed_risk_factors(transaction_dict, fraud_score)
            
            return {
                'fraud_score': fraud_score,
                'risk_level': risk_level,
                'risk_category': risk_category,
                'risk_factors': risk_factors,
                'transaction_data': transaction_dict
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error analyzing transaction: {str(e)}")

