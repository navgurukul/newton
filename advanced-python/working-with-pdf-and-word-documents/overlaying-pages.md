```ngMeta
name: overlaying-pages
completionMethod: manual
```
# Overlaying Pages
PyPDF2 can also overlay the contents of one page over another, which is useful for adding a logo, timestamp, or watermark to a page. With Python, it’s easy to add watermarks to multiple files and only to pages your program specifies.

Download watermark.pdf from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> and place the PDF in the current working directory along with meetingminutes.pdf. Then enter the following into the interactive shell:

```python
   >>> import PyPDF2
   >>> minutesFile = open('meetingminutes.pdf', 'rb')
❷ >>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
❷ >>> minutesFirstPage = pdfReader.getPage(0)
❸ >>> pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
❹ >>> minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
❺ >>> pdfWriter = PyPDF2.PdfFileWriter()
❻ >>> pdfWriter.addPage(minutesFirstPage)

❼ >>> for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)
   >>> resultPdfFile = open('watermarkedCover.pdf', 'wb')
   >>> pdfWriter.write(resultPdfFile)
   >>> minutesFile.close()
   >>> resultPdfFile.close()
```
Here we make a PdfFileReader object of meetingminutes.pdf ❶. We call getPage(0) to get a Page object for the first page and store this object in minutesFirstPage ❷. We then make a PdfFileReader object for watermark.pdf ❸ and call mergePage() on minutesFirstPage ❹. The argument we pass to mergePage() is a Page object for the first page of watermark.pdf.

Now that we’ve called mergePage() on minutesFirstPage, minutesFirstPage represents the watermarked first page. We make a PdfFileWriter object ❺ and add the watermarked first page ❻. Then we loop through the rest of the pages in meetingminutes.pdf and add them to the PdfFileWriter object ❼. Finally, we open a new PDF called watermarkedCover.pdf and write the contents of the PdfFileWriter to the new PDF.

Figure 13-3 shows the results. Our new PDF, watermarkedCover.pdf, has all the contents of the meetingminutes.pdf, and the first page is watermarked.

<!-- ![image](assets/000101.jpg)
 -->
Figure 13-3. The original PDF (left), the watermark PDF (center), and the merged PDF (right)
