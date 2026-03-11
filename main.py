from fastapi import FastAPI

from routers import user_router, project_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(project_router.router)
