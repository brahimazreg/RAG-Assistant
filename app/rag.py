import config
import os
import shutil
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

def rebuild_vector_store():

    print("Rebuilding vector store...")

    # 1. Load all PDFs
    documents = load_documents()

    print(f"Loaded {len(documents)} pages.")
    # Display detected PDF files
    detected_files = set()

    for doc in documents:
        source = doc.metadata.get("source", "Unknown")
        detected_files.add(os.path.basename(source))

    print("\nPDF FILES DETECTED:")

    for filename in sorted(detected_files):
        print(f"  - {filename}")


    # 2. Split documents
    chunks = split_into_chunk(documents)

    print(f"Generated {len(chunks)} chunks.")

    if not chunks:
        raise ValueError("No document chunks found.")

    # 3. Create a completely new vector store
    vector_store = create_vector_store(chunks)

    # 4. Save the new vector store
  

    if os.path.exists(config.VECTORE_STORE_PATH):
        shutil.rmtree(config.VECTORE_STORE_PATH)

    save_vector_store(vector_store)
        

    print("Vector store successfully rebuilt.")

    return vector_store

def initialize_rag():
    if vector_store_exists(config.VECTORE_STORE_PATH):
        print("Loading existing vector store...")
        vector_store = load_vector_store(config.VECTORE_STORE_PATH)
    else:
        print("No vector store found. Building a new one...")
        vector_store = rebuild_vector_store()

    retriever = get_retriever(vector_store)
    llm = get_llm()

    return retriever, llm

def ask_question(question, retriever, llm):

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Build context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # Build prompt
    prompt = config.PROMPT.format(
        context=context,
        question=question
    )

    # Generate answer
    response = llm.invoke(prompt)

    # Build sources
    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "Source inconnue")
        filename = os.path.basename(source)
        page = doc.metadata.get("page", None)

        sources.append({
            "source": filename,
            "page": page
        })

    return {
        "answer": response.content,
        "sources": sources
    }