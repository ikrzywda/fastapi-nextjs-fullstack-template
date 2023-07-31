import { emptySlitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    getTodoListsApiV1TodoListsGet: build.query<
      GetTodoListsApiV1TodoListsGetApiResponse,
      GetTodoListsApiV1TodoListsGetApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todo-lists`,
        params: {
          page: queryArg.page,
          page_size: queryArg.pageSize,
          search: queryArg.search,
          sorting_order: queryArg.sortingOrder,
          sorting_key: queryArg.sortingKey,
        },
      }),
    }),
    createTodoListApiV1TodoListsPost: build.mutation<
      CreateTodoListApiV1TodoListsPostApiResponse,
      CreateTodoListApiV1TodoListsPostApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todo-lists`,
        method: "POST",
        body: queryArg.todoListCreate,
      }),
    }),
    deleteTodoListApiV1TodoListsTodoListIdDelete: build.mutation<
      DeleteTodoListApiV1TodoListsTodoListIdDeleteApiResponse,
      DeleteTodoListApiV1TodoListsTodoListIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todo-lists/${queryArg.todoListId}`,
        method: "DELETE",
      }),
    }),
    getTodoItemsApiV1TodoListsTodoListIdItemsGet: build.query<
      GetTodoItemsApiV1TodoListsTodoListIdItemsGetApiResponse,
      GetTodoItemsApiV1TodoListsTodoListIdItemsGetApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todo-lists/${queryArg.todoListId}/items`,
        params: {
          page: queryArg.page,
          page_size: queryArg.pageSize,
          search: queryArg.search,
          sorting_order: queryArg.sortingOrder,
          sorting_key: queryArg.sortingKey,
        },
      }),
    }),
    createTodoItemApiV1TodoListsTodoListIdItemsPost: build.mutation<
      CreateTodoItemApiV1TodoListsTodoListIdItemsPostApiResponse,
      CreateTodoItemApiV1TodoListsTodoListIdItemsPostApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todo-lists/${queryArg.todoListId}/items`,
        method: "POST",
        body: queryArg.todoItemCreate,
      }),
    }),
    deleteTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdDelete: build.mutation<
      DeleteTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdDeleteApiResponse,
      DeleteTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todo-lists/${queryArg.todoListId}/items/${queryArg.todoItemId}`,
        method: "DELETE",
      }),
    }),
    updateTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdPatch: build.mutation<
      UpdateTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdPatchApiResponse,
      UpdateTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdPatchApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todo-lists/${queryArg.todoListId}/items/${queryArg.todoItemId}`,
        method: "PATCH",
        body: queryArg.todoItemUpdate,
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type GetTodoListsApiV1TodoListsGetApiResponse =
  /** status 200 Successful Response */ PaginatedResponseTodoList;
export type GetTodoListsApiV1TodoListsGetApiArg = {
  page?: number;
  pageSize?: number;
  search?: string;
  sortingOrder?: SortingOrder;
  sortingKey?: "id" | "title" | "created_date" | "updated_date";
};
export type CreateTodoListApiV1TodoListsPostApiResponse =
  /** status 200 Successful Response */ TodoList;
export type CreateTodoListApiV1TodoListsPostApiArg = {
  todoListCreate: TodoListCreate;
};
export type DeleteTodoListApiV1TodoListsTodoListIdDeleteApiResponse =
  /** status 200 Successful Response */ any;
export type DeleteTodoListApiV1TodoListsTodoListIdDeleteApiArg = {
  todoListId: number;
};
export type GetTodoItemsApiV1TodoListsTodoListIdItemsGetApiResponse =
  /** status 200 Successful Response */ PaginatedResponseTodoItem;
export type GetTodoItemsApiV1TodoListsTodoListIdItemsGetApiArg = {
  todoListId: number;
  page?: number;
  pageSize?: number;
  search?: string;
  sortingOrder?: SortingOrder;
  sortingKey?: "id" | "title" | "created_date" | "updated_date";
};
export type CreateTodoItemApiV1TodoListsTodoListIdItemsPostApiResponse =
  /** status 200 Successful Response */ TodoItem;
export type CreateTodoItemApiV1TodoListsTodoListIdItemsPostApiArg = {
  todoListId: number;
  todoItemCreate: TodoItemCreate;
};
export type DeleteTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdDeleteApiResponse =
  /** status 200 Successful Response */ any;
export type DeleteTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdDeleteApiArg =
  {
    todoListId: number;
    todoItemId: number;
  };
export type UpdateTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdPatchApiResponse =
  /** status 200 Successful Response */ TodoItem;
export type UpdateTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdPatchApiArg = {
  todoListId: number;
  todoItemId: number;
  todoItemUpdate: TodoItemUpdate;
};
export type TodoList = {
  id?: number;
  user_id?: number;
  title: string;
  description: string;
  created_date?: string;
  updated_date?: string;
};
export type PaginatedResponseTodoList = {
  total: number;
  page: number;
  per_page: number;
  items: TodoList[];
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type SortingOrder = "asc" | "desc";
export type TodoListCreate = {
  title: string;
  description: string;
};
export type TodoItem = {
  id?: number;
  title: string;
  description?: string;
  is_completed?: boolean;
  due_date?: string;
  todo_list_id?: number;
  created_date?: string;
  updated_date?: string;
};
export type PaginatedResponseTodoItem = {
  total: number;
  page: number;
  per_page: number;
  items: TodoItem[];
};
export type TodoItemCreate = {
  title: string;
  description?: string;
  is_completed?: boolean;
  due_date?: string;
};
export type TodoItemUpdate = {
  title?: string;
  description?: string;
  due_date?: string;
  is_completed?: boolean;
};
export const {
  useGetTodoListsApiV1TodoListsGetQuery,
  useLazyGetTodoListsApiV1TodoListsGetQuery,
  useCreateTodoListApiV1TodoListsPostMutation,
  useDeleteTodoListApiV1TodoListsTodoListIdDeleteMutation,
  useGetTodoItemsApiV1TodoListsTodoListIdItemsGetQuery,
  useLazyGetTodoItemsApiV1TodoListsTodoListIdItemsGetQuery,
  useCreateTodoItemApiV1TodoListsTodoListIdItemsPostMutation,
  useDeleteTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdDeleteMutation,
  useUpdateTodoItemApiV1TodoListsTodoListIdItemsTodoItemIdPatchMutation,
} = injectedRtkApi;
