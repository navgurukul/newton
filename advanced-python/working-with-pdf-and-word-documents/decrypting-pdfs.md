```ngMeta
name: decrypting-pdfs
completionMethod: manual
```
# Decrypting PDFs
Some PDF documents have an encryption feature that will keep them from being read until whoever is opening the document provides a password. Enter the following into the interactive shell with the PDF you downloaded, which has been encrypted with the password rosebud:

```python
   >>> import PyPDF2
   >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
❶ >>> pdfReader.isEncrypted
```
   True
```python
   >>> pdfReader.getPage(0)
```
❷ Traceback (most recent call last):
     File "<pyshell#173>", line 1, in <module>
       pdfReader.getPage()
     --snip--
     File "C:\Python34\lib\site-packages\PyPDF2\pdf.py", line 1173, in getObject
       raise utils.PdfReadError("file has not been decrypted")
   PyPDF2.utils.PdfReadError: file has not been decrypted
```python
❸ >>> pdfReader.decrypt('rosebud')
```
   1
```python
   >>> pageObj = pdfReader.getPage(0)
```
All PdfFileReader objects have an isEncrypted attribute that is True if the PDF is encrypted and False if it isn’t ❶. Any attempt to call a function that reads the file before it has been decrypted with the correct password will result in an error ❷.

To read an encrypted PDF, call the decrypt() function and pass the password as a string ❸. After you call decrypt() with the correct password, you’ll see that calling getPage() no longer causes an error. If given the wrong password, the decrypt() function will return 0 and getPage() will continue to fail. Note that the decrypt() method decrypts only the PdfFileReader object, not the actual PDF file. After your program terminates, the file on your hard drive remains encrypted. Your program will have to call decrypt() again the next time it is run.

