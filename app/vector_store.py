from langchain_community.vectorstores import FAISS
from app.embedding import get_embedding_model
import config
import os


BATCH_SIZE = 20


def create_vector_store(chunks):
    """
    Create a FAISS vector store by embedding documents in batches.
    """

    embedding_model = get_embedding_model()

    vector_store = None
    total = len(chunks)

    for start in range(0, total, BATCH_SIZE):

        end = min(start + BATCH_SIZE, total)

        batch = chunks[start:end]

        print(f"Embedding {start + 1} → {end} / {total}")

        # Create FAISS index for this batch
        batch_vector_store = FAISS.from_documents(
            batch,
            embedding_model
        )

        # First batch becomes the main vector store
        if vector_store is None:
            vector_store = batch_vector_store

        # Add subsequent batches to the main vector store
        else:
            vector_store.merge_from(batch_vector_store)

    return vector_store


def save_vector_store(
    vector_store,
    path: str = config.VECTORE_STORE_PATH
):
    """Save the vector store."""

    os.makedirs(path, exist_ok=True)

    vector_store.save_local(path)

    return "Vector store saved successfully!"


def load_vector_store(
    path: str = config.VECTORE_STORE_PATH
):
    """Load a saved vector store."""

    embedding_model = get_embedding_model()

    return FAISS.load_local(
        path,
        embedding_model,
        allow_dangerous_deserialization=True
    )


def vector_store_exists(
    path: str = config.VECTORE_STORE_PATH
):
    return os.path.exists(
        os.path.join(path, "index.faiss")
    )