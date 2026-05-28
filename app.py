from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

reader = PdfReader("sample.pdf")
pdf_text = ""
for page in reader.pages:
    pdf_text += page.extract_text()

print("PDF loaded! Content:")
print(pdf_text)
print("---")


question = "What products does the company offer and what are the prices?"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"You are a helpful assistant. Use this document to answer questions: {pdf_text}"},
        {"role": "user", "content": question}
    ]
)

print("GPT Response:")
print(response.choices[0].message.content)