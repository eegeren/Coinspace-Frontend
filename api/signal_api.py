from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/signal")
def get_signal():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "signal": "BUY",  # Gerçek sinyal burada üretilebilir
        "accuracy": "62%"
    }
