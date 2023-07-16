from core.config import settings
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api import api_router

app = FastAPI(app_name=settings.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
