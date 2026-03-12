from sqlalchemy.orm import Session
from models.project import Project


def get_all_projects(db: Session):
    """Return all available projects from the database."""
    return db.query(Project).all()
