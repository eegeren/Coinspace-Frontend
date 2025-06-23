from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.news_api import router as news_router
from api.signal_api import router as signal_router
from api.calendar_api import router as calendar_router

app = FastAPI()

# Statik dosyalar (HTML vs)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# API router'ları
app.include_router(news_router, prefix="/api")
app.include_router(signal_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")

# Ana sayfa (index.html)
@app.get("/")
def read_root():
    return FileResponse("index.html")
