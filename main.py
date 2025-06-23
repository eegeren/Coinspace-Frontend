from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.news_api import router as news_router
from api.signal_api import router as signal_router
from api.calendar_api import router as calendar_router

app = FastAPI()

# API router'ları
app.include_router(news_router, prefix="/api")
app.include_router(signal_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")

# Statik dosyaları serve et (HTML dosyaları dahil)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Ana sayfa
@app.get("/")
def read_root():
    return FileResponse("index.html")
