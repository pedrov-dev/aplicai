import React from "react";

/**
 * Home Page
 * This is the landing page for CoverLetterGPT.
 * Introduce the app, its features, and provide navigation to login/register or dashboard.
 */

const Home: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 px-4">
      <h1 className="text-4xl font-bold mb-4 text-center">CoverLetterGPT</h1>
      <p className="text-lg text-gray-700 mb-8 text-center max-w-xl">
        Instantly generate professional cover letters tailored to your job applications using AI. Save time, impress employers, and land your next job faster.
      </p>
      <div className="flex space-x-4">
        <a
          href="/login"
          className="px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
        >
          Login
        </a>
        <a
          href="/register"
          className="px-6 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300 transition"
        >
          Register
        </a>
      </div>
    </div>
  );
};

export default Home;