import tempfile
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(uploaded_file):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())

        pdf_path = tmp.name

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    return docs