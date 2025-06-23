
from fastapi import APIRouter
import requests 

router = APIRouter()

@router.get("/news")
def get_news():
    return [{"title": "Sample news", "summary": "This is a test news item."}]
