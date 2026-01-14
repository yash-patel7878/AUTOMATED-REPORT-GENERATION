from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import pandas as pd

def analyze_data(file_path):
    # Read CSV data
    df = pd.read_csv(file_path)

    # Basic analysis
    summary = df.describe(include='all')
    return df, summary

def export_pdf(df, summary, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "Automated Data Analysis Report")

    # Section: Dataset Overview
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 100, "Dataset Preview:")

    c.setFont("Helvetica", 10)

    y = height - 120
    for column in df.columns:
        c.drawString(60, y, f"- {column}: {df[column].iloc[0]}")
        y -= 15

    # Section: Summary Statistics
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 20, "Statistical Summary:")

    y -= 50
    for col in summary.columns:
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, f"{col}")
        y -= 15

        c.setFont("Helvetica", 10)
        for metric, value in summary[col].items():
            c.drawString(70, y, f"{metric}: {value}")
            y -= 15
        
        y -= 10

        if y < 100:  # Add new page if space ends
            c.showPage()
            y = height - 50

    c.save()
    print(f"PDF Report Generated: {output_pdf}")

# MAIN
if __name__ == "__main__":
    data_file = "sample_data.csv"     # Input file
    output_pdf = "report_output.pdf"  # Output file

    df, summary = analyze_data(data_file)
    export_pdf(df, summary, output_pdf)
