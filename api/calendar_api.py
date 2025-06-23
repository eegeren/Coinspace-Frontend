from fastapi import APIRouter

router = APIRouter()

@router.get("/calendar")
def get_calendar():
    return [
        {"event": "Fed Interest Rate Decision", "date": "2025-06-25T15:00:00Z", "impact": "High"},
        {"event": "ECB Press Conference", "date": "2025-06-26T13:45:00Z", "impact": "Medium"},
        {"event": "BoJ Policy Statement", "date": "2025-06-27T04:00:00Z", "impact": "High"}
    ]
