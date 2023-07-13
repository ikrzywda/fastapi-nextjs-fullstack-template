"use client";

import { useGetTodoApiV1TodosGetQuery } from "@/lib/redux/api/todos";

export const Counter = () => {
  const { data, error, isLoading } = useGetTodoApiV1TodosGetQuery();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      {error && <div>Oh no, there was an error</div>}
      {data && (
        <div>
          {data.map((todo) => (
            <div key={todo.id}>{todo.title}</div>
          ))}
        </div>
      )}
    </>
  );
};
