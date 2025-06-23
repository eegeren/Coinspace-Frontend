
from fastapi import APIRouter

router = APIRouter()

@router.get("/signal")
def get_signal():
    return {"pair": "BTC/USDT", "signal": "BUY", "accuracy": "62%"}
