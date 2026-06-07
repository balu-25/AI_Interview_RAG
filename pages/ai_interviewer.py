import streamlit as st

from utils.pdf_loader import load_pdf
from utils.gemini_helper import ask_gemini
from utils.answer_evaluator import evaluate_answer

st.title("🎤 AI Interviewer")

# Session Variables

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current" not in st.session_state:
    st.session_state.current = 0

if "results" not in st.session_state:
    st.session_state.results = []

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""


# Upload Resume

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


# Generate Questions

if resume and len(st.session_state.questions) == 0:

    docs = load_pdf(resume)

    resume_text = "\n".join(
        [doc.page_content for doc in docs]
    )

    st.session_state.resume_text = resume_text

    prompt = f"""
You are a Senior Technical Interviewer.

Resume:
{resume_text}

Generate exactly 20 interview questions.

Distribution:

5 Skill Based Questions
5 Project Based Questions
5 Technical Questions
5 HR Questions

Return ONLY questions.
One question per line.
"""

    response = ask_gemini(prompt)

    questions = [
        q.strip()
        for q in response.split("\n")
        if q.strip()
    ]

    st.session_state.questions = questions[:20]

    st.success("Interview Questions Generated")


# Interview Starts

if len(st.session_state.questions) > 0:

    current = st.session_state.current

    if current < len(st.session_state.questions):

        question = st.session_state.questions[current]

        st.subheader(
            f"Question {current + 1}/20"
        )

        st.info(question)

        answer = st.text_area(
            "Your Answer"
        )

        if st.button("Submit Answer"):

            feedback = evaluate_answer(
                question,
                answer,
                st.session_state.resume_text
            )

            st.session_state.results.append(
                {
                    "question": question,
                    "answer": answer,
                    "feedback": feedback
                }
            )

            st.write(feedback)

            st.session_state.current += 1

            st.rerun()

    else:

        st.success(
            "Interview Completed!"
        )

        st.header("Final Report")

        for i, item in enumerate(
            st.session_state.results
        ):

            with st.expander(
                f"Question {i+1}"
            ):

                st.write(
                    "**Question:**",
                    item["question"]
                )

                st.write(
                    "**Answer:**",
                    item["answer"]
                )

                st.write(
                    "**Evaluation:**"
                )

                st.write(
                    item["feedback"]
                )