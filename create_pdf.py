from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Company Product Catalog", ln=True)
pdf.cell(200, 10, txt="1. AI Chatbot - 500 euros/month", ln=True)
pdf.cell(200, 10, txt="2. Automation Tool - 300 euros/month", ln=True)
pdf.cell(200, 10, txt="3. Data Analysis Dashboard - 800 euros/month", ln=True)
pdf.cell(200, 10, txt="Contact: hello@company.com", ln=True)

pdf.output("sample.pdf")
print("PDF created!")