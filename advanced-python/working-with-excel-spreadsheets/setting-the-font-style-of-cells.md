```ngMeta
name: setting-the-font-style-of-cells
completionMethod: manual
```
# Setting the Font Style of Cells
Styling certain cells, rows, or columns can help you emphasize important areas in your spreadsheet. In the produce spreadsheet, for example, your program could apply bold text to the potato, garlic, and parsnip rows. Or perhaps you want to italicize every row with a cost per pound greater than $5. Styling parts of a large spreadsheet by hand would be tedious, but your programs can do it instantly.

To customize font styles in cells, important, import the Font() function from the openpyxl.styles module.


from openpyxl.styles import Font
This allows you to type Font() instead of openpyxl.styles.Font(). (See Importing Modules to review this style of import statement.)

Here’s an example that creates a new workbook and sets cell A1 to have a 24-point, italicized font. Enter the following into the interactive shell:

```python
   >>> import openpyxl
   >>> from openpyxl.styles import Font
   >>> wb = openpyxl.Workbook()
   >>> sheet = wb.get_sheet_by_name('Sheet')
❶ >>> italic24Font = Font(size=24, italic=True)
❷ >>> sheet['A1'].font = italic24Font
   >>> sheet['A1'] = 'Hello world!'
   >>> wb.save('styled.xlsx')
```
A cell’s style can be set by assigning the Font object to the style attribute.

In this example, Font(size=24, italic=True) returns a Font object, which is stored in italic24Font ❶. The keyword arguments to Font(), size and italic, configure the Font object. And when fontObj is assigned to the cell’s font attribute ❷, all that font styling information gets applied to cell A1.

# Font Objects
To set font style attributes, you pass keyword arguments to Font(). Table 12-2 shows the possible keyword arguments for the Font() function.

Table 12-2. Keyword Arguments for Font style Attributes

Keyword argument                 Data type                        Description

name                             String                   The font name, such as 'Calibri' or 'Times New Roman'

size                             Integer                  The point size

bold                             Boolean                  True, for bold font

italic                           Boolean                  True, for italic font

You can call Font() to create a Font object and store that Font object in a variable. You then pass that to Style(), store the resulting Style object in a variable, and assign that variable to a Cell object’s style attribute. For example, this code creates various font styles:

```python
>>> import openpyxl
>>> from openpyxl.styles import Font
>>> wb = openpyxl.Workbook()
>>> sheet = wb.get_sheet_by_name('Sheet')

>>> fontObj1 = Font(name='Times New Roman', bold=True)
>>> sheet['A1'].font = fontObj1
>>> sheet['A1'] = 'Bold Times New Roman'

>>> fontObj2 = Font(size=24, italic=True)
>>> sheet['B3'].font = fontObj2
>>> sheet['B3'] = '24 pt Italic'

>>> wb.save('styles.xlsx')
```
Here, we store a Font object in fontObj1 and then set the A1 Cell object’s font attribute to fontObj1. We repeat the process with another Font object to set the style of a second cell. After you run this code, the styles of the A1 and B3 cells in the spreadsheet will be set to custom font styles, as shown in Figure 12-4.

<!-- ![image](assets/000033.png)
 -->
Figure 12-4. A spreadsheet with custom font styles

For cell A1, we set the font name to 'Times New Roman' and set bold to true, so our text appears in bold Times New Roman. We didn’t specify a size, so the openpyxl default, 11, is used. In cell B3, our text is italic, with a size of 24; we didn’t specify a font name, so the openpyxl default, Calibri, is used.
