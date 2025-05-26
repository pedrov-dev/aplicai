"""
This file is for FastAPI dependencies such as authentication, database session, or user retrieval.
You can define reusable dependency functions here and import them in your endpoints.
"""

from fastapi import Depends, HTTPException, status, Request

# Example: Dependency to get the current user (stub)
async def get_current_user(request: Request):
    """
    Retrieve the current authenticated user from the request.
    Integrate with your auth provider (Supabase/Firebase) here.
    """
    # TODO: Implement actual user retrieval logic
    raise HTTPException(status_code=401, detail="Not authenticated")