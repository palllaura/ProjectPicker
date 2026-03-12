from pydantic import BaseModel, EmailStr, Field
from typing import List

from models.user import Experience, Stack, Duration


class UserSubmission(BaseModel):
    """Schema for user profile submission."""

    name: str
    email: EmailStr
    experience_level: Experience
    primary_stack: Stack
    preferred_duration: Duration
    skills: str | None = None
    projects: List[int] = Field(min_length=1)
    availability_confirmed: bool
