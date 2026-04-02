from fastapi import FastAPI
from app.api.routes import chat

app = FastAPI(title="One Healthline Assistant")

app.include_router(chat.router, prefix="/api")