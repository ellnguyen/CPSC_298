interface User {
    id: number;
    username: string;
    email: string;
    password: SecureString;
    // Additional user properties as needed
  }

  interface LoginCredentials {
    username: string;
    password: string;
  }

  interface HashedPassword {
    salt: string;
    hash: string;
  }

  interface Email {
    value: string; // Enforce email format validation
  }

  interface SecureString {
    value: string; // Enforce password length, character requirements, etc.
  }

  interface HashedPassword {
    algorithm: string;
    value: string;
  }

  async function login(credentials: LoginCredentials, userStore: (username: string) => Promise<User | null>, hashCompare: (password: string, hashedPassword: HashedPassword) => Promise<boolean>): Promise<User | null> {
    const user = await userStore(credentials.username);

    if (!user) {
      return null; // Username not found
    }

    const isMatch = await hashCompare(credentials.password, user.hashedPassword);

    if (isMatch) {
      return user; // Login successful
    }

    return null; // Invalid password
  }

  // Example usage:
  async function handleLoginFormSubmit(credentials: LoginCredentials) {
    const user = await login(credentials, getUserByUsername, compareHashedPassword);
    if (user) {
      console.log("Login successful!");
      // Store user information securely (e.g., in a signed token)
    } else {
      console.log("Invalid username or password.");
    }
  }