```ngMeta
name: getting-the-full-text-from-a-docx-file
completionMethod: manual
```
# Getting the Full Text from a .docx File
If you care only about the text, not the styling information, in the Word document, you can use the getText() function. It accepts a filename of a .docx file and returns a single string value of its text. Open a new file editor window and enter the following code, saving it as readDocx.py:


	#! python3

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
The getText() function opens the Word document, loops over all the Paragraph objects in the paragraphs list, and then appends their text to the list in fullText. After the loop, the strings in fullText are joined together with newline characters.

The readDocx.py program can be imported like any other module. Now if you just need the text from a Word document, you can enter the following:

```python
>>> import readDocx
>>> print(readDocx.getText('demo.docx'))
```
Document Title
A plain paragraph with some bold and some italic
Heading, level 1
Intense quote
first item in unordered list
first item in ordered list
You can also adjust getText() to modify the string before returning it. For example, to indent each paragraph, replace the append() call in readDocx.py with this:


fullText.append(' ' + para.text)
To add a double space in between paragraphs, change the join() call code to this:


return '\n\n'.join(fullText)
As you can see, it takes only a few lines of code to write functions that will read a .docx file and return a string of its content to your liking.

# Styling Paragraph and Run Objects
In Word for Windows, you can see the styles by pressing CTRL-ALT-SHIFT-S to display the Styles pane, which looks like Figure 13-5. On OS X, you can view the Styles pane by clicking the View▸Styles menu item.

<!-- ![image](assets/000035.jpg)
 -->
Figure 13-5. Display the Styles pane by pressing CTRL-ALT-SHIFT-S on Windows.

Word and other word processors use styles to keep the visual presentation of similar types of text consistent and easy to change. For example, perhaps you want to set body paragraphs in 11-point, Times New Roman, left-justified, ragged-right text. You can create a style with these settings and assign it to all body paragraphs. Then, if you later want to change the presentation of all body paragraphs in the document, you can just change the style, and all those paragraphs will be automatically updated.

For Word documents, there are three types of styles: Paragraph styles can be applied to Paragraph objects, character styles can be applied to Run objects, and linked styles can be applied to both kinds of objects. You can give both Paragraph and Run objects styles by setting their style attribute to a string. This string should be the name of a style. If style is set to None, then there will be no style associated with the Paragraph or Run object.

The string values for the default Word styles are as follows:

'Normal'               'Heading5'             'ListBullet'                     'ListParagraph'

'BodyText'             'Heading6'              'ListBullet2'                    'MacroText'

'BodyText2'            'Heading7'               'ListBullet3'                   'NoSpacing'

'BodyText3'             'Heading8'               'ListContinue'                 'Quote'

'Caption'               'Heading9'               'ListContinue2'                'Subtitle'

'Heading1'              'IntenseQuote'            'ListContinue3'                'TOCHeading'

'Heading2'               'List'                    'ListNumber'                   'Title'

'Heading3'               'List2'                   'ListNumber2'

'Heading4'               'List3'                    'ListNumber3'

 
When setting the style attribute, do not use spaces in the style name. For example, while the style name may be Subtle Emphasis, you should set the style attribute to the string value 'SubtleEmphasis' instead of 'Subtle Emphasis'. Including spaces will cause Word to misread the style name and not apply it.

When using a linked style for a Run object, you will need to add 'Char' to the end of its name. For example, to set the Quote linked style for a Paragraph object, you would use paragraphObj.style = 'Quote', but for a Run object, you would use runObj.style = 'QuoteChar'.

In the current version of Python-Docx (0.7.4), the only styles that can be used are the default Word styles and the styles in the opened .docx. New styles cannot be created—though this may change in future versions of Python-Docx.

