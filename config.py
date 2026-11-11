import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

# LLM model

LLM_MODEL_NAME="openai/gpt-oss-120b"

# Embeddings
#EMBEDDING_MODEL_NAME="gemini-embedding-001"
#EMBEDDING_MODEL_NAME="jina-embeddings-v5-text-small"
#EMBEDDING_MODEL_NAME = "jinaai/jina-embeddings-v5-text-small"

# path vector store
VECTORE_STORE_PATH=os.path.join("data","faiss_index")

# path data file
PATH_DATA_FILE=os.path.join("data")

# Top result
TOP_K_RESULT=3

# chunks
CHUNK_SIZE=500
CHUNK_OVERLAP=50

PROMPT = """
    Tu es un assistant spécialisé dans la réponse aux questions
    à partir des documents fournis.

    Utilise uniquement les informations présentes dans le contexte.
    Si la réponse n'est pas présente dans le contexte, indique que
    tu ne trouves pas la réponse dans les documents.

    Contexte:
    {context}

    Question:
    {question}

    Réponse:
"""

# Check if GIMINI_API_KEY is missing
def check_api_key():
    """ stop early with a clear message if required key is missing"""
    if not GEMINI_API_KEY:
        raise ValueError("Missing GIMINI_API_KEY  please added it to your .env file")
