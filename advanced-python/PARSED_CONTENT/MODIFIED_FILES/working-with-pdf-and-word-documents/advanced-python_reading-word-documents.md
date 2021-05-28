```ngMeta
reading-word-documents_key1
```
# reading-word-documents_key2
reading-word-documents_key3reading-word-documents_key4reading-word-documents_key5

```python
   >>> import docx
❶ >>> doc = docx.Document('demo.docx')
❷ >>> len(doc.paragraphs)
```
reading-word-documents_key6```python
❸ >>> doc.paragraphs[0].text
```
reading-word-documents_key7```python
❹ >>> doc.paragraphs[1].text
```
reading-word-documents_key8```python
❺ >>> len(doc.paragraphs[1].runs)
```
reading-word-documents_key9```python
❻ >>> doc.paragraphs[1].runs[0].text
```
reading-word-documents_key10```python
❼ >>> doc.paragraphs[1].runs[1].text
```
reading-word-documents_key11```python
❽ >>> doc.paragraphs[1].runs[2].text
```
reading-word-documents_key12```python
➒ >>> doc.paragraphs[1].runs[3].text
```
reading-word-documents_key13

reading-word-documents_key14

reading-word-documents_key15