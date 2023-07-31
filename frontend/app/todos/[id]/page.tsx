const TodoListPage = ({ params }: { params: { id: number } }) => {
  return <div>Todo List {params.id}</div>;
};

export default TodoListPage;
