from fastapi import APIRouter

from app.api.v1.endpoints.todo_items import router as todos_router
from app.api.v1.endpoints.users import router as users_router

api_v1_router = APIRouter()

api_v1_router.include_router(todos_router, prefix="/todos", tags=["todos"])
api_v1_router.include_router(users_router, prefix="/users", tags=["users"])
