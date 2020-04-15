# Pdfs have to be read in binary mode
import PyPDF2

# Open a pdf file 
pdf_file = open('meetingminutes.pdf', 'rb')

# Read a pdf file
reader = PyPDF2.PdfFileReader(pdf_file)

# Number of pages
print(reader.numPages)

# Read a page of the pdf
page = reader.getPage(0)
print(page.extractText())

# Read all the pages in the pdf
for page_num in range(reader.numPages):
    page = reader.getPage(page_num)
    print(page.extractText())

# Combine two pdf documents
pdf1_file = open('meetingminutes.pdf', 'rb')
pdf2_file = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1_file)
reader2 = PyPDF2.PdfFileReader(pdf2_file)

writer = PyPDF2.PdfFileWriter()

for page_num in range(reader1.numPages):
    page = reader1.getPage(page_num)
    writer.addPage(page)

for page_num in range(reader2.numPages):
    page = reader2.getPage(page_num)
    writer.addPage(page)

combined_pdf = open('combinedminutes.pdf', 'wb')
writer.write(combined_pdf)
combined_pdf.close()
pdf1_file.close()
pdf2_file.close()