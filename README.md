Question
   ↓
Streamlit
   ↓
FastAPI
   ↓
Retriever
   ↓
FAISS
   ↓
LLM
   ↓
Réponse + source
   ↓
Streamlit

rag.py

initialize_rag()
      ↓
load documents
      ↓
split documents
      ↓
load/create FAISS
      ↓
create retriever
      ↓
load LLM
      ↓
return retriever + LLM