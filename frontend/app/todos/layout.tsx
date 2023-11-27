import { Box, Stack } from "@mui/material";
import TodoLists from "../components/TodoLists";

const TodosLayout = ({ children }: React.PropsWithChildren) => {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <title>Todos</title>
        <meta name="description" content="todos" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body>
        <Stack direction="row" spacing={2}>
          <Box sx={{ width: 300, height: "100vh", bgcolor: "grey.300" }}>
            <TodoLists />
          </Box>
          <Box sx={{ flexGrow: 1, height: "100vh", bgcolor: "grey.100" }}>
            {children}
          </Box>
        </Stack>
      </body>
    </html>
  );
};

export default TodosLayout;
