"""
Pydantic schemas for CoverLetter objects.
These are used for request validation and response serialization.
"""

from pydantic import BaseModel
from typing import Optional

class CoverLetterBase(BaseModel):
    job_id: int
    user_id: int
    content: Optional[str] = None

class CoverLetterCreate(CoverLetterBase):
    pass

class CoverLetterUpdate(BaseModel):
    content: str

class CoverLetterResponse(CoverLetterBase):
    id: int
    content: Optional[str] = None

    class Config:
        orm_mode = True