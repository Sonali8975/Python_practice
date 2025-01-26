import fitz  # PyMuPDF

# Open the PDF
pdf_path = r"C:\Users\sosangle\OneDrive - Capgemini\Desktop\CERTIFICATES\what is data science certificate.pdf"
doc = fitz.open(pdf_path)

# Loop through each page and convert it to an image
for page_num in range(doc.page_count):
    page = doc.load_page(page_num)  # Get the page
    pix = page.get_pixmap()  # Convert the page to a pixmap (image)

    # Save the pixmap as an image file (e.g., PNG)
    pix.save(f'page_{page_num + 1}.png')  # You can save as PNG, JPEG, etc.
