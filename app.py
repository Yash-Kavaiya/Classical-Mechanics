import nbconvert
import sys

notebook_path = "Classical Mechanics.ipynb"
output_path = "Classical Mechanics.html"

# Convert notebook to PDF
pdf_exporter = nbconvert.PDFExporter()
pdf_data, resources = pdf_exporter.from_filename(notebook_path)

# Write to file
with open(output_path, "wb") as f:
    f.write(pdf_data)