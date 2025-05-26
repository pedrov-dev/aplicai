import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import Jobs from "./pages/Jobs";
import CoverLetter from "./pages/CoverLetter";

/**
 * Main App component with routing.
 * Add layout and authentication providers as needed.
 */

const App: React.FC = () => {
  return (
    <Router>
      {/* TODO: Add AppLayout and AuthProvider here */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/jobs" element={<Jobs />} />
        <Route path="/coverletters" element={<CoverLetter />} />
        {/* Add more routes as needed */}
      </Routes>
    </Router>
  );
};

export default App;