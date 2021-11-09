encrypting-pdfs_key1
encrypting-pdfs_key2


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
encrypting-pdfs_key3


encrypting-pdfs_key4
