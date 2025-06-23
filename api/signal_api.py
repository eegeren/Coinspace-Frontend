from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_signal():
    return {
        "signal": "BUY",
        "accuracy": "63%"
    }
