from .state import CareerState

# ---------- SIGNAL EXTRACTION ----------
def extract_signals(resume: str):
    resume = resume.lower()

    return {
        "has_projects": any(k in resume for k in [
            "project", "projects", "experience", "worked on", "developed", "built", 
            "model", "training", "dataset"
            ]),
        "has_backend": any(k in resume for k in ["api", "backend", "fastapi", "django", "flask"]),
        "has_frontend": any(k in resume for k in ["react", "frontend", "ui"]),
        "has_database": any(k in resume for k in ["sql", "mysql", "postgres", "mongodb"]),
        "has_deployment": any(k in resume for k in ["deploy", "docker", "aws", "cloud"]),
        "has_dsa": any(k in resume for k in ["data structures", "algorithm", "dsa"]),
    }


def identify_gaps(signals):
    gaps = []

    if not signals["has_projects"]:
        gaps.append("project_experience")

    if not (signals["has_backend"] or signals["has_frontend"]):
        gaps.append("core_development_skills")

    if signals["has_projects"] and not signals["has_deployment"]:
        gaps.append("production_readiness")
        
    if not signals["has_dsa"] and not signals["has_deployment"]:
        gaps.append("problem_solving")

    return gaps


# ---------- START NODE ----------
def start_node(state: CareerState):
    return state

# ---------- ROUTER NODE ----------
def router_node(state: CareerState):
    resume = state["resume_text"].lower()
    state["signals"] = extract_signals(resume)

    score = 0
    s = state["signals"]

    if s["has_projects"]:
        score += 1
    if s["has_dsa"]:
        score += 1
    if s["has_backend"] or s["has_frontend"]:
        score += 1
    if s["has_deployment"]:
        score += 2

    if score == 0:
        state["guidance_category"] = "resume_improvement"
    elif score <= 3:
        state["guidance_category"] = "skill_gap"
    else:
        state["guidance_category"] = "career_readiness"

    return state


# ---------- GUIDANCE NODES ----------
def resume_improvement_node(state: CareerState):
    summary = (
        "Your resume lacks clear project descriptions and structure. "
        "Improve bullet clarity, add measurable impact, and organize sections properly."
    )
    state["career_summary"] = summary
    state["final_reply"] = summary
    return state


GAP_TEMPLATES = {
    "project_experience":
        "Your profile would benefit from stronger end-to-end project experience.",

    "core_development_skills":
        "Strengthening core development skills aligned with your target role is recommended.",

    "production_readiness":
        "Adding deployment or production-level exposure will improve real-world readiness.",

    "problem_solving":
        "Improving data structures and algorithmic problem-solving will strengthen fundamentals.",
}

def skill_gap_node(state: CareerState):
    gaps = identify_gaps(state["signals"])
    role = state["career_goal"]

    parts = [
        f"You have a solid foundation, but there are key areas to strengthen for a {role} role."
    ]

    for gap in gaps:
        parts.append(GAP_TEMPLATES[gap])

    parts.append(
        "Addressing these gaps with focused learning and projects will significantly improve readiness."
    )

    summary = " ".join(parts)

    state["career_summary"] = summary
    state["final_reply"] = summary
    return state


def career_readiness_node(state: CareerState):
    summary = (
        "You are largely career-ready. Strengthen system design, polish your resume, "
        "and continue applying consistently."
    )

    state["career_summary"] = summary
    state["final_reply"] = summary
    return state


# ---------- END NODE ----------
def end_node(state: CareerState):
    # Ensure final_reply is always preserved
    state["final_reply"] = state.get("final_reply")
    return state

