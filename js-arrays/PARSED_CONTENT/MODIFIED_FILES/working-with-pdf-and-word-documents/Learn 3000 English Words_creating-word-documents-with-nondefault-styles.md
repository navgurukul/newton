creating-word-documents-with-nondefault-styles_key1
creating-word-documents-with-nondefault-styles_key2


creating-word-documents-with-nondefault-styles_key3


![image](assets/000048.jpg)
creating-word-documents-with-nondefault-styles_key4


creating-word-documents-with-nondefault-styles_key5


creating-word-documents-with-nondefault-styles_key6


creating-word-documents-with-nondefault-styles_key7


creating-word-documents-with-nondefault-styles_key8


creating-word-documents-with-nondefault-styles_key9


creating-word-documents-with-nondefault-styles_key10


creating-word-documents-with-nondefault-styles_key11


creating-word-documents-with-nondefault-styles_key12


creating-word-documents-with-nondefault-styles_key13


creating-word-documents-with-nondefault-styles_key14


creating-word-documents-with-nondefault-styles_key15


creating-word-documents-with-nondefault-styles_key16


creating-word-documents-with-nondefault-styles_key17


creating-word-documents-with-nondefault-styles_key18


creating-word-documents-with-nondefault-styles_key19


creating-word-documents-with-nondefault-styles_key20


```python
>>> doc = docx.Document('demo.docx')
>>> doc.paragraphs[0].text
```
creating-word-documents-with-nondefault-styles_key21
```python
>>> doc.paragraphs[0].style
```
creating-word-documents-with-nondefault-styles_key22
```python
>>> doc.paragraphs[0].style = 'Normal'
>>> doc.paragraphs[1].text
```
creating-word-documents-with-nondefault-styles_key23
```python
>>> (doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.
```
creating-word-documents-with-nondefault-styles_key24
```python
>>> doc.paragraphs[1].runs[0].style = 'QuoteChar'
>>> doc.paragraphs[1].runs[1].underline = True
>>> doc.paragraphs[1].runs[3].underline = True
>>> doc.save('restyled.docx')
```
creating-word-documents-with-nondefault-styles_key25


creating-word-documents-with-nondefault-styles_key26


![image](assets/000086.jpg)
creating-word-documents-with-nondefault-styles_key27


creating-word-documents-with-nondefault-styles_key28
