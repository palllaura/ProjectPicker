from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from services.project_service import get_all_projects

router = APIRouter()


def get_db():
    """Provide a database session for request handling and ensure it is closed afterward."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/projects")
def list_projects(db: Session = Depends(get_db)):
    """Return all available projects."""
    return get_all_projects(db)
