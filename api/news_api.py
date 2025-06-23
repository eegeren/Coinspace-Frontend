from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_news():
    return [
        {
            "title": "Bitcoin surges past $65K",
            "description": "Bitcoin reached a new high this week.",
            "link": "https://example.com"
        },
        {
            "title": "Ethereum update boosts performance",
            "description": "ETH 2.0 rollout gains traction.",
            "link": "https://example.com"
        }
    ]
