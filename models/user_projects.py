from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class UserProject(Base):
    """User projects assignment model."""
    __tablename__ = "user_projects"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)

