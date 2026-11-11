
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from pydantic import BaseModel

from app.rag import initialize_rag, ask_question


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Initializing RAG application...")

    # Initialize only once when API starts
    retriever, llm = initialize_rag()

    app.state.retriever = retriever
    app.state.llm = llm

    print("RAG application ready!")

    yield

    print("Shutting down RAG application...")


app = FastAPI(
    title="Assma RAG API",
    description="Question answering API using RAG",
    version="1.0.0",
    lifespan=lifespan
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Assma RAG API is running"
    }


@app.post("/ask")
def ask(request: QuestionRequest, app_request: Request):

    retriever = app_request.app.state.retriever
    llm = app_request.app.state.llm

    result = ask_question(
        request.question,
        retriever,
        llm
    )

    return result
