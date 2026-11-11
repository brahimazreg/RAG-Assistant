from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import ask_question


app = FastAPI(
    title="Assma RAG API",
    description="Question answering API using RAG",
    version="1.0.0",
)


class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {
        "message": "Assma RAG API is running"
    }


# @app.post("/ask")   -------- old version
# def ask(request: QuestionRequest):

#     answer = ask_question(request.question)

#     return {
#         "answer": answer
#     }

@app.post("/ask")
def ask(request: QuestionRequest):

    result = ask_question(request.question)

    return result