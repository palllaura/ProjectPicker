from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from database import engine, Base, SessionLocal
from models import user, project, user_projects
from routers.project_router import router as project_router
from routers.user_router import router as user_router
from seed_data import seed_projects


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Initialize database schema and seed initial project data on application startup."""
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    seed_projects(db)
    db.close()

    yield

app = FastAPI(lifespan=lifespan)
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
app.include_router(project_router)
app.include_router(user_router)


@app.get("/")
def root():
    """Serve frontend page."""
    return FileResponse("frontend/index.html")
