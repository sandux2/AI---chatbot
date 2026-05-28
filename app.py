import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Document Chatbot")
st.write("Upload a PDF and ask questions about it!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text()
    
    st.success("PDF loaded successfully!")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    question = st.chat_input("Ask a question about the document:")

    if question:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        # Build messages for GPT including history
        gpt_messages = [
            {"role": "system", "content": f"You are a helpful assistant. Answer questions based on this document:\n{pdf_text}"}
        ]
        gpt_messages += st.session_state.messages

        # Get GPT response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=gpt_messages
        )

        answer = response.choices[0].message.content

        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)