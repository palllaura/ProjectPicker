from sqlalchemy.orm import Session
from models.project import Project


def seed_projects(db: Session):
    """Add projects to database if projects is empty."""
    projects = [
        "Customer Portal Redesign",
        "Data Pipeline Migration",
        "Mobile App Enhancement",
        "Internal Analytics Dashboard",
        "API Gateway Implementation",
        "Cloud Infrastructure Setup",
        "E-commerce Platform Update",
        "Reporting System Automation",
        "Microservices Architecture Transition",
        "Customer Data Platform Integration"
    ]

    existing = db.query(Project).count()

    if existing == 0:
        for name in projects:
            db.add(Project(name=name))

        db.commit()
