```ngMeta
name:  writing-word-documents
```
# Writing Word Documents
Enter the following into the interactive shell:

```python
>>> import docx
>>> doc = docx.Document()
>>> doc.add_paragraph('Hello world!')
<docx.text.Paragraph object at 0x0000000003B56F60>
>>> doc.save('helloworld.docx')
```
To create your own .docx file, call docx.Document() to return a new, blank Word Document object. The add_paragraph() document method adds a new paragraph of text to the document and returns a reference to the Paragraph object that was added. When you’re done adding text, pass a filename string to the save() document method to save the Document object to a file.

This will create a file named helloworld.docx in the current working directory that, when opened, looks like Figure 13-8.

<!-- ![image](assets/000038.jpg)
 -->
Figure 13-8. The Word document created using add_paragraph('Hello world!')

You can add paragraphs by calling the add_paragraph() method again with the new paragraph’s text. Or to add text to the end of an existing paragraph, you can call the paragraph’s add_run() method and pass it a string. Enter the following into the interactive shell:

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
The resulting document will look like Figure 13-9. Note that the text This text is being added to the second paragraph. was added to the Paragraph object in paraObj1, which was the second paragraph added to doc. The add_paragraph() and add_run() functions return paragraph and Run objects, respectively, to save you the trouble of extracting them as a separate step.

Keep in mind that as of Python-Docx version 0.5.3, new Paragraph objects can be added only to the end of the document, and new Run objects can be added only to the end of a Paragraph object.

The save() method can be called again to save the additional changes you’ve made.

<!-- ![image](assets/000045.jpg)
 -->
Figure 13-9. The document with multiple Paragraph and Run objects added

Both add_paragraph() and add_run() accept an optional second argument that is a string of the Paragraph or Run object’s style. For example:

```python
>>> doc.add_paragraph('Hello world!', 'Title')
```
This line adds a paragraph with the text Hello world! in the Title style.




