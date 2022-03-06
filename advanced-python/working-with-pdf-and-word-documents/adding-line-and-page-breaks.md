```ngMeta
name: adding-line-and-page-breaks
```
# Adding Line and Page Breaks
To add a line break (rather than starting a whole new paragraph), you can call the add_break() method on the Run object you want to have the break appear after. If you want to add a page break instead, you need to pass the value docx.text.WD_BREAK.PAGE as a lone argument to add_break(), as is done in the middle of the following example:

```python
   >>> doc = docx.Document()
   >>> doc.add_paragraph('This is on the first page!')
   <docx.text.Paragraph object at 0x0000000003785518>
❶ >>> doc.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)
   >>> doc.add_paragraph('This is on the second page!')
   <docx.text.Paragraph object at 0x00000000037855F8>
   >>> doc.save('twoPage.docx')
```
This creates a two-page Word document with This is on the first page! on the first page and This is on the second page! on the second. Even though there was still plenty of space on the first page after the text This is on the first page!, we forced the next paragraph to begin on a new page by inserting a page break after the first run of the first paragraph ❶.

# Adding Pictures
Document objects have an add_picture() method that will let you add an image to the end of the document. Say you have a file zophie.png in the current working directory. You can add zophie.png to the end of your document with a width of 1 inch and height of 4 centimeters (Word can use both imperial and metric units) by entering the following:

```python
>>> doc.add_picture('zophie.png', width=docx.shared.Inches(1),
```
height=docx.shared.Cm(4))
<docx.shape.InlineShape object at 0x00000000036C7D30>
The first argument is a string of the image’s filename. The optional width and height keyword arguments will set the width and height of the image in the document. If left out, the width and height will default to the normal size of the image.

You’ll probably prefer to specify an image’s height and width in familiar units such as inches and centimeters, so you can use the docx.shared.Inches() and docx.shared.Cm() functions when you’re specifying the width and height keyword arguments.

# Summary
Text information isn’t just for plaintext files; in fact, it’s pretty likely that you deal with PDFs and Word documents much more often. You can use the PyPDF2 module to read and write PDF documents. Unfortunately, reading text from PDF documents might not always result in a perfect translation to a string because of the complicated PDF file format, and some PDFs might not be readable at all. In these cases, you’re out of luck unless future updates to PyPDF2 support additional PDF features.

Word documents are more reliable, and you can read them with the python-docx module. You can manipulate text in Word documents via Paragraph and Run objects. These objects can also be given styles, though they must be from the default set of styles or styles already in the document. You can add new paragraphs, headings, breaks, and pictures to the document, though only to the end.

Many of the limitations that come with working with PDFs and Word documents are because these formats are meant to be nicely displayed for human readers, rather than easy to parse by software. The next chapter takes a look at two other common formats for storing information: JSON and CSV files. These formats are designed to be used by computers, and you’ll see that Python can work with these formats much more easily.

