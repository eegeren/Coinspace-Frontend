from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.signal_api import router as signal_router
from api.calendar_api import router as calendar_router
from api.coin_api import router as coin_router
from api.news_api import router as news_router

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signal_router, prefix="/api/signal")
app.include_router(calendar_router, prefix="/api/calendar")
app.include_router(coin_router, prefix="/api/coins")
app.include_router(news_router, prefix="/api/news")
