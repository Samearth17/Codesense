import PyPDF2

# open the PDF file
pdf_file = open('sample.pdf', 'rb')

# create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# get the number of pages
num_pages = pdf_reader.numPages

# iterate over all pages
for page_num in range(num_pages):
    # get the page
    page = pdf_reader.getPage(page_num)
    # extract text
    text = page.extractText()
    print(text)