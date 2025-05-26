from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Pydantic models
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None

@router.get("/", response_model=List[UserResponse])
async def list_users():
    """
    List all users (admin only).
    """
    # TODO: Implement user listing logic (admin only)
    raise HTTPException(status_code=501, detail="List users not implemented")

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """
    Get a user by ID.
    """
    # TODO: Implement user retrieval logic
    raise HTTPException(status_code=501, detail="Get user not implemented")

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, data: UserUpdate):
    """
    Update user profile.
    """
    # TODO: Implement user update logic
    raise HTTPException(status_code=501, detail="Update user not implemented")

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """
    Delete a user (admin only).
    """
    # TODO: Implement user deletion logic (admin only)
    raise HTTPException(status_code=501, detail="Delete user not implemented")