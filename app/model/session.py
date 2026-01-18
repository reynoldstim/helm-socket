from typing import Literal, Optional

from pydantic import BaseModel


class Target(BaseModel):
    type: Literal["agent"]
    id: str


class SessionCreateRequest(BaseModel):
    target: Target
    ttl_seconds: int
    metadata: Optional[dict] = None
