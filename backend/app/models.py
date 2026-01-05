from pydantic import BaseModel
from typing import Optional, Literal

class ChatRequest(BaseModel):
    message: Optional[str] = None
    career_goal: Optional[str] = None
    experience_level: Optional[Literal["student", "fresher", "early-career"]] = None

class ChatResponse(BaseModel):
    reply: str
