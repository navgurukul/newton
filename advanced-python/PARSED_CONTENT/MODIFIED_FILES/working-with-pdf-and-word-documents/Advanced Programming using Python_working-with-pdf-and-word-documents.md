```ngMeta
working-with-pdf-and-word-documents_key1
```

working-with-pdf-and-word-documents_key2
working-with-pdf-and-word-documents_key3


working-with-pdf-and-word-documents_key4


working-with-pdf-and-word-documents_key5
working-with-pdf-and-word-documents_key6


working-with-pdf-and-word-documents_key7


working-with-pdf-and-word-documents_key8
working-with-pdf-and-word-documents_key9


working-with-pdf-and-word-documents_key10
working-with-pdf-and-word-documents_key11


![image](assets/000065.jpg)working-with-pdf-and-word-documents_key12


working-with-pdf-and-word-documents_key13


```python
   >>> import PyPDF2
   >>> pdfFileObj = open('meetingminutes.pdf', 'rb')
   >>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
❶ >>> pdfReader.numPages
```
working-with-pdf-and-word-documents_key14
```python
❷ >>> pageObj = pdfReader.getPage(0)
❸ >>> pageObj.extractText()
```
working-with-pdf-and-word-documents_key15


working-with-pdf-and-word-documents_key16


working-with-pdf-and-word-documents_key17


working-with-pdf-and-word-documents_key18


working-with-pdf-and-word-documents_key19
