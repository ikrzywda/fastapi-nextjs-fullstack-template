"use client";

import {
  Button,
  Grid,
  Stack,
  TextField,
  ThemeProvider,
  Typography,
} from "@mui/material";
import { login } from "app/services/login";
import { useState } from "react";
import LoginForm from "../components/Login/LoginForm";
import { theme } from "../styles/theme";
import Title from "../components/Login/Title";

const Login = () => {
  const [authError, setAuthError] = useState(false);

  const handleLogin = async (email: string, password: string) => {
    const { error } = await login(email, password);
    if (error) {
      setAuthError(true);
    }
    window.location.href = "/todos/2137";
  };

  return (
    <>
      <Grid
        container
        spacing={5}
        columns={12}
        alignItems="center"
        sx={{ minHeight: "100vh" }}
      >
        <Grid item xs={8}>
          <Title />
        </Grid>
        <Grid item xs={4}>
          <LoginForm onLogin={handleLogin} />
        </Grid>
      </Grid>
      {authError && (
        <Typography color="error">Failed to authenticate</Typography>
      )}
    </>
  );
};

export default Login;
