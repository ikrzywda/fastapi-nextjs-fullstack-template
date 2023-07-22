from fastapi import APIRouter


from app.api.v1.endpoints.todo_lists.todo_lists import router as todo_lists_router

router = APIRouter()

router.include_router(todo_lists_router, prefix="/todo-lists", tags=["todo_lists"])
