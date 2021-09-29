adding-line-and-page-breaks_key1
adding-line-and-page-breaks_key2


```python
   >>> doc = docx.Document()
   >>> doc.add_paragraph('This is on the first page!')
   <docx.text.Paragraph object at 0x0000000003785518>
❶ >>> doc.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)
   >>> doc.add_paragraph('This is on the second page!')
   <docx.text.Paragraph object at 0x00000000037855F8>
   >>> doc.save('twoPage.docx')
```
adding-line-and-page-breaks_key3


adding-line-and-page-breaks_key4
adding-line-and-page-breaks_key5


```python
>>> doc.add_picture('zophie.png', width=docx.shared.Inches(1),
```
adding-line-and-page-breaks_key6


adding-line-and-page-breaks_key7


adding-line-and-page-breaks_key8
adding-line-and-page-breaks_key9


adding-line-and-page-breaks_key10


adding-line-and-page-breaks_key11
