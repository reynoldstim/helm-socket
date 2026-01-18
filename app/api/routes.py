from this import s

from fastapi import APIRouter

import app.service.session as session_service
from app.model.session import SessionCreateRequest

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/sessions")
async def create_session(session: SessionCreateRequest) -> SessionCreateRequest:
    """Create a new session"""
    return session_service.create(session)
