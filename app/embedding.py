from langchain_ollama import OllamaEmbeddings


#BATCH_SIZE = 20


def get_embedding_model():
    return OllamaEmbeddings(
        model="nomic-embed-text"
    )


