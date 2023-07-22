from fastapi import APIRouter


from app.api.v1.endpoints.todo_lists.todo_lists import router as todo_lists_router
from app.api.v1.endpoints.todo_lists.todo_items import router as todo_items_router

router = APIRouter()

router.include_router(todo_lists_router, prefix="/todo-lists", tags=["todo_lists"])
router.include_router(todo_items_router, prefix="/todo-lists", tags=["todo_items"])
