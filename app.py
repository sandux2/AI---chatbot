import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page config
st.set_page_config(
    page_title="AI Document Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Document Chatbot")
st.write("Upload a PDF and ask questions about it!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for PDF upload
with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        st.success("PDF loaded successfully!")
        
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main chat area
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text()

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    question = st.chat_input("Ask a question about the document...")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Thinking..."):
            gpt_messages = [
                {"role": "system", "content": f"You are a helpful assistant. Answer questions based on this document:\n{pdf_text}"}
            ]
            gpt_messages += st.session_state.messages

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=gpt_messages
            )

            answer = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)

else:
    st.info("Please upload a PDF document from the sidebar to get started!")