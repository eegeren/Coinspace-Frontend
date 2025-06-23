from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from api.news_api import router as news_router
from api.signal_api import router as signal_router
from api.calendar_api import router as calendar_router

app = FastAPI()

# CORS (Tarayıcıdan API çağrılarına izin verir)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Her yerden gelen isteklere izin ver
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Statik dosyalar
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# API rotaları
app.include_router(news_router, prefix="/api")
app.include_router(signal_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")

# Ana sayfa
@app.get("/")
def read_root():
    return FileResponse("index.html")
