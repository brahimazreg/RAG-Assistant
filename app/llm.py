import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import config

load_dotenv()


def get_llm():
    return ChatGroq(
        model=config.LLM_MODEL_NAME,
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY"),
    )