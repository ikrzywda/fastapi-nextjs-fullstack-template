"use client";

import TodoList from "app/components/TodoList";

const TodoListPage = ({ params }: { params: { id: number } }) => {
  return <TodoList todoListId={params.id} />;
};

export default TodoListPage;
