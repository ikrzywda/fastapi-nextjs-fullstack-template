"use client";

import { Button, Stack, TextField, Typography } from "@mui/material";
import { useState } from "react";

interface LoginFormProps {
  onLogin: (email: string, password: string) => void;
}

const LoginForm = ({ onLogin }: LoginFormProps) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    onLogin(email, password);
  };

  return (
    <Stack spacing={2} sx={{ maxWidth: 300 }}>
      <TextField
        label="Email"
        onChange={(e) => setEmail(e.currentTarget.value)}
      />
      <TextField
        label="Password"
        onChange={(e) => setPassword(e.currentTarget.value)}
      />
      <Button variant="contained" onClick={handleLogin}>
        Login
      </Button>
    </Stack>
  );
};

export default LoginForm;
