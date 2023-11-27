import { useGetTodoItemsApiV1TodoListsTodoListIdItemsGetQuery } from "@/lib/redux/api/todoLists";
import { Typography } from "@mui/material";

interface Props {
  todoListId: number;
}

const TodoList = ({ todoListId }: Props) => {
  const { data: todoListItems, isLoading } =
    useGetTodoItemsApiV1TodoListsTodoListIdItemsGetQuery({
      todoListId,
      page: 1,
      pageSize: 100,
    });

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      {todoListItems &&
        todoListItems!.items.map((todoList) => (
          <Typography key={todoList.id}>{todoList.title}</Typography>
        ))}
    </>
  );
};

export default TodoList;
