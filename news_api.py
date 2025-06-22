from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NEWS_API_KEY = os.getenv("NEWS_API_KEY") or "506d562e0d4a434c97df2e3a51e4cd1c"

@app.get("/api/news")
def get_news(page: int = Query(1, ge=1), page_size: int = Query(10, le=100)):
    url = (
        f"https://newsapi.org/v2/everything?q=crypto&language=en"
        f"&sortBy=publishedAt&pageSize={page_size}&page={page}&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "News API fetch failed"}

    articles = response.json().get("articles", [])
    result = []
    for article in articles:
        result.append({
            "title": article["title"],
            "description": article["description"] or "",
            "imgURL": article["urlToImage"] or "https://via.placeholder.com/300x200?text=No+Image",
            "link": article["url"],
            "publishedAt": article["publishedAt"],
            "likes": 0
        })
    return result
