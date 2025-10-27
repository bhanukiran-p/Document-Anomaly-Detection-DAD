from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class TransactionData(BaseModel):
    account_number: str
    amount: float
    type: str
    merchant: Optional[str] = None
    location: Optional[str] = None
    recipient: Optional[str] = None
    time: Optional[str] = None
    device: Optional[str] = None

class TransactionResponse(BaseModel):
    fraud_score: float
    risk_level: str
    risk_category: str
    risk_factors: List[str]
    transaction_data: Dict[str, Any]

class CheckResponse(BaseModel):
    extracted_data: Dict[str, Any]
    fraud_score: float
    risk_level: str
    risk_category: str
    risk_factors: List[str]
    ml_score: float
    rule_score: float
    ml_ensemble: Optional[Dict[str, Any]]