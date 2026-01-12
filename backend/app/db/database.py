import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import Json

# -----------------------------------
# Environment variable (SAFE)
# -----------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in environment")

# -----------------------------------
# SQLAlchemy Engine
# -----------------------------------
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# -----------------------------------
# Insert helper (AUTO-COMMIT SAFE)
# -----------------------------------
def save_history(data: dict):
    """
    Safely inserts a career history record.
    Uses engine.begin() to ensure commit.
    """

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
                "gaps": data["gaps"] if data.get("gaps") else None,
                "roadmap": Json(data["roadmap"]) if data.get("roadmap") else None,
            }
        )
