import React from "react";

/**
 * Profile Page
 * This page displays and allows editing of the user's profile information.
 * Integrate with backend API to fetch and update user data.
 */

const Profile: React.FC = () => {
  return (
    <div className="max-w-xl mx-auto py-8 px-4">
      <h1 className="text-2xl font-bold mb-4">Your Profile</h1>
      {/* TODO: Add user profile form and display user info */}
      <div className="bg-white rounded shadow p-6">
        <p className="text-gray-600">
          View and update your profile information here.
        </p>
      </div>
    </div>
  );
};

export default Profile;