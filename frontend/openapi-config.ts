import type { ConfigFile } from "@rtk-query/codegen-openapi";

const config: ConfigFile = {
  schemaFile: "http://localhost:8000/api/v1/openapi.json",
  apiFile: "./lib/redux/api/emptyApi.ts",
  apiImport: "emptySlitApi",
  exportName: "api",
  hooks: true,
  outputFiles: {
    "./lib/redux/api/todos.ts": {
      filterEndpoints: [/todos/i],
    },
  },
};

export default config;
