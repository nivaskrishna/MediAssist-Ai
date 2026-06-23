from pydantic_settings import BaseSettings, SettingsConfigDict

import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "MediAssist AI"
    # Use /tmp on Vercel (ephemeral but writable) to avoid read-only filesystem errors
    DATABASE_URL: str = "sqlite+aiosqlite:////tmp/mediassist.db" if os.environ.get("VERCEL") else "sqlite+aiosqlite:///./mediassist.db"
    GEMINI_API_KEY: str = ""
    FRONTEND_URL: str = "http://localhost:5173"
    HUGGINGFACE_API_KEY: str = ""  # HuggingFace Inference API key for SDXL

    # Phase 1 — OpenFDA (optional, increases quota from 1k to 120k/day)
    OPENFDA_API_KEY: str = ""

    # Phase 3 — OpenRouter (free AI fallback when Gemini is unavailable)
    OPENROUTER_API_KEY: str = ""

    # Phase 4 — MongoDB Atlas (for chat history + saved diagnoses)
    MONGODB_URI: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
