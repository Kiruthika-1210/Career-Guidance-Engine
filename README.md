# 🎯 Career Guidance Engine (Resume-Centric AI Advisor)

A full-stack career guidance system that analyzes a user's **resume**, **career goal**, and **experience level** to generate **personalized, actionable career guidance**.

Built with **FastAPI**, **LangGraph**, and **React (Vite)**, this project demonstrates real backend ownership, API design, file handling, AI workflow orchestration, and frontend–backend integration.

---

## 🚀 Features

- 📄 **Resume Parsing (PDF)**  
  Extracts and processes resume text using PyPDF2.

- 🎯 **Career-Aware Guidance**  
  Takes:
  - Target career role  
  - Experience level (student / fresher / early-career)  
  - Resume content  
  to generate tailored career advice.

- 🧠 **LangGraph-Based AI Workflow**  
  Structured, deterministic AI flow instead of prompt-only logic.

- 🔒 **API-Level Validation**  
  Ensures required inputs before entering the AI workflow.

- 🧾 **Clear Guidance Categorization**
  - Career Readiness
  - Skill Gap
  - Resume Improvement

- 🌐 **Webhook Integration**  
  Sends structured results to an external system (e.g., Relay.app, Zapier).

- 💻 **Modern Frontend**
  - React + Vite
  - Resume upload
  - Clean summary card UI
  - Status badges

---
## Environment section:

```ini
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

## 🏗️ Tech Stack

### Backend
- FastAPI  
- LangGraph  
- Python  
- PyPDF2  
- Pydantic  
- CORS Middleware  
- Webhook Integration  
- dotenv
- PostgreSQL
- SQLAlchemy
- psycopg2

### Frontend
- React (Vite)  
- Fetch API  
- Tailwind CSS  

---

## 🔁 System Flow

1. User provides:
   - Target career role
   - Experience level
   - Resume (PDF)

2. Frontend sends multipart form data to the backend.

3. Backend:
   - Performs API-level validation
   - Extracts resume text
   - Invokes the LangGraph workflow

4. AI workflow produces:
   - Career summary
   - Guidance category

5. Result is:
   - Saved to PostgreSQL (career history)
   - Displayed on the UI
   - Sent to webhook (if configured)

---

## 🧠 LangGraph Workflow (Backend)

**Input State**
- `resume_text`
- `career_goal`
- `experience_level`

**Processing**
- Resume-contextual reasoning
- Career-specific evaluation
- Experience-aware recommendations

**Output**
- `career_summary`
- `guidance_category`

This avoids uncontrolled LLM behavior and ensures predictable output.

---

## 🗄️ Database (PostgreSQL)

Every guidance result is persisted for history and traceability.

**Table: `career_history`**

| Column | Description |
|---|---|
| career_goal | Target role entered by the user |
| experience_level | student / fresher / early-career |
| guidance_category | Career Readiness / Skill Gap / Resume Improvement |
| score | Readiness score |
| gaps | Identified skill gaps |
| roadmap | Structured roadmap (JSON) |

- Connection via SQLAlchemy engine with `pool_pre_ping` for stale-connection safety
- Inserts use parameterized queries inside a transaction (`engine.begin()`), preventing SQL injection and guaranteeing commit or rollback
- Configured through the `DATABASE_URL` environment variable (app fails fast if it's missing)

---

## 🔐 API Endpoint

### `POST /chat`

**Form Data**
- `career_goal` (string)
- `experience_level` (student | fresher | early-career)
- `resume` (PDF)

**Response**
```json
{
  "reply": "You are largely career-ready...",
  "guidance_category": "career_readiness"
}
```

---

## 🌐 Webhook Support

Optional webhook integration via environment variable.

```ini
WEBHOOK_URL=https://your-webhook-url.com
```

## 🖥️ Frontend UI

- Resume upload component  
- Clean summary card  
- Badge-based guidance category  
- Loading and error handling  
