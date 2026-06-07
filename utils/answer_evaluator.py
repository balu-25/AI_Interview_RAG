from utils.gemini_helper import ask_gemini

def evaluate_answer(
    question,
    answer,
    context
):

    prompt = f"""
You are a Technical Interviewer.

Resume:
{context}

Question:
{question}

Candidate Answer:
{answer}

Evaluate:

1. Technical Accuracy /10
2. Communication /10
3. Confidence /10

Provide:

Score
Feedback
Correct Answer
"""

    return ask_gemini(prompt)