from sqlalchemy.orm import Session
from schemas.user_schema import UserSubmission


def submit_user_profile(db: Session, submission: UserSubmission):
    """Handle user profile submission."""

    # TODO: handle submission

    return {"message": "Submission received"}
