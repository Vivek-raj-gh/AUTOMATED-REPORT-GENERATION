import pandas as pd
from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Data Analysis Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(5)

    def chapter_content(self, content):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, content)
        self.ln(5)

if __name__ == "__main__":
    try:
        data = pd.read_csv("data.csv")
    except FileNotFoundError:
        print("The file 'data.csv' was not found.")
        exit()

    report_content = "Data Summary:\n" + str(data.describe())

    pdf = PDFReport()
    pdf.add_page()

    pdf.chapter_title("Data Summary")
    pdf.chapter_content(report_content)

    pdf.output("Data_Analysis_Report.pdf")
    print("PDF report generated successfully as 'Data_Analysis_Report.pdf'")
