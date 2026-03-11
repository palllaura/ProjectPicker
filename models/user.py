import enum

from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class User(Base):
    """User model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    experience_level = Column(String, nullable=False)
    primary_stack = Column(String, nullable=False)
    preferred_duration = Column(String, nullable=False)
    skills = Column(String, nullable=True)
    availability_confirmed = Column(Boolean, nullable=False)


class Experience(enum.Enum):
    """Level of experience."""

    JUNIOR = 'Junior (0-2 years)'
    MID = 'Mid-level (2-5 years)'
    SENIOR = 'Senior (5+ years)'


class Stack(enum.Enum):
    """Primary technology stack."""

    BACKEND = 'Backend Development'
    FRONTEND = 'Frontend Development'
    FULLSTACK = 'Full-Stack Development'
    DATA = 'Data Engineering'
    DEVOPS = 'DevOps'
    MOBILE = 'Mobile Development'


class Duration(enum.Enum):
    """Preferred project duration."""

    SHORT = 'Short-term (1-3 months)'
    MEDIUM = 'Medium-term (3-6 months)'
    LONG = 'Long-term (6+ months)'
