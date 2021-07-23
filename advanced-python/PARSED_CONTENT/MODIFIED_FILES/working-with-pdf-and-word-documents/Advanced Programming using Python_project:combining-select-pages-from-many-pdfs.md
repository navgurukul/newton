```ngMeta
project:combining-select-pages-from-many-pdfs_key1
```

project:combining-select-pages-from-many-pdfs_key2
project:combining-select-pages-from-many-pdfs_key3


project:combining-select-pages-from-many-pdfs_key4


project:combining-select-pages-from-many-pdfs_key5


project:combining-select-pages-from-many-pdfs_key6


project:combining-select-pages-from-many-pdfs_key7


project:combining-select-pages-from-many-pdfs_key8


project:combining-select-pages-from-many-pdfs_key9


project:combining-select-pages-from-many-pdfs_key10


project:combining-select-pages-from-many-pdfs_key11


project:combining-select-pages-from-many-pdfs_key12


project:combining-select-pages-from-many-pdfs_key13


project:combining-select-pages-from-many-pdfs_key14


project:combining-select-pages-from-many-pdfs_key15


project:combining-select-pages-from-many-pdfs_key16


project:combining-select-pages-from-many-pdfs_key17
project:combining-select-pages-from-many-pdfs_key18



project:combining-select-pages-from-many-pdfs_key19
project:combining-select-pages-from-many-pdfs_key20
project:combining-select-pages-from-many-pdfs_key21
project:combining-select-pages-from-many-pdfs_key22


project:combining-select-pages-from-many-pdfs_key23
project:combining-select-pages-from-many-pdfs_key24


project:combining-select-pages-from-many-pdfs_key25


project:combining-select-pages-from-many-pdfs_key26
project:combining-select-pages-from-many-pdfs_key27
project:combining-select-pages-from-many-pdfs_key28
project:combining-select-pages-from-many-pdfs_key29


project:combining-select-pages-from-many-pdfs_key30


project:combining-select-pages-from-many-pdfs_key31
project:combining-select-pages-from-many-pdfs_key32



project:combining-select-pages-from-many-pdfs_key33
project:combining-select-pages-from-many-pdfs_key34
project:combining-select-pages-from-many-pdfs_key35
project:combining-select-pages-from-many-pdfs_key36


project:combining-select-pages-from-many-pdfs_key37
project:combining-select-pages-from-many-pdfs_key38
```python
  # Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
```
project:combining-select-pages-from-many-pdfs_key39
project:combining-select-pages-from-many-pdfs_key40


project:combining-select-pages-from-many-pdfs_key41
project:combining-select-pages-from-many-pdfs_key42



project:combining-select-pages-from-many-pdfs_key43
project:combining-select-pages-from-many-pdfs_key44
project:combining-select-pages-from-many-pdfs_key45
project:combining-select-pages-from-many-pdfs_key46


project:combining-select-pages-from-many-pdfs_key47


project:combining-select-pages-from-many-pdfs_key48
project:combining-select-pages-from-many-pdfs_key49
```python
       # Loop through all the pages (except the first) and add them.
❶     for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)
```
project:combining-select-pages-from-many-pdfs_key50
project:combining-select-pages-from-many-pdfs_key51


project:combining-select-pages-from-many-pdfs_key52
project:combining-select-pages-from-many-pdfs_key53



project:combining-select-pages-from-many-pdfs_key54
project:combining-select-pages-from-many-pdfs_key55
project:combining-select-pages-from-many-pdfs_key56
project:combining-select-pages-from-many-pdfs_key57


project:combining-select-pages-from-many-pdfs_key58


project:combining-select-pages-from-many-pdfs_key59
project:combining-select-pages-from-many-pdfs_key60
```python
#Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
```
project:combining-select-pages-from-many-pdfs_key61


project:combining-select-pages-from-many-pdfs_key62
project:combining-select-pages-from-many-pdfs_key63


project:combining-select-pages-from-many-pdfs_key64


project:combining-select-pages-from-many-pdfs_key65


project:combining-select-pages-from-many-pdfs_key66
