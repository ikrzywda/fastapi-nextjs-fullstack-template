from fastapi import FastAPI
from core.config import settings
from api.api import api_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(app_name=settings.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

app.include_router(api_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
