import { createTheme } from "@mui/material";

export const theme = createTheme({
  palette: {
    primary: {
      main: "#000000",
    },
    secondary: {
      main: "#ffffff",
    },
  },
  typography: {
    fontFamily: "Roboto",
    h1: {
      fontSize: "3rem",
      fontWeight: 700,
      "@media (min-width:600px)": {
        fontSize: "5rem",
      },
    },
  },
});
