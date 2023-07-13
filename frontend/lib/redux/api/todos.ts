import { emptySplitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    getTodoApiV1TodosGet: build.query<
      GetTodoApiV1TodosGetApiResponse,
      GetTodoApiV1TodosGetApiArg
    >({
      query: () => ({ url: `/api/v1/todos` }),
    }),
    createTodoApiV1TodosPost: build.mutation<
      CreateTodoApiV1TodosPostApiResponse,
      CreateTodoApiV1TodosPostApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todos`,
        method: "POST",
        body: queryArg.todoCreate,
      }),
    }),
    deleteTodoApiV1TodosTodoIdDelete: build.mutation<
      DeleteTodoApiV1TodosTodoIdDeleteApiResponse,
      DeleteTodoApiV1TodosTodoIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todos/${queryArg.todoId}`,
        method: "DELETE",
      }),
    }),
    updateTodoApiV1TodosTodoIdPatch: build.mutation<
      UpdateTodoApiV1TodosTodoIdPatchApiResponse,
      UpdateTodoApiV1TodosTodoIdPatchApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/todos/${queryArg.todoId}`,
        method: "PATCH",
        body: queryArg.todoCreate,
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type GetTodoApiV1TodosGetApiResponse =
  /** status 200 Successful Response */ Todo[];
export type GetTodoApiV1TodosGetApiArg = void;
export type CreateTodoApiV1TodosPostApiResponse =
  /** status 200 Successful Response */ Todo;
export type CreateTodoApiV1TodosPostApiArg = {
  todoCreate: TodoCreate;
};
export type DeleteTodoApiV1TodosTodoIdDeleteApiResponse =
  /** status 200 Successful Response */ any;
export type DeleteTodoApiV1TodosTodoIdDeleteApiArg = {
  todoId: number;
};
export type UpdateTodoApiV1TodosTodoIdPatchApiResponse =
  /** status 200 Successful Response */ Todo;
export type UpdateTodoApiV1TodosTodoIdPatchApiArg = {
  todoId: number;
  todoCreate: TodoCreate;
};
export type Todo = {
  title: string;
  description?: string;
  id: number;
  completed_on?: string;
  created_on: string;
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type TodoCreate = {
  title: string;
  description?: string;
};
export const {
  useGetTodoApiV1TodosGetQuery,
  useCreateTodoApiV1TodosPostMutation,
  useDeleteTodoApiV1TodosTodoIdDeleteMutation,
  useUpdateTodoApiV1TodosTodoIdPatchMutation,
} = injectedRtkApi;
