from langchain_community.vectorstores import FAISS

def create_vector_store(
    docs,
    embedding_model
):

    db = FAISS.from_documents(
        docs,
        embedding_model
    )

    return db