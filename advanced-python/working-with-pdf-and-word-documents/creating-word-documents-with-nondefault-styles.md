```ngMeta
name: creating-word-documents-with-nondefault-styles
completionMethod: manual
```
# Creating Word Documents with Nondefault Styles
If you want to create Word documents that use styles beyond the default ones, you will need to open Word to a blank Word document and create the styles yourself by clicking the New Style button at the bottom of the Styles pane (Figure 13-6 shows this on Windows).

This will open the Create New Style from Formatting dialog, where you can enter the new style. Then, go back into the interactive shell and open this blank Word document with docx.Document(), using it as the base for your Word document. The name you gave this style will now be available to use with Python-Docx.

<!-- ![image](assets/000048.jpg)
 -->
Figure 13-6. The New Style button (left) and the Create New Style from Formatting dialog (right)
Run Attributes
Runs can be further styled using text attributes. Each attribute can be set to one of three values: True (the attribute is always enabled, no matter what other styles are applied to the run), False (the attribute is always disabled), or None (defaults to whatever the run’s style is set to).

Table 13-1 lists the text attributes that can be set on Run objects.

Table 13-1. Run Object text Attributes

Attribute   									Description

bold											The text appears in bold.

italic											The text appears in italic.

underlined 										The text is underlined.

strike  										The text appears with strikethrough.

double_strike 									The text appears with double strikethrough.

all_caps 										The text appears in capital letters.

small_caps										The text appears in capital letters, with lowercase letters two points smaller.

shadow 											The text appears with a shadow.

outline 										The text appears outlined rather than solid.

rtl 											The text is written right-to-left.

imprint 										The text appears pressed into the page.

emboss 											The text appears raised off the page in relief.

For example, to change the styles of demo.docx, enter the following into the interactive shell:

```python
>>> doc = docx.Document('demo.docx')
>>> doc.paragraphs[0].text
```
'Document Title'
```python
>>> doc.paragraphs[0].style
```
'Title'
```python
>>> doc.paragraphs[0].style = 'Normal'
>>> doc.paragraphs[1].text
```
'A plain paragraph with some bold and some italic'
```python
>>> (doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.
```
paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text)
('A plain paragraph with some ', 'bold', ' and some ', 'italic')
```python
>>> doc.paragraphs[1].runs[0].style = 'QuoteChar'
>>> doc.paragraphs[1].runs[1].underline = True
>>> doc.paragraphs[1].runs[3].underline = True
>>> doc.save('restyled.docx')
```
Here, we use the text and style attributes to easily see what’s in the paragraphs in our document. We can see that it’s simple to divide a paragraph into runs and access each run individiaully. So we get the first, second, and fourth runs in the second paragraph, style each run, and save the results to a new document.

The words Document Title at the top of restyled.docx will have the Normal style instead of the Title style, the Run object for the text A plain paragraph with some will have the QuoteChar style, and the two Run objects for the words bold and italic will have their underline attributes set to True. Figure 13-7 shows how the styles of paragraphs and runs look in restyled.docx.

<!-- ![image](assets/000086.jpg)
 -->
Figure 13-7. The restyled.docx file

You can find more complete documentation on Python-Docx’s use of styles at <span><a href="https://python-docx.readthedocs.org/en/latest/user/styles.html.">https://python-docx.readthedocs.org/en/latest/user/styles.html.</a></span>




