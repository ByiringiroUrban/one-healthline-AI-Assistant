from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.chat_service import handle_chat

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    return handle_chat(request.message)