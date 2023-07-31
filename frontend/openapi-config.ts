import type { ConfigFile } from "@rtk-query/codegen-openapi";

const config: ConfigFile = {
  schemaFile: "http://localhost:8000/api/v1/openapi.json",
  apiFile: "./lib/redux/api/emptyApi.ts",
  apiImport: "emptySlitApi",
  exportName: "api",
  hooks: { queries: true, lazyQueries: true, mutations: true },
  outputFiles: {
    "./lib/redux/api/todoLists.ts": {
      filterEndpoints: (endpoint) => endpoint.includes("TodoList"),
    },
    "./lib/redux/api/users.ts": {
      filterEndpoints: (endpoint) => endpoint.includes("User"),
    },
    "./lib/redux/api/login.ts": {
      filterEndpoints: (endpoint) => endpoint.includes("Login"),
    },
  },
};

export default config;
