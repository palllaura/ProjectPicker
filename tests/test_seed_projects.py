from models.project import Project
from seed_data import seed_projects


def test_seed_projects_inserts_projects(db):
    """Seed function should insert projects into an empty database."""

    seed_projects(db)

    projects = db.query(Project).all()

    assert len(projects) > 0


def test_seed_projects_not_duplicate(db):
    """Running seed twice should not create duplicate projects."""

    seed_projects(db)
    seed_projects(db)

    projects = db.query(Project).all()

    assert len(projects) == 10
