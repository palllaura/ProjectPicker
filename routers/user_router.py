from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.user_schema import UserSubmission
from services.user_service import submit_user_profile

router = APIRouter()


def get_db():
    """Provide a database session for the request lifecycle."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/submit")
def submit_user(user_submission: UserSubmission, db: Session = Depends(get_db)):
    """Receive a user profile submission and forward it to the service layer."""
    return submit_user_profile(db, user_submission)
