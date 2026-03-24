from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}


@app.get("/config-test")
def config_test():
    return {
        "project_name": settings.PROJECT_NAME,
        "database_url": settings.DATABASE_URL
    }
