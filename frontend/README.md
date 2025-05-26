# CoverLetterGPT Frontend

This is the React + Tailwind CSS frontend for CoverLetterGPT.

## Features

- Modern React UI with Tailwind CSS
- Authentication (Supabase Auth or Firebase Auth)
- Manage jobs and cover letters
- Integrate with backend API for CRUD operations
- Export cover letters as PDF (jsPDF or via backend)
- Responsive design

## Getting Started

### Prerequisites

- Node.js (v18+ recommended)
- npm or yarn

### Setup

1. **Install dependencies:**
   ```sh
   npm install
   # or
   yarn
   ```

2. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your API URLs and keys.

3. **Start the development server:**
   ```sh
   npm run dev
   # or
   yarn dev
   ```

- App runs at `http://localhost:5173` by default.

### Project Structure

```
frontend/
  src/
    components/
    pages/
    assets/
    App.tsx
    index.tsx
    tailwind.css
  public/
  package.json
  tailwind.config.js
  tsconfig.json
  .env
```

### Development Notes

- Update `VITE_API_URL` in `.env` to point to your backend.
- See `src/components/Auth` for authentication logic.
- See `src/components/CoverLetter` for cover letter UI.

---

## License

MIT