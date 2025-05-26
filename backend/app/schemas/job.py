"""
Pydantic schemas for Job objects.
These are used for request validation and response serialization.
"""

from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    user_id: int
    title: str
    company: str
    description: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    description: Optional[str] = None

class JobResponse(JobBase):
    id: int

    class Config:
        orm_mode = True