import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from models import user, project, user_projects
from models.project import Project

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def db():
    """Provide a clean test database session."""

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def projects_seed(db):
    """Insert sample projects into the test database."""

    projects = [
        Project(id=1, name="Project A"),
        Project(id=2, name="Project B"),
        Project(id=3, name="Project C"),
    ]

    db.add_all(projects)
    db.commit()

    return projects
