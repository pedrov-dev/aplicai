import React from "react";

/**
 * Login Page
 * This page displays the login form for users.
 * Integrate with Supabase Auth or Firebase Auth for authentication.
 */

const Login: React.FC = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
      <div className="w-full max-w-md bg-white rounded shadow p-8">
        <h1 className="text-2xl font-bold mb-6 text-center">Login</h1>
        {/* TODO: Replace with <LoginForm /> component */}
        <form>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="email">
              Email
            </label>
            <input
              className="w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300"
              type="email"
              id="email"
              name="email"
              required
              autoComplete="email"
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 mb-2" htmlFor="password">
              Password
            </label>
            <input
              className="w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300"
              type="password"
              id="password"
              name="password"
              required
              autoComplete="current-password"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
          >
            Login
          </button>
        </form>
        <div className="mt-4 text-center">
          <a href="/register" className="text-blue-600 hover:underline">
            Don't have an account? Register
          </a>
        </div>
      </div>
    </div>
  );
};

export default Login;