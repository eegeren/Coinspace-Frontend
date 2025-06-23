from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Statik klasörü mount et
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ana sayfa için index.html'i döndür
@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Diğer API router'larını burada import et
from api.coin_api import router as coin_router
#from api.signal_api import router as signal_router
#from api.calendar_api import router as calendar_router

#app.include_router(coin_router, prefix="/api/coin")
#app.include_router(signal_router, prefix="/api/signal")
#app.include_router(calendar_router, prefix="/api/calendar")
