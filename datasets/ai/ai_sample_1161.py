import win32com.client

# word file to be converted
wordFile =  r'filename.docx'

# Open the word file
word = win32com.client.Dispatch("Word.Application")
doc = word.Documents.Open(wordFile)

# Set the pdf parameters
pdf_format_id = 17
file_name = r'filename.pdf'

# Save the file as pdf
doc.SaveAs(file_name, FileFormat=pdf_format_id)

# Close the word file
word.Quit()