from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme aşamasında tüm frontend isteklerine açık
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NEWS_API_KEY = os.getenv("NEWS_API_KEY") or "506d562e0d4a434c97df2e3a51e4cd1c"

@app.get("/api/news")
def get_news():
    url = f"https://newsapi.org/v2/everything?q=crypto&language=en&sortBy=publishedAt&pageSize=15&apiKey={NEWS_API_KEY}"
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
            "publishedAt": article["publishedAt"]
        })

    return result
