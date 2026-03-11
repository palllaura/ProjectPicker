from fastapi import FastAPI

from database import Base, engine
from models import user, project, user_projects

from routers import user_router, project_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(project_router.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "ProjectPicker API running"}
