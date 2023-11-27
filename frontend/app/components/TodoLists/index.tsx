"use client";

import { useGetTodoListsApiV1TodoListsGetQuery } from "@/lib/redux/api/todoLists";
import TodoListItem from "./TodoListItem";
import { Stack } from "@mui/material";
import TodoListsHeader from "./Header";

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
      <Stack direction="row" spacing={2}>
        <TodoListsHeader onAddClick={() => {}} />
        {data &&
          data!.items.map((todoList) => (
            <TodoListItem key={todoList.id} todoList={todoList} />
          ))}
      </Stack>
    </>
  );
};
export default TodoLists;
