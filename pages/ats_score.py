import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_docs
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store
from utils.ats_analyzer import ats_analysis

st.title("ATS Resume Score Analyzer")

resume = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

jd = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze ATS"):

    docs = load_pdf(resume)

    chunks = split_docs(docs)

    db = create_vector_store(
        chunks,
        get_embedding_model()
    )

    retrieved = db.similarity_search(
        jd,
        k=5
    )

    context = "\n".join(
        [doc.page_content for doc in retrieved]
    )

    result = ats_analysis(
        context,
        jd
    )

    st.write(result)