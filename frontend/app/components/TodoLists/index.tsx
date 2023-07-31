"use client";

import { useGetTodoListsApiV1TodoListsGetQuery } from "@/lib/redux/api/todoLists";
import TodoListItem from "./TodoListItem";

const TodoLists = () => {
  const { data, isLoading } = useGetTodoListsApiV1TodoListsGetQuery({
    page: 1,
    pageSize: 100,
  });

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      {data &&
        data!.items.map((todoList) => (
          <TodoListItem key={todoList.id} todoList={todoList} />
        ))}
    </>
  );
};
export default TodoLists;
