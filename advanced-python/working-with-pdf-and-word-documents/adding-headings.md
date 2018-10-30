```ngMeta
name: adding-headings
completionMethod: manual
```
# Adding Headings
Calling add_heading() adds a paragraph with one of the heading styles. Enter the following into the interactive shell:

```python
>>> doc = docx.Document()
>>> doc.add_heading('Header 0', 0)
<docx.text.Paragraph object at 0x00000000036CB3C8>
>>> doc.add_heading('Header 1', 1)
<docx.text.Paragraph object at 0x00000000036CB630>
>>> doc.add_heading('Header 2', 2)
<docx.text.Paragraph object at 0x00000000036CB828>
>>> doc.add_heading('Header 3', 3)
<docx.text.Paragraph object at 0x00000000036CB2E8>
>>> doc.add_heading('Header 4', 4)
<docx.text.Paragraph object at 0x00000000036CB3C8>
>>> doc.save('headings.docx')
```
The arguments to add_heading() are a string of the heading text and an integer from 0 to 4. The integer 0 makes the heading the Title style, which is used for the top of the document. Integers 1 to 4 are for various heading levels, with 1 being the main heading and 4 the lowest subheading. The add_heading() function returns a Paragraph object to save you the step of extracting it from the Document object as a separate step.

The resulting headings.docx file will look like Figure 13-10.

<!-- ![image](assets/000050.jpg)
 -->
Figure 13-10. The headings.docx document with headings 0 to 4

