# Import the PdfReader class from the pypdf library
from pypdf import PdfReader

# Define the path to the PDF file
pdf_path = "data/ai_text_detection.pdf"

# Create a PdfReader object to access the PDF file
reader = PdfReader(pdf_path)

# Initialize an empty string to store the extracted text
text = ""

# Loop through page in the PDF
for page in reader.pages:
    # Extract the text from the current page
    page_text = page.extract_text()
    # Check if text was succcessfully extracted
    if page_text:
        # Append the extracted text to the overall text variable
        text += page_text + "\n"  # Add a newline after each page's text

print(f"Pages: {len(reader.pages)}") # Print the number of pages in the PDF
print(f"Characters extracted: {len(text)}") # Print the number of characters extracted from the PDF
print("\n---Preview ---\n") # Print a preview header
print(text[:2000]) # Print the first 2000 characters of the extracted text as a preview

with open("output.txt", "w", encoding="utf-8") as f: # Open a new file named "output.txt" in write mode with UTF-8 encoding
    f.write(text) # Write the extracted text to an output file named "output.txt"
    
print("\nFull extracted text has been saved to output.txt") # Print a message indicating that the full extracted text has been saved to the output file
