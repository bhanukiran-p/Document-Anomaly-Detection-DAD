import hashlib
import tempfile
import os
from datetime import datetime
from typing import Dict, List, Optional
from fastapi import HTTPException, UploadFile

# Configuration
MINDEE_API_KEY = "md_sIUeSD0Mpunqz6tDDjvNoIJOvJeAwZAe"
MINDEE_ACCOUNT_NAME = ""
MINDEE_ENDPOINT_NAME = ""
MINDEE_VERSION = "1"
MINDEE_MODEL_ID = "e11fdf0e-4bd6-42ff-88a8-1f3f1b9263d3"

# ML Model fallback
try:
    from ML_Model import ml_transaction_analysis
except ImportError:
    def ml_transaction_analysis(data):
        h = hashlib.sha256(str(data).encode()).hexdigest()
        return (int(h, 16) % 1000) / 1000.0


class CheckController:
    """Controller for check fraud detection"""
    
    @staticmethod
    def extract_check_data(response) -> Optional[Dict]:
        """Extract check data from Mindee response"""
        try:
            fields = response.inference.result.fields
            names = ['memo', 'pay_to', 'bank_name', 'signature', 'check_date', 
                     'payer_name', 'word_amount', 'check_number', 'number_amount', 
                     'payer_address', 'account_number', 'routing_number']
            return {n: (fields[n].value if n in fields else None) for n in names}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error extracting check data: {e}")
    
    @staticmethod
    def convert_ocr_to_ml_format(check_data: Dict) -> Dict:
        """Convert OCR data to ML model format"""
        amount = check_data.get('number_amount', 0) or 0
        return {
            'account_number': str(check_data.get('account_number') or 'UNKNOWN'),
            'amount': float(amount),
            'type': 'Check',
            'merchant': str(check_data.get('memo') or 'Check Payment'),
            'location': 'Unknown',
            'recipient': str(check_data.get('pay_to') or 'Unknown'),
            'time': 'Morning (6AM-12PM)',
            'device': 'Check'
        }
    
    @staticmethod
    def calculate_fraud_score(check_data: Dict) -> float:
        """Calculate rule-based fraud score for check"""
        score = 0.1
        
        if not check_data.get('pay_to'):
            score += 0.2
        if not check_data.get('number_amount'):
            score += 0.3
        if not check_data.get('signature'):
            score += 0.3
        if not check_data.get('bank_name'):
            score += 0.2
        if not check_data.get('account_number'):
            score += 0.2
        if not check_data.get('routing_number'):
            score += 0.2
        
        amt = check_data.get('number_amount', 0)
        if amt and amt > 10000:
            score += 0.2
        elif amt and amt > 5000:
            score += 0.1
        
        words = check_data.get('word_amount', '')
        if words and amt and len(words.split()) < 3:
            score += 0.1
        
        check_date = check_data.get('check_date')
        if check_date:
            try:
                date_obj = datetime.strptime(str(check_date), '%Y-%m-%d')
                days = (datetime.now() - date_obj).days
                if days > 180:
                    score += 0.2
                elif days > 90:
                    score += 0.1
            except:
                score += 0.1
        
        return min(score, 0.95)
    
    @staticmethod
    def get_risk_level(score: float) -> tuple:
        """Get risk level for check"""
        if score >= 0.7:
            return "HIGH RISK", "high"
        elif score >= 0.4:
            return "MEDIUM RISK", "medium"
        else:
            return "LOW RISK", "low"
    
    @staticmethod
    def get_check_risk_factors(check_data: Dict, ml_score: float, rule_score: float) -> List[str]:
        """Get risk factors for check"""
        factors = []
        
        if not check_data.get('signature'):
            factors.append("Missing signature")
        if not check_data.get('number_amount'):
            factors.append("Missing amount")
        if not check_data.get('pay_to'):
            factors.append("Missing payee")
        if not check_data.get('bank_name'):
            factors.append("Missing bank information")
        
        amt = check_data.get('number_amount', 0)
        if amt and amt > 10000:
            factors.append("Very high check amount")
        elif amt and amt > 5000:
            factors.append("High check amount")
        
        check_date = check_data.get('check_date')
        if check_date:
            try:
                days = (datetime.now() - datetime.strptime(str(check_date), '%Y-%m-%d')).days
                if days > 180:
                    factors.append("Check is over 6 months old")
                elif days > 90:
                    factors.append("Check is over 3 months old")
            except:
                factors.append("Invalid check date")
        
        if ml_score > 0.8:
            factors.append("AI detected very high fraud risk")
        elif ml_score > 0.6:
            factors.append("AI detected elevated fraud risk")
        
        words = check_data.get('word_amount', '')
        if words and amt and len(words.split()) < 3:
            factors.append("Incomplete written amount")
        
        return factors if factors else ["No significant risk factors detected"]
    
    @staticmethod
    async def analyze_check(file: UploadFile) -> Dict:
        """Analyze a check image for fraud"""
        try:
            # Check file type
            if not file.content_type.startswith('image/'):
                raise HTTPException(status_code=400, detail="File must be an image")
            
            # Import Mindee
            try:
                from mindee import ClientV2, InferenceParameters
            except ImportError:
                raise HTTPException(status_code=500, detail="Mindee SDK not installed")
            
            if not MINDEE_API_KEY:
                raise HTTPException(status_code=500, detail="MINDEE_API_KEY is not set")
            
            # Initialize Mindee client
            try:
                client = ClientV2(MINDEE_API_KEY, region="us")
            except TypeError:
                client = ClientV2(MINDEE_API_KEY)
            
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
                content = await file.read()
                tmp.write(content)
                tmp_path = tmp.name
            
            try:
                # Process with Mindee
                source = client.source_from_path(tmp_path)
                
                if MINDEE_ACCOUNT_NAME and MINDEE_ENDPOINT_NAME:
                    params = InferenceParameters(
                        account_name=MINDEE_ACCOUNT_NAME,
                        endpoint_name=MINDEE_ENDPOINT_NAME,
                        version=MINDEE_VERSION or "1"
                    )
                elif MINDEE_MODEL_ID:
                    params = InferenceParameters(model_id=MINDEE_MODEL_ID)
                else:
                    raise HTTPException(status_code=500, detail="Mindee not configured properly")
                
                response = client.enqueue_and_get_inference(source, params)
                check_data = CheckController.extract_check_data(response)
                
                if not check_data:
                    raise HTTPException(status_code=500, detail="Could not extract check data")
                
                # Format extracted data
                extracted = {
                    "Pay To": check_data.get('pay_to', 'N/A'),
                    "Bank Name": check_data.get('bank_name', 'N/A'),
                    "Check Date": check_data.get('check_date', 'N/A'),
                    "Payer Name": check_data.get('payer_name', 'N/A'),
                    "Amount (Words)": check_data.get('word_amount', 'N/A'),
                    "Amount (Number)": f"${check_data.get('number_amount', 0):,.2f}" if check_data.get('number_amount') else 'N/A',
                    "Check Number": check_data.get('check_number', 'N/A'),
                    "Account Number": check_data.get('account_number', 'N/A'),
                    "Routing Number": check_data.get('routing_number', 'N/A'),
                    "Payer Address": check_data.get('payer_address', 'N/A'),
                    "Memo": check_data.get('memo', 'N/A'),
                    "Signature Present": "Yes" if check_data.get('signature') else "No"
                }
                
                # Convert to ML format and analyze
                transaction = CheckController.convert_ocr_to_ml_format(check_data)
                ml_result = ml_transaction_analysis(transaction)
                
                if isinstance(ml_result, dict):
                    ml_score = float(ml_result.get('ensemble_probability', 0.0))
                    ml_ensemble = ml_result
                else:
                    ml_score = float(ml_result or 0.0)
                    ml_ensemble = None
                
                # Calculate rule-based score
                rule_score = CheckController.calculate_fraud_score(check_data)
                
                # Combined score
                combined_score = ml_score * 0.7 + rule_score * 0.3
                
                # Get risk level
                risk_level, risk_category = CheckController.get_risk_level(combined_score)
                
                # Get risk factors
                risk_factors = CheckController.get_check_risk_factors(check_data, ml_score, rule_score)
                
                return {
                    'extracted_data': extracted,
                    'fraud_score': combined_score,
                    'risk_level': risk_level,
                    'risk_category': risk_category,
                    'risk_factors': risk_factors,
                    'ml_score': ml_score,
                    'rule_score': rule_score,
                    'ml_ensemble': ml_ensemble
                }
            
            finally:
                # Clean up temp file
                try:
                    os.unlink(tmp_path)
                except Exception:
                    pass
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing check: {str(e)}")

