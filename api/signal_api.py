from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/signal")
async def get_ai_signal():
    return {
        "pair": "BTC/USDT",
        "signal": "BUY",
        "accuracy": "62%",
        "timestamp": datetime.utcnow().isoformat()
    }