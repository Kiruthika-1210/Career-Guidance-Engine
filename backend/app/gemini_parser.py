import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract_signals_with_gemini(resume_text: str):
    prompt = f"""
You are an expert resume analyzer.

Read the resume and determine whether the candidate possesses the following.

Return ONLY valid JSON.

{{
    "has_projects": true/false,
    "has_backend": true/false,
    "has_frontend": true/false,
    "has_database": true/false,
    "has_deployment": true/false,
    "has_dsa": true/false
}}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
