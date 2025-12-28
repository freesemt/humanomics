import fitz  # PyMuPDF
import sys
import os
from pathlib import Path

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

# Get PDF path from command line argument or use default in current directory
if len(sys.argv) > 1:
    pdf_path = sys.argv[1]
else:
    pdf_path = "SmithA_MoralSentiments.pdf"

# Check if file exists
if not os.path.exists(pdf_path):
    print(f"Error: PDF file not found: {pdf_path}")
    print(f"\nUsage: python {Path(__file__).name} [pdf_path]")
    print(f"Example: python {Path(__file__).name} SmithA_MoralSentiments.pdf")
    sys.exit(1)

# Open PDF
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}\n")

# Extract text from first 10 pages to get an overview
print("=== First 10 pages overview ===\n")
for page_num in range(min(10, len(doc))):
    page = doc[page_num]
    text = page.get_text()
    print(f"\n--- Page {page_num + 1} ---\n{text}\n")

doc.close()
