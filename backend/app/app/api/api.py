from api.v1.api_v1 import api_v1_router
from fastapi import APIRouter
from core.config import settings

api_router = APIRouter()

api_router.include_router(api_v1_router, prefix=settings.API_V1_STR)
