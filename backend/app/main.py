from fastapi import FastAPI, UploadFile, File, Form
from .pdf_utils import extract_text_from_pdf
from .graph.workflow import build_graph
from .webhook import trigger_webhook
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI()
graph = build_graph()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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
    # Normalize empty strings
    career_goal = career_goal or None
    experience_level = experience_level or None

    # ✅ API-LEVEL VALIDATION (THIS FIXES EVERYTHING)
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

    # ✅ NOW SAFE TO ENTER LANGGRAPH
    state = {
        "resume_text": resume_text,
        "career_goal": career_goal,
        "experience_level": experience_level,
    }

    result = graph.invoke(state)

    reply = result.get("career_summary")

    if not reply:
        return {"reply": "Something went wrong. Please try again."}

    trigger_webhook(result)
    
    return {
        "reply": reply,
        "guidance_category": result.get("guidance_category")
    }


