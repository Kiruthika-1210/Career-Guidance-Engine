from typing import TypedDict, Optional, Dict

class CareerState(TypedDict):
    resume_text: Optional[str]
    career_goal: Optional[str]
    experience_level: Optional[str]
    guidance_category: Optional[str]
    career_summary: Optional[str]
    final_reply: Optional[str]   # ✅ single authoritative output
    signals: Optional[Dict[str, bool]]
