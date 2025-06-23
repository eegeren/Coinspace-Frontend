from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.coin_api import router as coin_router

app = FastAPI()

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router ekle
app.include_router(coin_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Coinspace API is working!"}
