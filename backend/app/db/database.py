import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import Json

# ✅ Correct .env path (project root)
env_path = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def save_history(data: dict):
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO career_history (
                    career_goal,
                    experience_level,
                    guidance_category,
                    score,
                    gaps,
                    roadmap
                )
                VALUES (
                    :career_goal,
                    :experience_level,
                    :guidance_category,
                    :score,
                    :gaps,
                    :roadmap
                )
            """),
            {
                "career_goal": data["career_goal"],
                "experience_level": data["experience_level"],
                "guidance_category": data["guidance_category"],
                "score": data["score"],
                "gaps": data["gaps"] if data["gaps"] else None,
                "roadmap": Json(data["roadmap"]),
            }
        )
