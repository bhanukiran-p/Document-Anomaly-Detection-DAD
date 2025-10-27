from fastapi import APIRouter, UploadFile, File
from datetime import datetime
from model.model import TransactionData, TransactionResponse, CheckResponse
from controller.transaction_controller import TransactionController
from controller.check_controller import CheckController

router = APIRouter()

@router.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Fraud Detection API",
        "version": "1.0.0",
        "endpoints": {
            "transaction_analysis": "/api/analyze-transaction",
            "check_detection": "/api/analyze-check",
            "health": "/health"
        }
    }

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@router.post("/api/analyze-transaction", response_model=TransactionResponse)
async def analyze_transaction(transaction: TransactionData):
    """Analyze a transaction for fraud"""
    transaction_dict = transaction.dict()
    result = TransactionController.analyze_transaction(transaction_dict)
    return TransactionResponse(**result)

@router.post("/api/analyze-check", response_model=CheckResponse)
async def analyze_check(file: UploadFile = File(...)):
    """Analyze a check image for fraud"""
    result = await CheckController.analyze_check(file)
    return CheckResponse(**result)
