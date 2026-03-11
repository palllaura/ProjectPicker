from database import SessionLocal
from models.project import Project
from seed_data import seed_projects


def test_seed_projects_inserts_projects():
    """Seed function should insert projects into an empty database."""

    db = SessionLocal()

    seed_projects(db)

    projects = db.query(Project).all()

    assert len(projects) > 0

    db.close()


def test_seed_projects_not_duplicate():
    """Running seed twice should not create duplicate projects."""

    db = SessionLocal()

    seed_projects(db)
    seed_projects(db)

    projects = db.query(Project).all()

    assert len(projects) == 10
    db.close()
