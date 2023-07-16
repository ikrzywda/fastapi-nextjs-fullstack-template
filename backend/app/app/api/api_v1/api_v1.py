from app.api.api_v1.endpoints.todos import router as todos_router
from fastapi import APIRouter

api_v1_router = APIRouter()
api_v1_router.include_router(todos_router, prefix="/todos", tags=["todos"])
