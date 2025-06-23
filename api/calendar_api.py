from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/calendar")
async def get_economic_calendar():
    return [
        {
            "event": "Fed Interest Rate Decision",
            "date": "2025-06-25T15:00:00Z",
            "impact": "High",
            "country": "US"
        },
        {
            "event": "ECB Press Conference",
            "date": "2025-06-26T13:45:00Z",
            "impact": "Medium",
            "country": "EU"
        },
        {
            "event": "BoJ Monetary Policy Statement",
            "date": "2025-06-27T04:00:00Z",
            "impact": "High",
            "country": "JP"
        }
    ]