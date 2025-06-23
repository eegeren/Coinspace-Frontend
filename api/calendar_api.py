from fastapi import APIRouter

router = APIRouter()

@router.get("/calendar")
async def get_calendar():
    return {"event": "Fed Meeting", "date": "2025-06-24"}
