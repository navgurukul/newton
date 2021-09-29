creating-pdfs_key1
creating-pdfs_key2


creating-pdfs_key3


creating-pdfs_key4


creating-pdfs_key5


creating-pdfs_key6


creating-pdfs_key7


creating-pdfs_key8


creating-pdfs_key9


creating-pdfs_key10


creating-pdfs_key11
creating-pdfs_key12


creating-pdfs_key13


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
creating-pdfs_key14


creating-pdfs_key15


creating-pdfs_key16
creating-pdfs_key17


creating-pdfs_key18


creating-pdfs_key19
creating-pdfs_key20


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
creating-pdfs_key21


creating-pdfs_key22


![image](assets/000104.jpg)
creating-pdfs_key23
