from langchain_ollama import OllamaEmbeddings


#BATCH_SIZE = 20


def get_embedding_model():
    return OllamaEmbeddings(
        model="nomic-embed-text"
    )


# def embed_document(chunks):
#     """Generate embeddings for document chunks in batches."""

#     embedding_model = get_embedding_model()

#     vectors = []
#     total = len(chunks)

#     for start in range(0, total, BATCH_SIZE):

#         end = min(start + BATCH_SIZE, total)

#         batch = chunks[start:end]

#         texts = [
#             chunk.page_content
#             for chunk in batch
#         ]

#         print(
#             f"Embedding {start + 1} → {end} / {total}"
#         )

#         batch_vectors = embedding_model.embed_documents(texts)

#         vectors.extend(batch_vectors)

#     return vectors