```ngMeta
name: creating-pdfs
completionMethod: manual
```
# Creating PDFs
PyPDF2’s counterpart to PdfFileReader objects is PdfFileWriter objects, which can create new PDF files. But PyPDF2 cannot write arbitrary text to a PDF like Python can do with plaintext files. Instead, PyPDF2’s PDF-writing capabilities are limited to copying pages from other PDFs, rotating pages, overlaying pages, and encrypting files.

PyPDF2 doesn’t allow you to directly edit a PDF. Instead, you have to create a new PDF and then copy content over from an existing document. The examples in this section will follow this general approach:

Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.

Create a new PdfFileWriter object.

Copy pages from the PdfFileReader objects into the PdfFileWriter object.

Finally, use the PdfFileWriter object to write the output PDF.

Creating a PdfFileWriter object creates only a value that represents a PDF document in Python. It doesn’t create the actual PDF file. For that, you must call the PdfFileWriter’s write() method.

The write() method takes a regular File object that has been opened in write-binary mode. You can get such a File object by calling Python’s open() function with two arguments: the string of what you want the PDF’s filename to be and 'wb' to indicate the file should be opened in write-binary mode.

If this sounds a little confusing, don’t worry—you’ll see how this works in the following code examples.

# Copying Pages
You can use PyPDF2 to copy pages from one PDF document to another. This allows you to combine multiple PDF files, cut unwanted pages, or reorder pages.

Download meetingminutes.pdf and meetingminutes2.pdf from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> and place the PDFs in the current working directory. Enter the following into the interactive shell:

```python
   >>> import PyPDF2
   >>> pdf1File = open('meetingminutes.pdf', 'rb')
   >>> pdf2File = open('meetingminutes2.pdf', 'rb')
❶ >>> pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
❷ >>> pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
❸ >>> pdfWriter = PyPDF2.PdfFileWriter()

   >>> for pageNum in range(pdf1Reader.numPages):
❹         pageObj = pdf1Reader.getPage(pageNum)
❺         pdfWriter.addPage(pageObj)

   >>> for pageNum in range(pdf2Reader.numPages):
❻         pageObj = pdf2Reader.getPage(pageNum)
❼         pdfWriter.addPage(pageObj)

❽ >>> pdfOutputFile = open('combinedminutes.pdf', 'wb')
   >>> pdfWriter.write(pdfOutputFile)
   >>> pdfOutputFile.close()
   >>> pdf1File.close()
   >>> pdf2File.close()
```
Open both PDF files in read binary mode and store the two resulting File objects in pdf1File and pdf2File. Call PyPDF2.PdfFileReader() and pass it pdf1File to get a PdfFileReader object for meetingminutes.pdf ❶. Call it again and pass it pdf2File to get a PdfFileReader object for meetingminutes2.pdf ❷. Then create a new PdfFileWriter object, which represents a blank PDF document ❸.

Next, copy all the pages from the two source PDFs and add them to the PdfFileWriter object. Get the Page object by calling getPage() on a PdfFileReader object ❹. Then pass that Page object to your PdfFileWriter’s addPage() method ❺. These steps are done first for pdf1Reader and then again for pdf2Reader. When you’re done copying pages, write a new PDF called combinedminutes.pdf by passing a File object to the PdfFileWriter’s write() method ❻.

# Note
PyPDF2 cannot insert pages in the middle of a PdfFileWriter object; the addPage() method will only add pages to the end.

You have now created a new PDF file that combines the pages from meetingminutes.pdf and meetingminutes2.pdf into a single document. Remember that the File object passed to PyPDF2.PdfFileReader() needs to be opened in read-binary mode by passing 'rb' as the second argument to open(). Likewise, the File object passed to PyPDF2.PdfFileWriter() needs to be opened in write-binary mode with 'wb'.

# Rotating Pages
The pages of a PDF can also be rotated in 90-degree increments with the rotateClockwise() and rotateCounterClockwise() methods. Pass one of the integers 90, 180, or 270 to these methods. Enter the following into the interactive shell, with the meetingminutes.pdf file in the current working directory:

```python
   >>> import PyPDF2
   >>> minutesFile = open('meetingminutes.pdf', 'rb')
   >>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
❶ >>> page = pdfReader.getPage(0)
❷ >>> page.rotateClockwise(90)
   {'/Contents': [IndirectObject(961, 0), IndirectObject(962, 0),
   --snip--
   }
   >>> pdfWriter = PyPDF2.PdfFileWriter()
   >>> pdfWriter.addPage(page)
❸ >>> resultPdfFile = open('rotatedPage.pdf', 'wb')
   >>> pdfWriter.write(resultPdfFile)
   >>> resultPdfFile.close()
   >>> minutesFile.close()
```
Here we use getPage(0) to select the first page of the PDF ❶, and then we call rotateClockwise(90) on that page ❷. We write a new PDF with the rotated page and save it as rotatedPage.pdf ❸.

The resulting PDF will have one page, rotated 90 degrees clockwise, as in Figure 13-2. The return values from rotateClockwise() and rotateCounterClockwise() contain a lot of information that you can ignore.

<!-- ![image](assets/000104.jpg)
 -->
Figure 13-2. The rotatedPage.pdf file with the page rotated 90 degrees clockwise
