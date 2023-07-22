from typing import Optional

from sqlmodel import Session, and_, func, select

from app.crud.base import CRUDBase
from app.models.todo_list import (
    TodoList,
    TodoListCreate,
    TodoListSortingFields,
    TodoListUpdate,
)
from app.schamas.paginated_response import PaginatedResponse, SortingOrder


class CrudTodoList(CRUDBase[TodoList, TodoListCreate, TodoListUpdate]):
    def get_for_user_paginated(
        self,
        db: Session,
        *,
        user_id: int,
        page: int,
        per_page: int,
        search: Optional[str] = None,
        sorting_key: TodoListSortingFields,
        sorting_order: SortingOrder,
    ) -> PaginatedResponse[TodoList]:
        query = select(TodoList).where(
            and_(
                TodoList.user_id == user_id,
                TodoList.title.ilike(f"%{search}%" if search else "%"),
            )
        )
        skip = (page - 1) * per_page
        pagination_query = (
            query.order_by(
                self.get_order_by_expression(
                    sorting_key=sorting_key, sorting_order=sorting_order
                )
            )
            .offset(skip)
            .limit(per_page)
        )
        items = db.exec(pagination_query).unique().all()
        all_count = db.exec(select(func.count()).select_from(query)).one()

        return PaginatedResponse[TodoList](
            items=items, total=all_count, page=page, per_page=per_page
        )

    def get_for_user(
        self,
        db: Session,
        *,
        id: int,
        user_id: int,
    ) -> Optional[TodoList]:
        query = select(TodoList).where(
            and_(TodoList.id == id, TodoList.user_id == user_id)
        )
        items = db.exec(query).first()
        return items

    def create_for_user(
        self, db: Session, *, obj_in: TodoListCreate, user_id: int
    ) -> TodoList:
        todo_list = TodoList(**obj_in.dict(), user_id=user_id)
        db.add(todo_list)
        db.commit()
        db.refresh(todo_list)
        return todo_list


crud_todo_list = CrudTodoList(TodoList)
