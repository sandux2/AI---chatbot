import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Document Chatbot")
st.write("Upload a PDF and ask questions about it!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text()
    
    st.success("PDF loaded successfully!")
    
    question = st.text_input("Ask a question about the document:")
    
    if question:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions strictly based on the provided document. Only use information from the document to answer."},
                {"role": "user", "content": f"Document content:\n{pdf_text}\n\nQuestion: {question}"}
            ]
        )
        
        st.write("**Answer:**")
        st.write(response.choices[0].message.content)