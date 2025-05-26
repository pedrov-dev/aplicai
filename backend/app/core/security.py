"""
This file contains security utilities for authentication, password hashing, and token handling.
You can expand this file as you integrate with Supabase Auth, Firebase Auth, or your own JWT logic.
"""

from passlib.context import CryptContext

# Password hashing context (if you need to hash passwords locally)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

