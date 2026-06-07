from utils.gemini_helper import ask_gemini

def generate_questions(context):

    prompt = f"""
You are a Senior Technical Interviewer.

Resume:
{context}

Generate:

10 Easy Questions
10 Medium Questions
10 Advanced Questions
10 HR Questions

For each question provide:

- Question
- Ideal Answer
- Why Interviewer Asks
- Follow Up Question
"""

    return ask_gemini(prompt)