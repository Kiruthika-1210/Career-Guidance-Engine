from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
from app.pdf_utils import extract_text_from_pdf
from app.graph.workflow import build_graph
from app.webhook import trigger_webhook
from app.db.database import save_history

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI(title="Career Guidance Engine API")
graph = build_graph()

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Career Guidance Engine Backend",
        "docs": "/docs"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(
    message: Optional[str] = Form(None),
    career_goal: Optional[str] = Form(None),
    experience_level: Optional[str] = Form(None),
    resume: Optional[UploadFile] = File(None),
):
    career_goal = career_goal or None
    experience_level = experience_level or None

    if not career_goal:
        return {"reply": "What is your target career role?"}

    if not experience_level:
        return {
            "reply": "What is your experience level? (student / fresher / early-career)"
        }

    resume_text = None
    if resume and resume.filename:
        resume_text = extract_text_from_pdf(resume.file)

    if not resume_text:
        return {"reply": "Please upload your resume (PDF)."}

    state = {
        "resume_text": resume_text,
        "career_goal": career_goal,
        "experience_level": experience_level,
    }

    try:
        result = graph.invoke(state)
    except Exception as e:
        print("Graph failed:", e)
        return {"reply": "Analysis failed. Please try again later."}

    reply = result.get("final_reply")
    if not reply:
        return {"reply": "Something went wrong. Please try again."}

    # ✅ DB save (non-blocking)
    try:
        save_history({
            "career_goal": career_goal,
            "experience_level": experience_level,
            "guidance_category": result.get("guidance_category"),
            "score": result.get("score"),
            "gaps": result.get("gaps"),
            "roadmap": result.get("roadmap"),
        })
    except Exception as e:
        print("DB save failed:", e)

    # ✅ Webhook (non-blocking)
    try:
        trigger_webhook(result)
    except Exception as e:
        print("Webhook failed:", e)

    return {
        "reply": reply,
        "guidance_category": result.get("guidance_category"),
        "roadmap": result.get("roadmap"),
        "score": result.get("score"),
    }



