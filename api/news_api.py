from fastapi import APIRouter

router = APIRouter()

@router.get("/news")
async def get_news():
    return [
        {"title": "Bitcoin hits new high"},
        {"title": "Ethereum merges successfully"},
        {"title": "Altcoin season incoming"}
    ]
