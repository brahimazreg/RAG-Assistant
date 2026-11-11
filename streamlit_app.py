
import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/ask"


# Page configuration
st.set_page_config(
    page_title="Assma RAG",
    page_icon="📚",
    layout="centered"
)


# Title
st.title("📚 Assma RAG")
st.write("Posez vos questions sur vos documents.")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input(
    "Posez votre question..."
)


# When user asks a question
if question:

    # Display user question
    with st.chat_message("user"):
        st.markdown(question)

    # Save user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })


    # Call API
    with st.chat_message("assistant"):

        with st.spinner("Recherche en cours..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question
                    }
                )


                if response.status_code == 200:

                    # data = response.json()   --- old version
                    # answer = data["answer"]
                    # st.markdown(answer)
                    
                    data = response.json()

                    answer = data["answer"]
                    sources = data["sources"]

                    st.markdown(answer)

                if sources:

                    st.markdown("### 📚 Sources")

                    for source in sources:

                        filename = source["source"]
                    page = source["page"]

                    if page is not None:
                        page = page + 1
                        st.write(f"- {filename} — page {page}")
                    else:
                        st.write(f"- {filename}")
                    # Save answer
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer
                    })


                else:

                    error_message = (
                        f"Erreur API : {response.status_code}"
                    )

                    st.error(error_message)


            except requests.exceptions.ConnectionError:

                st.error(
                    "Impossible de contacter l'API. "
                    "Vérifiez que FastAPI est démarré."
                )

