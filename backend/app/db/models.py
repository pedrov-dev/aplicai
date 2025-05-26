"""
This file defines the SQLAlchemy ORM models for the application.
"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    # Add more fields as needed

    jobs = relationship("Job", back_populates="user")
    coverletters = relationship("CoverLetter", back_populates="user")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    user = relationship("User", back_populates="jobs")
    coverletters = relationship("CoverLetter", back_populates="job")

class CoverLetter(Base):
    __tablename__ = "coverletters"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)

    user = relationship("User", back_populates="coverletters")
    job = relationship("Job", back_populates="coverletters")