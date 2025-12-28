import fitz  # PyMuPDF
import sys
import os
from pathlib import Path

def extract_pdf(pdf_path, output_file=None, encoding='utf-8'):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        output_file: Optional output file path. If None, prints to stdout
        encoding: Text encoding (default: utf-8)
    """
    # Check if file exists
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        return False
    
    try:
        # Open PDF
        doc = fitz.open(pdf_path)
        
        total_pages = len(doc)
        print(f"Total pages: {total_pages}\n")
        
        # Extract text from all pages
        full_text = f"PDF: {Path(pdf_path).name}\nTotal pages: {total_pages}\n\n"
        
        for page_num in range(total_pages):
            page = doc[page_num]
            text = page.get_text()
            full_text += f"\n{'='*60}\n"
            full_text += f"Page {page_num + 1}\n"
            full_text += f"{'='*60}\n\n"
            full_text += text
            full_text += "\n"
            
            # Progress indicator
            if (page_num + 1) % 10 == 0:
                print(f"Processed {page_num + 1}/{total_pages} pages...")
        
        doc.close()
        
        # Output to file or stdout
        if output_file:
            with open(output_file, 'w', encoding=encoding) as f:
                f.write(full_text)
            print(f"\nExtraction complete! Output saved to: {output_file}")
        else:
            sys.stdout.reconfigure(encoding=encoding)
            print(full_text)
        
        return True
        
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return False

def main():
    """Main function to handle command line arguments."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Extract text from PDF files using PyMuPDF',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract to stdout
  python extract_pdf_full.py document.pdf
  
  # Extract to file
  python extract_pdf_full.py document.pdf -o output.txt
  
  # Specify encoding (for Japanese text on Windows)
  python extract_pdf_full.py document.pdf -o output.txt -e cp932
        """
    )
    
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    parser.add_argument('-e', '--encoding', default='utf-8', 
                       help='Text encoding (default: utf-8)')
    
    args = parser.parse_args()
    
    # Extract PDF
    success = extract_pdf(args.pdf_path, args.output, args.encoding)
    
    if not success:
        sys.exit(1)

if __name__ == '__main__':
    main()
