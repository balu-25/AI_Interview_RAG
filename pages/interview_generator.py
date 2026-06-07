import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_docs
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store
from utils.interview_questions import generate_questions

st.title("Interview Question Generator")

resume = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

if st.button("Generate Questions"):

    docs = load_pdf(resume)

    chunks = split_docs(docs)

    db = create_vector_store(
        chunks,
        get_embedding_model()
    )

    retrieved = db.similarity_search(
        "Interview Questions",
        k=5
    )

    context = "\n".join(
        [doc.page_content for doc in retrieved]
    )

    result = generate_questions(
        context
    )

    st.write(result)