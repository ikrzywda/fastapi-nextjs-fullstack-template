from api.api_v1.api_v1 import api_v1_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(api_v1_router, prefix="/v1")
