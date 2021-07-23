```ngMeta
overlaying-pages_key1
```

overlaying-pages_key2
overlaying-pages_key3


overlaying-pages_key4


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
overlaying-pages_key5


overlaying-pages_key6


overlaying-pages_key7


![image](assets/000101.jpg)overlaying-pages_key8
