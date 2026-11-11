# 🤖  RAG Assistant

## 📌 Overview

Assma RAG Assistant is an AI-powered application based on **Retrieval-Augmented Generation (RAG)**. It allows users to ask questions and receive intelligent answers based on the content of their uploaded or stored files.

The application retrieves relevant information from local files and uses a Large Language Model (LLM) to generate contextual responses.

## 🎯 Main Features

- File-based knowledge retrieval.
- Document processing and text extraction.
- Intelligent question answering.
- Context-aware AI responses.
- Semantic search and information retrieval.
- Integration with Large Language Models (LLMs).

## ⚙️ How It Works

1. Load documents from local files.
2. Extract and process document content.
3. Split text into smaller chunks.
4. Generate embeddings.
5. Retrieve relevant information based on the user's question.
6. Send the retrieved context to the LLM.
7. Generate and display the final answer.

## 🧠 RAG Architecture

```text
       Local Documents
              |
              v
       Document Loading
              |
              v
       Text Extraction
              |
              v
        Text Splitting
              |
              v
      Embedding Generation
              |
              v
       Document Retrieval
              |
              v
        User Question
              |
              v
       Context + LLM
              |
              v
       AI Generated Answer
```

## 🛠️ Technologies

- Python
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Text Embeddings
- File-Based Document Processing

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/brahimazreg/RAG-Assistant.git
```

Navigate to the project:

```bash
cd RAG-Assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the application using its main Python entry point:

```bash
python app.py
```

Adjust the command if your application uses a different entry point.

## 📂 Project Structure

The project uses local files as its knowledge source rather than requiring an external database.

## 🔮 Future Improvements

- Support for additional document formats.
- Improved document retrieval.
- Better answer accuracy.
- Source references in generated answers.
- Conversation history.
- Improved user interface.

## 👩‍💻 Author

**AZREG BRAHIM**

GitHub: [brahimazreg](https://github.com/brahimazreg)

