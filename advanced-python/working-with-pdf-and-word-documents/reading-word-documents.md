```ngMeta
name: reading-word-documents
```
# Reading Word Documents
Let’s experiment with the python-docx module. Download demo.docx from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> and save the document to the working directory. Then enter the following into the interactive shell:

```python
   >>> import docx
❶ >>> doc = docx.Document('demo.docx')
❷ >>> len(doc.paragraphs)
```
   7
```python
❸ >>> doc.paragraphs[0].text
```
   'Document Title'
```python
❹ >>> doc.paragraphs[1].text
```
   'A plain paragraph with some bold and some italic'
```python
❺ >>> len(doc.paragraphs[1].runs)
```
   4
```python
❻ >>> doc.paragraphs[1].runs[0].text
```
   'A plain paragraph with some '
```python
❼ >>> doc.paragraphs[1].runs[1].text
```
   'bold'
```python
❽ >>> doc.paragraphs[1].runs[2].text
```
   ' and some '
```python
➒ >>> doc.paragraphs[1].runs[3].text
```
   'italic'
At ❶, we open a .docx file in Python, call docx.Document(), and pass the filename demo.docx. This will return a Document object, which has a paragraphs attribute that is a list of Paragraph objects. When we call len() on doc.paragraphs, it returns 7, which tells us that there are seven Paragraph objects in this document ❷. Each of these Paragraph objects has a text attribute that contains a string of the text in that paragraph (without the style information). Here, the first text attribute contains 'DocumentTitle' ❸, and the second contains 'A plain paragraph with some bold and some italic' ❹.

Each Paragraph object also has a runs attribute that is a list of Run objects. Run objects also have a text attribute, containing just the text in that particular run. Let’s look at the text attributes in the second Paragraph object, 'A plain paragraph with some bold and some italic'. Calling len() on this Paragraph object tells us that there are four Run objects ❺. The first run object contains 'A plain paragraph with some ' ❻. Then, the text change to a bold style, so 'bold' starts a new Run object ❼. The text returns to an unbolded style after that, which results in a third Run object, ' and some ' ❽. Finally, the fourth and last Run object contains 'italic' in an italic style ➒.

With Python-Docx, your Python programs will now be able to read the text from a .docx file and use it just like any other string value.