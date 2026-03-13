"""Tests for project service functions."""

from models.project import Project
from services.project_service import get_all_projects


def test_get_all_projects_returns_projects(db):
    """Verify that all projects are returned when the database contains projects."""
    project1 = Project(name="Project A")
    project2 = Project(name="Project B")

    db.add(project1)
    db.add(project2)
    db.commit()

    projects = get_all_projects(db)
    names = [p.name for p in projects]

    assert len(projects) == 2
    assert "Project A" in names
    assert "Project B" in names


def test_get_all_projects_empty(db):
    """Verify that an empty list is returned when no projects exist."""

    projects = get_all_projects(db)

    assert len(projects) == 0
