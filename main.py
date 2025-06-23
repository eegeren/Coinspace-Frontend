from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from api.signal_api import router as signal_router
from api.news_api import router as news_router
from api.calendar_api import router as calendar_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

app.include_router(signal_router, prefix="/api")
app.include_router(news_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")
