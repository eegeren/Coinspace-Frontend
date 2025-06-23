
from fastapi import APIRouter

router = APIRouter()

@router.get("/calendar")
def get_calendar():
    return [
        {"event": "Fed Interest Rate Decision", "date": "2025-06-25", "impact": "High"},
        {"event": "ECB Press Conference", "date": "2025-06-26", "impact": "Medium"}
    ]
