import { Box, Stack, Typography } from "@mui/material";

const testData = ["todo-1", "todo-2", "todo-3", "todo-4", "todo-5", "todo-6"];

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
            <Stack spacing={2}>
              {testData.map((todo) => (
                <Typography key={todo}>{todo}</Typography>
              ))}
            </Stack>
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
