from fastapi import APIRouter

router = APIRouter()

@router.get("/signal")
async def get_signal():
    return {"signal": "BUY", "accuracy": 72.5}
