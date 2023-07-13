from fastapi import FastAPI
from core.config import settings
from api.api import api_router

app = FastAPI(app_name=settings.PROJECT_NAME)

app.include_router(api_router)
