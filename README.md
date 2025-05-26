# CoverLetterGPT

AI-powered cover letter generator built with **FastAPI** (Python), **React** (with Tailwind CSS), and **PostgreSQL**.  
Easily generate, edit, and manage professional cover letters for your job applications.

---

## Features

- ✨ Generate cover letters using OpenAI GPT-4
- 📝 Edit, save, and export cover letters as PDF
- 🗂️ Manage job applications and related cover letters
- 🔒 User authentication (Supabase Auth or Firebase Auth)
- 💳 Stripe integration for payments (optional)
- 🚀 Modern stack: FastAPI, React, Tailwind CSS, PostgreSQL, Docker

---

## Tech Stack

- **Frontend:** React, Tailwind CSS, Vite
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL (via Docker, Supabase, or Railway)
- **Authentication:** Supabase Auth or Firebase Auth
- **AI:** OpenAI API (GPT-4)
- **PDF Generation:** WeasyPrint (backend) or jsPDF (frontend)
- **Payments:** Stripe (optional)
- **Hosting:** Vercel (frontend), Railway (backend), Docker Compose (local)

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Node.js](https://nodejs.org/) (for frontend development)
- [Python 3.10+](https://www.python.org/) (for backend development)

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/coverlettergpt.git
cd coverlettergpt
```

### 2. Set up environment variables

Copy the example files and fill in your secrets:

```sh
cp .env.example .env
cp backend/.env.server.example backend/.env.server
cp frontend/.env.example frontend/.env
```

Edit these files to add your OpenAI, Supabase, Stripe, and database credentials.

### 3. Start with Docker Compose

```sh
docker-compose up --build
```

- Backend: [http://localhost:8000](http://localhost:8000)
- Frontend: [http://localhost:5173](http://localhost:5173)
- Database: [localhost:5432](localhost:5432)

### 4. Manual Development (optional)

#### Backend

```sh
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend

```sh
cd frontend
npm install
npm run dev
```

---

## Project Structure

```
coverlettergpt-refactor/
│
├── backend/         # FastAPI backend
│   ├── app/
│   ├── requirements.txt
│   └── ...
├── frontend/        # React frontend (Vite + Tailwind)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
├── docker-compose.yml
├── .env
└── README.md
```

---

## Customization

- **Authentication:** Choose Supabase or Firebase and update the relevant config and components.
- **Payments:** Enable Stripe by adding your keys and enabling payment endpoints.
- **PDF Export:** Use WeasyPrint (backend) or jsPDF (frontend) as needed.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE)

---

## Credits

- [OpenAI](https://openai.com/)
- [Supabase](https://supabase.com/)
- [Stripe](https://stripe.com/)
- [WeasyPrint](https://weasyprint.org/)
- [Vercel](https://vercel.com/)
- [Railway](https://railway.app/)