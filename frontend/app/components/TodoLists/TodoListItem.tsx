"use client";

import { TodoList } from "@/lib/redux/api/todoLists";
import { Typography } from "@mui/material";
import { usePathname } from "next/navigation";

interface Props {
  todoList: TodoList;
}

const TodoListItem = ({ todoList }: Props) => {
  const pathname = usePathname();
  const isActive = pathname === `/todos/${todoList.id}`;

  const handleClick = () => {
    window.location.href = `/todos/${todoList.id}`;
  };

  return (
    <>
      <Typography
        onClick={handleClick}
        color={isActive ? "primary" : "initial"}
        sx={{ cursor: "pointer" }}
      >
        {todoList.title}
      </Typography>
    </>
  );
};

export default TodoListItem;
