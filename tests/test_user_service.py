from services.user_service import submit_user_profile
from schemas.user_schema import UserSubmission
from models.user import User
from models.user_projects import UserProject
from models.user import Experience, Stack, Duration


def test_submit_user_creates_new_user(db, projects_seed):
    """Verify that a new user and project selections are created."""

    submission = UserSubmission(
        name="Alice",
        email="alice@test.com",
        experience_level=Experience.MID,
        primary_stack=Stack.BACKEND,
        preferred_duration=Duration.SHORT,
        skills="Python",
        projects=[1, 2],
        availability_confirmed=True
    )

    submit_user_profile(db, submission)

    user = db.query(User).filter_by(email="alice@test.com").first()

    assert user is not None
    assert user.name == "Alice"

    user_projects = db.query(UserProject).filter_by(user_id=user.id).all()

    assert len(user_projects) == 2


def test_submit_user_updates_existing_user(db, projects_seed):
    """Verify that submitting with the same email updates the user."""

    submission = UserSubmission(
        name="Bob",
        email="bob@test.com",
        experience_level=Experience.JUNIOR,
        primary_stack=Stack.FRONTEND,
        preferred_duration=Duration.SHORT,
        skills="JS",
        projects=[1],
        availability_confirmed=True
    )

    submit_user_profile(db, submission)

    updated_submission = UserSubmission(
        name="Bob Updated",
        email="bob@test.com",
        experience_level=Experience.SENIOR,
        primary_stack=Stack.BACKEND,
        preferred_duration=Duration.LONG,
        skills="Python",
        projects=[2, 3],
        availability_confirmed=True
    )

    submit_user_profile(db, updated_submission)

    user = db.query(User).filter_by(email="bob@test.com").first()

    assert user.name == "Bob Updated"
    assert user.experience_level == Experience.SENIOR.value

    user_projects = db.query(UserProject).filter_by(user_id=user.id).all()
    assert len(user_projects) == 2
