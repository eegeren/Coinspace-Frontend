from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Router importları (bunlar dosyalarında `router = APIRouter()` olarak tanımlanmış olmalı)
from api.signal_api import router as signal_router
from api.coin_api import router as coin_router
from api.calendar_api import router as calendar_router
from api.news_api import router as news_router

app = FastAPI()

# CORS ayarı
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routerlarını bağlama
app.include_router(signal_router, prefix="/api")
app.include_router(coin_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")
app.include_router(news_router, prefix="/api")

# Ana sayfa kontrolü
@app.get("/api")
def read_root():
    return {"message": "Coinspace API is working!"}

# Statik dosyaları servis et (HTML, JS, CSS)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
