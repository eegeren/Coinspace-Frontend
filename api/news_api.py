from fastapi import APIRouter
import requests

router = APIRouter()


NEWS_API_KEY = "506d562e0d4a434c97df2e3a51e4cd1c"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=10"

@router.get("/api/news")
def get_latest_news():
    try:
        response = requests.get(f"{NEWS_ENDPOINT}&apiKey={NEWS_API_KEY}")
        data = response.json()

        articles = data.get("articles", [])
        simplified_news = [
            {
                "title": article["title"],
                "description": article.get("description", ""),
                "link": article["url"]
            }
            for article in articles if article.get("title") and article.get("url")
        ]
        return simplified_news

    except Exception as e:
        return {"error": str(e)}
