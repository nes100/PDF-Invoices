from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
				df = pd.read_excel(filepath, sheet_name="Sheet 1")
				print(df)
				pdf = FPDF(orientation="P", unit="mm", format="A4")
				pdf.set_font(family="Times", style="B", size=16)
				pdf.add_page()
				filename = Path(filepath).stem
				invoice_nr = filename.split("-")[0]
				pdf.cell(w=50,h=8, txt=f"Invoice nr.{invoice_nr}", align="L", ln=1)
				pdf.output(f"PDFs/{filename}.pdf")
