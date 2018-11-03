```ngMeta
name:  encrypting-pdfs
completionMethod: manual
```
# Encrypting PDFs
A PdfFileWriter object can also add encryption to a PDF document. Enter the following into the interactive shell:

```python
   >>> import PyPDF2
   >>> pdfFile = open('meetingminutes.pdf', 'rb')
   >>> pdfReader = PyPDF2.PdfFileReader(pdfFile)
   >>> pdfWriter = PyPDF2.PdfFileWriter()
   >>> for pageNum in range(pdfReader.numPages):
           pdfWriter.addPage(pdfReader.getPage(pageNum))

❶ >>> pdfWriter.encrypt('swordfish')
   >>> resultPdf = open('encryptedminutes.pdf', 'wb')
   >>> pdfWriter.write(resultPdf)
   >>> resultPdf.close()
```
Before calling the write() method to save to a file, call the encrypt() method and pass it a password string ❶. PDFs can have a user password (allowing you to view the PDF) and an owner password (allowing you to set permissions for printing, commenting, extracting text, and other features). The user password and owner password are the first and second arguments to encrypt(), respectively. If only one string argument is passed to encrypt(), it will be used for both passwords.

In this example, we copied the pages of meetingminutes.pdf to a PdfFileWriter object. We encrypted the PdfFileWriter with the password swordfish, opened a new PDF called encryptedminutes.pdf, and wrote the contents of the PdfFileWriter to the new PDF. Before anyone can view encryptedminutes.pdf, they’ll have to enter this password. You may want to delete the original, unencrypted meetingminutes.pdf file after ensuring its copy was correctly encrypted.