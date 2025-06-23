from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.news_api import router as news_router
from api.signal_api import router as signal_router
from api.calendar_api import router as calendar_router

app = FastAPI()

# Statik dosyaları sunmak için
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# API'leri ekle
app.include_router(news_router, prefix="/api")
app.include_router(signal_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")

# Ana sayfa (örnek)
@app.get("/")
def read_root():
    return FileResponse("index.html")
