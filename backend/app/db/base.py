"""
This file defines the base class for SQLAlchemy models.
All ORM models should inherit from Base.
"""

from sqlalchemy.orm import declarative_base

Base = declarative_base()