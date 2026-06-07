from utils.gemini_helper import ask_gemini

def ats_analysis(
    resume_context,
    jd
):

    prompt = f"""
You are an ATS evaluator.

Resume:
{resume_context}

Job Description:
{jd}

Provide:

1. ATS Score (/100)
2. Missing Skills
3. Missing Keywords
4. Strengths
5. Improvements
"""

    return ask_gemini(prompt)