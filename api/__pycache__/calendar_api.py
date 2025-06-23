from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_calendar():
    return [
        {
            "event": "Fed Interest Rate Decision",
            "date": "2025-06-25",
            "time": "15:00 UTC",
            "impact": "High"
        },
        {
            "event": "ECB Press Conference",
            "date": "2025-06-26",
            "time": "13:45 UTC",
            "impact": "Medium"
        }
    ]
