from fastapi import APIRouter
import requests

router = APIRouter()


NEWS_API_KEY = "506d562e0d4a434c97df2e3a51e4cd1c"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=10"

@router.get("/api/news")
def get_latest_news():
    return [
        {
            "title": "Bitcoin breaks $100,000 for first time",
            "description": "Bitcoin has hit a major milestone, crossing the $100,000 mark...",
            "link": "https://example.com/bitcoin-100k"
        },
        {
            "title": "Ethereum 2.0 Launches",
            "description": "The long-awaited Ethereum upgrade goes live today...",
            "link": "https://example.com/eth2-launch"
        }
    ]
