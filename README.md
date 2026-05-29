# AI Document Chatbot

An AI-powered chatbot that allows users to upload PDF documents and ask questions about their content using OpenAI's GPT model.

## Features
- Upload any PDF document
- Ask questions in natural language
- Chat history maintained during session
- Powered by OpenAI GPT-4o-mini

## Tech Stack
- Python
- Streamlit
- OpenAI API
- PyPDF

## How to Run
1. Clone the repository
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Add your OpenAI API key to `.env` file: `OPENAI_API_KEY=your_key_here`
6. Run: `streamlit run app.py`

## Demo
Upload a PDF and start asking questions about its content!