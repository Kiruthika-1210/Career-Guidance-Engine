from typing import TypedDict, Optional, Dict, List

class CareerState(TypedDict):
    resume_text: Optional[str]
    career_goal: Optional[str]
    experience_level: Optional[str]

    guidance_category: Optional[str]
    score: Optional[int]
    gaps: Optional[List[str]]

    career_summary: Optional[str]
    roadmap: Optional[Dict[str, str]]

    follow_up_question: Optional[str]
    final_reply: Optional[str]

    signals: Optional[Dict[str, bool]]
