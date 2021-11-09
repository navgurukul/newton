reading-word-documents_key1
reading-word-documents_key2


```python
   >>> import docx
❶ >>> doc = docx.Document('demo.docx')
❷ >>> len(doc.paragraphs)
```
reading-word-documents_key3
```python
❸ >>> doc.paragraphs[0].text
```
reading-word-documents_key4
```python
❹ >>> doc.paragraphs[1].text
```
reading-word-documents_key5
```python
❺ >>> len(doc.paragraphs[1].runs)
```
reading-word-documents_key6
```python
❻ >>> doc.paragraphs[1].runs[0].text
```
reading-word-documents_key7
```python
❼ >>> doc.paragraphs[1].runs[1].text
```
reading-word-documents_key8
```python
❽ >>> doc.paragraphs[1].runs[2].text
```
reading-word-documents_key9
```python
➒ >>> doc.paragraphs[1].runs[3].text
```
reading-word-documents_key10


reading-word-documents_key11


reading-word-documents_key12
