import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

class Settings:
    PROJECT_NAME: str = "CoverLetterGPT"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    # Add other config variables as needed

settings = Settings()