import { emptySlitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    createUserApiV1UsersPost: build.mutation<
      CreateUserApiV1UsersPostApiResponse,
      CreateUserApiV1UsersPostApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/users`,
        method: "POST",
        body: queryArg.userCreate,
      }),
    }),
    deleteUserApiV1UsersUserIdDelete: build.mutation<
      DeleteUserApiV1UsersUserIdDeleteApiResponse,
      DeleteUserApiV1UsersUserIdDeleteApiArg
    >({
      query: (queryArg) => ({
        url: `/api/v1/users/${queryArg.userId}`,
        method: "DELETE",
      }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as api };
export type CreateUserApiV1UsersPostApiResponse =
  /** status 200 Successful Response */ User;
export type CreateUserApiV1UsersPostApiArg = {
  userCreate: UserCreate;
};
export type DeleteUserApiV1UsersUserIdDeleteApiResponse =
  /** status 200 Successful Response */ any;
export type DeleteUserApiV1UsersUserIdDeleteApiArg = {
  userId: number;
};
export type User = {
  id?: number;
  username: string;
  email: string;
  hashed_password: string;
  is_superuser?: boolean;
  created_date?: string;
  updated_date?: string;
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type UserCreate = {
  email: string;
  username: string;
  password: string;
  is_superuser?: boolean;
};
export const {
  useCreateUserApiV1UsersPostMutation,
  useDeleteUserApiV1UsersUserIdDeleteMutation,
} = injectedRtkApi;
