```ngMeta
name: project:combining-select-pages-from-many-pdfs
```
# Project: Combining Select Pages from Many PDFs
Say you have the boring job of merging several dozen PDF documents into a single PDF file. Each of them has a cover sheet as the first page, but you don’t want the cover sheet repeated in the final result. Even though there are lots of free programs for combining PDFs, many of them simply merge entire files together. Let’s write a Python program to customize which pages you want in the combined PDF.

At a high level, here’s what the program will do:

Find all PDF files in the current working directory.

Sort the filenames so the PDFs are added in order.

Write each page, excluding the first page, of each PDF to the output file.

In terms of implementation, your code will need to do the following:

Call os.listdir() to find all the files in the working directory and remove any non-PDF files.

Call Python’s sort() list method to alphabetize the filenames.

Create a PdfFileWriter object for the output PDF.

Loop over each PDF file, creating a PdfFileReader object for it.

Loop over each page (except the first) in each PDF file.

Add the pages to the output PDF.

Write the output PDF to a file named allminutes.pdf.

For this project, open a new file editor window and save it as combinePdfs.py.

# Step 1: Find All PDF Files
First, your program needs to get a list of all files with the .pdf extension in the current working directory and sort them. Make your code look like the following:


   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # into a single PDF.

❶ import PyPDF2, os

   # Get all the PDF filenames.
   pdfFiles = []
   for filename in os.listdir('.'):
       if filename.endswith('.pdf'):
❷         pdfFiles.append(filename)
❸ pdfFiles.sort(key=str.lower)

❹ pdfWriter = PyPDF2.PdfFileWriter()

   # TODO: Loop through all the PDF files.

   # TODO: Loop through all the pages (except the first) and add them.

   # TODO: Save the resulting PDF to a file.
After the shebang line and the descriptive comment about what the program does, this code imports the os and PyPDF2 modules ❶. The os.listdir('.') call will return a list of every file in the current working directory. The code loops over this list and adds only those files with the .pdf extension to pdfFiles ❷. Afterward, this list is sorted in alphabetical order with the key=str.lower keyword argument to sort() ❸.

A PdfFileWriter object is created to hold the combined PDF pages ❹. Finally, a few comments outline the rest of the program.

# Step 2: Open Each PDF
Now the program must read each PDF file in pdfFiles. Add the following to your program:


  #! python3
  # combinePdfs.py - Combines all the PDFs in the current working directory into
  # a single PDF.

import PyPDF2, os

  # Get all the PDF filenames.
pdfFiles = []
--snip--
```python
  # Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
```
    # TODO: Loop through all the pages (except the first) and add them.

  # TODO: Save the resulting PDF to a file.
For each PDF, the loop opens a filename in read-binary mode by calling open() with 'rb' as the second argument. The open() call returns a File object, which gets passed to PyPDF2.PdfFileReader() to create a PdfFileReader object for that PDF file.

# Step 3: Add Each Page
For each PDF, you’ll want to loop over every page except the first. Add this code to your program:


   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # a single PDF.

   import PyPDF2, os

   --snip--

   # Loop through all the PDF files.
   for filename in pdfFiles:
   --snip--
```python
       # Loop through all the pages (except the first) and add them.
❶     for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)
```
   # TODO: Save the resulting PDF to a file.
The code inside the for loop copies each Page object individually to the PdfFileWriter object. Remember, you want to skip the first page. Since PyPDF2 considers 0 to be the first page, your loop should start at 1 ❶ and then go up to, but not include, the integer in pdfReader.numPages.

# Step 4: Save the Results
After these nested for loops are done looping, the pdfWriter variable will contain a PdfFileWriter object with the pages for all the PDFs combined. The last step is to write this content to a file on the hard drive. Add this code to your program:


#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# a single PDF.
import PyPDF2, os

--snip--

# Loop through all the PDF files.
for filename in pdfFiles:
--snip--
    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
    --snip--
```python
#Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
```
Passing 'wb' to open() opens the output PDF file, allminutes.pdf, in write-binary mode. Then, passing the resulting File object to the write() method creates the actual PDF file. A call to the close() method finishes the program.

# Ideas for Similar Programs
Being able to create PDFs from the pages of other PDFs will let you make programs that can do the following:

Cut out specific pages from PDFs.

Reorder pages in a PDF.

Create a PDF from only those pages that have some specific text, identified by extractText().

