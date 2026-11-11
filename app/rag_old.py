import config

from app.llm import get_llm
from app.loader import load_documents
from app.splitter import split_into_chunk
from app.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store,
    vector_store_exists
)
from app.retriever import get_retriever



def get_or_create_vector_store(chunks):
    """
    Load the existing FAISS vector store if it exists.
    Otherwise create and save a new one.
    """

    if vector_store_exists():
        print("Vector store found. Loading...")
        vector_store = load_vector_store()

    else:
        print("Vector store not found.")
        print("Creating vector store...")

        vector_store = create_vector_store(chunks)

        save_vector_store(vector_store)

        print("Vector store created and saved.")

    return vector_store


def main():
    # 1. Load documents
    print("Loading documents...")
    documents = load_documents()

    # 2. Split documents into chunks
    print("Splitting documents...")
    chunks = split_into_chunk(documents)

    print(f"Total chunks: {len(chunks)}")

    # 3. Load or create vector store
    vector_store = get_or_create_vector_store(chunks)

    # 4. Create retriever
    retriever = get_retriever(vector_store)
    

    # 5. Ask user for a question
    question = input("\nYour question: ")

    # 6. Retrieve relevant documents
    docs = retriever.invoke(question)

    # 7. Build context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # 8. Build prompt
    prompt = config.PROMPT.format(
        context=context,
        question=question
    )

    # 9. Load LLM
    llm = get_llm()

    # 10. Generate answer
    response = llm.invoke(prompt)

    # 11. Display answer
    print("\nAnswer:")
    print("-" * 50)
    print(response.content)

    return response


if __name__ == "__main__":
    main()