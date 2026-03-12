"""Tests for project service functions."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from models.project import Project
from services.project_service import get_all_projects


engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def db():
    """Create a temporary database session for each test."""
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)


def test_get_all_projects_returns_projects(db):
    """Verify that all projects are returned when the database contains projects."""
    project1 = Project(name="Project A")
    project2 = Project(name="Project B")

    db.add(project1)
    db.add(project2)
    db.commit()

    projects = get_all_projects(db)

    assert len(projects) == 2
    assert projects[0].name == "Project A"
    assert projects[1].name == "Project B"


def test_get_all_projects_empty(db):
    """Verify that an empty list is returned when no projects exist."""
    projects = get_all_projects(db)

    assert projects == []
