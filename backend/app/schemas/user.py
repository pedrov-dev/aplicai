"""
Pydantic schemas for User objects.
These are used for request validation and response serialization.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True