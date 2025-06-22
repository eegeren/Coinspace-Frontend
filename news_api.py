from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

NEWS_API_KEY = os.getenv("NEWS_API_KEY") or "your_newsapi_key_here"

LIKES = {}

class LikeRequest(BaseModel):
    link: str

@app.get("/api/news")
def get_news():
    url = f"https://newsapi.org/v2/everything?q=crypto&language=en&sortBy=publishedAt&pageSize=100&apiKey={NEWS_API_KEY}"

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
            "likes": LIKES.get(article["url"], 0)
        })

    return result

@app.post("/api/news/like")
def like_news(data: LikeRequest):
    link = data.link
    if link not in LIKES:
        LIKES[link] = 1
    else:
        LIKES[link] += 1
    return {"link": link, "likes": LIKES[link]}
