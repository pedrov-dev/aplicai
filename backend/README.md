# CoverLetterGPT Backend

This is the FastAPI backend for CoverLetterGPT, an AI-powered cover letter generator.

## Features

- RESTful API for cover letter and job management
- User authentication (Supabase Auth or Firebase Auth)
- Integration with OpenAI GPT-4 for cover letter drafting
- PDF generation (WeasyPrint)
- PostgreSQL database (via Docker, Supabase, or Railway)
- Stripe integration for payments (optional)

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (for local development)
- PostgreSQL database (local, Railway, or Supabase)

### Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   - Copy `.env.server.example` to `.env.server` and fill in your secrets.

3. **Run database migrations:**  
   *(If using Alembic or similar, otherwise skip)*
   ```sh
   # Example: alembic upgrade head
   ```

4. **Start the server:**
   ```sh
   uvicorn app.main:app --reload
   ```

Or use Docker Compose from the project root:
```sh
docker-compose up --build
```

### Project Structure

```
backend/
  app/
    main.py
    api/
    core/
    crud/
    db/
    schemas/
    services/
  requirements.txt
  .env.server
```

### Development Notes

- API runs at `http://localhost:8000`
- Update `.env.server` for your environment
- See `app/services/ai.py` for OpenAI integration

---

## Refactoring Plan

See [backend/README.md](backend/README.md) for a detailed step-by-step refactoring plan.

---

## License

MIT