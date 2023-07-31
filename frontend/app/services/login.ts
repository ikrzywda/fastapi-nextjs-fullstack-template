export const login = async (email: string, password: string) => {
  try {
    const result = await fetch(
      "http://localhost:8000/api/v1/login/access-token",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded", // Correct the Content-Type value
        },
        body: new URLSearchParams({
          username: email,
          password: password,
        }).toString(), // Convert the URLSearchParams object to a string
      }
    );

    if (!result.ok) {
      // If the response status is not okay (2xx range), handle the error
      throw new Error("Failed to log in");
    }

    const json = await result.json();

    // Assuming the JSON response contains the 'access_token' field
    const accessToken = json.access_token;

    // Store the access token in localStorage
    localStorage.setItem("accessToken", accessToken);

    // Return the JSON response
    return json;
  } catch (error) {
    // Handle any errors that occur during the login process
    console.error("Error during login:", error);
    throw error; // Re-throw the error to propagate it to the caller
  }
};
