import { theme } from "@/app/styles/theme";
import { Box, Stack, ThemeProvider, Typography } from "@mui/material";
import Image from "next/image";

const Title = () => {
  return (
    <ThemeProvider theme={theme}>
      <Box>
        <Stack spacing={2}>
          <Typography variant="h1">Welcome to ___</Typography>
          <Box sx={{ maxWidth: 300 }}>
            <Image src="/logo.svg" alt="Image" width={300} height={200} />
          </Box>
        </Stack>
      </Box>
    </ThemeProvider>
  );
};

export default Title;
