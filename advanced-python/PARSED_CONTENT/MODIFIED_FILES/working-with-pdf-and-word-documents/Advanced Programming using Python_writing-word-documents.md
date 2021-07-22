```ngMeta
writing-word-documents_key1
```

writing-word-documents_key2
writing-word-documents_key3


```python
>>> import docx
>>> doc = docx.Document()
>>> doc.add_paragraph('Hello world!')
<docx.text.Paragraph object at 0x0000000003B56F60>
>>> doc.save('helloworld.docx')
```
writing-word-documents_key4


writing-word-documents_key5


![image](assets/000038.jpg)writing-word-documents_key6


writing-word-documents_key7


```python
>>> import docx
>>> doc = docx.Document()
>>> doc.add_paragraph('Hello world!')
<docx.text.Paragraph object at 0x000000000366AD30>
>>> paraObj1 = doc.add_paragraph('This is a second paragraph.')
>>> paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
>>> paraObj1.add_run(' This text is being added to the second paragraph.')
<docx.text.Run object at 0x0000000003A2C860>
>>> doc.save('multipleParagraphs.docx')
```
writing-word-documents_key8


writing-word-documents_key9


writing-word-documents_key10


![image](assets/000045.jpg)writing-word-documents_key11


writing-word-documents_key12


```python
>>> doc.add_paragraph('Hello world!', 'Title')
```
writing-word-documents_key13
