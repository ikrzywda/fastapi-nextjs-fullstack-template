"use client";

import { Button, Stack, TextField, Typography } from "@mui/material";
import { login } from "app/services/login";
import { useState } from "react";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [authError, setAuthError] = useState(false);

  const handleLogin = async () => {
    const { error } = await login(email, password);
    if (error) {
      setAuthError(true);
    }
    window.location.href = "/todos/2137";
  };

  return (
    <>
      <Stack spacing={2}>
        <Typography variant="h1">Hello 👋</Typography>
        <Stack spacing={2}>
          <TextField
            label="Email"
            onChange={(e) => setEmail(e.currentTarget.value)}
          />
          <TextField
            label="Password"
            onChange={(e) => setPassword(e.currentTarget.value)}
          />
          {authError && (
            <Typography color="error">Failed to authenticate</Typography>
          )}
          <Button variant="contained" onClick={handleLogin}>
            Login
          </Button>
        </Stack>
      </Stack>
    </>
  );
};

export default Login;
