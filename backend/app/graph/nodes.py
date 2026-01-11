from .state import CareerState

# ---------- SIGNAL EXTRACTION ----------
def extract_signals(resume: str):
    resume = resume.lower()
    return {
        "has_projects": any(k in resume for k in ["project", "developed", "built"]),
        "has_backend": any(k in resume for k in ["fastapi", "django", "flask", "api"]),
        "has_frontend": any(k in resume for k in ["react", "frontend", "ui"]),
        "has_database": any(k in resume for k in ["sql", "postgres", "mysql"]),
        "has_deployment": any(k in resume for k in ["deploy", "docker", "aws"]),
        "has_dsa": any(k in resume for k in ["dsa", "algorithm"]),
    }


def identify_gaps(signals):
    gaps = []
    if not signals["has_projects"]:
        gaps.append("project_experience")
    if not (signals["has_backend"] or signals["has_frontend"]):
        gaps.append("core_development")
    if not signals["has_deployment"]:
        gaps.append("production_readiness")
    if not signals["has_dsa"]:
        gaps.append("problem_solving")
    return gaps


# ---------- START ----------
def start_node(state: CareerState):
    return state


# ---------- ROUTER ----------
def router_node(state: CareerState):
    signals = extract_signals(state["resume_text"])
    gaps = identify_gaps(signals)

    score = 0
    score += int(signals["has_projects"])
    score += int(signals["has_backend"] or signals["has_frontend"])
    score += int(signals["has_dsa"])
    score += int(signals["has_database"])
    score += int(signals["has_deployment"])  # optional strength

    state["signals"] = signals
    state["gaps"] = gaps
    state["score"] = score

    # ✅ Correct classification logic
    if not signals["has_projects"]:
        state["guidance_category"] = "follow_up"
    elif score <= 2:
        state["guidance_category"] = "resume_improvement"
    elif score <= 3:
        state["guidance_category"] = "skill_gap"
    else:
        state["guidance_category"] = "career_readiness"

    return state

# ---------- FOLLOW UP ----------
def follow_up_node(state: CareerState):
    state["follow_up_question"] = (
        "I couldn't detect clear projects in your resume. "
        "Have you done any academic, personal, or internship projects?"
    )
    state["final_reply"] = state["follow_up_question"]
    return state

# ---------- RESUME IMPROVEMENT ----------
def resume_improvement_node(state: CareerState):
    role = state["career_goal"]
    gaps = state["gaps"]

    roadmap = {
        "30_days": "Rewrite resume with clear project impact and metrics.",
        "60_days": f"Build 1 strong resume-worthy project aligned with {role}.",
        "90_days": "Refine resume, get reviews, and reapply strategically."
    }

    summary = (
        "Your resume needs improvement before aggressive applications. "
        f"Focus on strengthening: {', '.join(gaps)}."
    )

    state["roadmap"] = roadmap
    state["career_summary"] = summary
    state["final_reply"] = summary
    return state

# ---------- SKILL GAP ----------
def skill_gap_node(state: CareerState):
    role = state["career_goal"]
    gaps = state["gaps"]
    signals = state["signals"]

    roadmap = {
        "30_days": f"Strengthen core concepts and build 1 mini-project aligned with {role}.",
        "60_days": "Build an end-to-end project with backend and database integration.",
        "90_days": "Practice DSA consistently and start applying to relevant roles."
    }

    # 🔹 Suggest deployment only if missing
    if not signals.get("has_deployment"):
        roadmap["60_days"] = (
            "Deploy one project using Render / Railway "
            "and host frontend on Vercel."
        )

    # 🔹 Emphasize DSA if missing
    if not signals.get("has_dsa"):
        roadmap["90_days"] = (
            "Focus on data structures and algorithms and solve problems daily."
        )

    summary = (
        f"You are progressing toward a {role} role, but there are still gaps to address. "
        f"Focus on {', '.join(gaps)} to improve readiness."
    )

    state["roadmap"] = roadmap
    state["career_summary"] = summary
    state["final_reply"] = summary
    return state
# ---------- CAREER READY ----------
def career_readiness_node(state: CareerState):
    roadmap = {
        "30_days": "Polish resume and revise system design basics.",
        "60_days": "Apply aggressively and do mock interviews.",
        "90_days": "Negotiate offers and deepen specialization."
    }

    summary = "You are largely career-ready. Maintain momentum."

    state["roadmap"] = roadmap
    state["career_summary"] = summary
    state["final_reply"] = summary
    return state


# ---------- END ----------
def end_node(state: CareerState):
    return state
