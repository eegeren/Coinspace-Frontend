
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.news_api import router as news_router
from api.signal_api import router as signal_router
from api.calendar_api import router as calendar_router

app = FastAPI()

app.mount("/", StaticFiles(directory=".", html=True), name="static")

app.include_router(news_router, prefix="/api")
app.include_router(signal_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")

@app.get("/")
def read_root():
    return FileResponse("index.html")

from api.coin_api import router as coin_router
app.include_router(coin_router, prefix="/api")

