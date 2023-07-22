from fastapi import APIRouter

from app.api.v1.endpoints.login import router as login_router
from app.api.v1.endpoints.todo_lists import router as todo_lists_router
from app.api.v1.endpoints.users import router as users_router

api_v1_router = APIRouter()

api_v1_router.include_router(users_router, prefix="/users", tags=["users"])
api_v1_router.include_router(login_router, prefix="/login", tags=["login"])
api_v1_router.include_router(todo_lists_router)
