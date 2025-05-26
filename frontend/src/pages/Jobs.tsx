import React from "react";

/**
 * Jobs Page
 * This page displays the user's jobs and allows CRUD operations.
 * Integrate with backend API for job management.
 */

const Jobs: React.FC = () => {
  return (
    <div className="max-w-3xl mx-auto py-8 px-4">
      <h1 className="text-2xl font-bold mb-4">Your Jobs</h1>
      {/* TODO: Add JobList, JobForm, or JobView components here */}
      <div className="bg-white rounded shadow p-6">
        <p className="text-gray-600">
          Here you can add, edit, and manage your job applications.
        </p>
      </div>
    </div>
  );
};

export default Jobs;