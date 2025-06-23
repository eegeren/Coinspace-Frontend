from fastapi import APIRouter

router = APIRouter()

@router.get("/signal")
def get_signal():
    return {
        "signal": "BUY",
        "accuracy": "62%",
        "timestamp": "2025-06-23T08:00:00Z"
    }
