from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.user_schema import UserSubmission
from models.user import User
from models.user_projects import UserProject


def submit_user_profile(db: Session, submission: UserSubmission):
    """Handle user profile submission by creating or updating a user profile."""

    if not submission.availability_confirmed:
        raise HTTPException(
            status_code=400,
            detail="Availability must be confirmed"
        )

    user = db.query(User).filter_by(email=submission.email).first()

    if user:
        user.name = submission.name
        user.experience_level = submission.experience_level.value
        user.primary_stack = submission.primary_stack.value
        user.preferred_duration = submission.preferred_duration.value
        user.skills = submission.skills
        user.availability_confirmed = submission.availability_confirmed

    else:
        user = User(
            name=submission.name,
            email=submission.email,
            experience_level=submission.experience_level.value,
            primary_stack=submission.primary_stack.value,
            preferred_duration=submission.preferred_duration.value,
            skills=submission.skills,
            availability_confirmed=submission.availability_confirmed
        )
        db.add(user)
        db.flush()

    db.query(UserProject).filter_by(user_id=user.id).delete()

    for project_id in submission.projects:
        user_project = UserProject(
            user_id=user.id,
            project_id=project_id
        )
        db.add(user_project)

    db.commit()
    db.refresh(user)

    return {
        "message": "Profile saved successfully",
        "user": {
            "name": user.name,
            "email": user.email,
            "experience_level": user.experience_level,
            "primary_stack": user.primary_stack,
            "preferred_duration": user.preferred_duration,
            "skills": user.skills,
            "projects": submission.projects
        }
    }
