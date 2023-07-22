from typing import Optional

from sqlmodel import Session, and_, func, select

from app.crud.base import CRUDBase
from app.models.todo_item import (
    TodoItem,
    TodoItemCreate,
    TodoItemSortingFields,
    TodoItemUpdate,
)
from app.schamas.paginated_response import PaginatedResponse, SortingOrder


class CRUDTodoItem(CRUDBase[TodoItem, TodoItemCreate, TodoItemUpdate]):
    def get_for_list_paginated(
        self,
        db: Session,
        *,
        todo_list_id: int,
        page: int,
        per_page: int,
        search: Optional[str] = None,
        sorting_key: TodoItemSortingFields,
        sorting_order: SortingOrder,
    ) -> PaginatedResponse[TodoItem]:
        query = select(TodoItem).where(
            and_(
                TodoItem.todo_list_id == todo_list_id,
                TodoItem.title.like(f"%{search}%" if search else "%"),
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

        return PaginatedResponse[TodoItem](
            items=items, total=all_count, page=page, per_page=per_page
        )

    def get_for_list(
        self,
        db: Session,
        *,
        todo_list_id: int,
    ) -> Optional[TodoItem]:
        query = select(TodoItem).where(TodoItem.todo_list_id == todo_list_id)
        items = db.exec(query).first()
        return items

    def create_for_list(
        self, db, *, obj_in: TodoItemCreate, todo_list_id: int
    ) -> TodoItem:
        todo_item = TodoItem(**obj_in.dict(), todo_list_id=todo_list_id)
        db.add(todo_item)
        db.commit()
        db.refresh(todo_item)
        return todo_item


crud_todo_item = CRUDTodoItem(TodoItem)
