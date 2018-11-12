```ngMeta
name:  writing-excel-documents
completionMethod: manual
```
# Writing Excel Documents
OpenPyXL also provides ways of writing data, meaning that your programs can create and edit spreadsheet files. With Python, it’s simple to create spreadsheets with thousands of rows of data.

Creating and Saving Excel Documents
Call the openpyxl.Workbook() function to create a new, blank Workbook object. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb.get_sheet_names()
```
['Sheet']
```python
>>> sheet = wb.active
>>> sheet.title
```
'Sheet'
```python
>>> sheet.title = 'Spam Bacon Eggs Sheet'
>>> wb.get_sheet_names()
```
['Spam Bacon Eggs Sheet']
The workbook will start off with a single sheet named Sheet. You can change the name of the sheet by storing a new string in its title attribute.

Any time you modify the Workbook object or its sheets and cells, the spreadsheet file will not be saved until you call the save() workbook method. Enter the following into the interactive shell (with example.xlsx in the current working directory):

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.active
>>> sheet.title = 'Spam Spam Spam'
>>> wb.save('example_copy.xlsx')
```
Here, we change the name of our sheet. To save our changes, we pass a filename as a string to the save() method. Passing a different filename than the original, such as 'example_copy.xlsx', saves the changes to a copy of the spreadsheet.

Whenever you edit a spreadsheet you’ve loaded from a file, you should always save the new, edited spreadsheet to a different filename than the original. That way, you’ll still have the original spreadsheet file to work with in case a bug in your code caused the new, saved file to have incorrect or corrupt data.

Creating and Removing Sheets
Sheets can be added to and removed from a workbook with the create_sheet() and remove_sheet() methods. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb.get_sheet_names()
```
['Sheet']
```python
>>> wb.create_sheet()
```
<Worksheet "Sheet1">
```python
>>> wb.get_sheet_names()
```
['Sheet', 'Sheet1']
```python
>>> wb.create_sheet(index=0, title='First Sheet')
```
<Worksheet "First Sheet">
```python
>>> wb.get_sheet_names()
```
['First Sheet', 'Sheet', 'Sheet1']
```python
>>> wb.create_sheet(index=2, title='Middle Sheet')
```
<Worksheet "Middle Sheet">
```python
>>> wb.get_sheet_names()
```
['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']
The create_sheet() method returns a new Worksheet object named SheetX, which by default is set to be the last sheet in the workbook. Optionally, the index and name of the new sheet can be specified with the index and title keyword arguments.

Continue the previous example by entering the following:

```python
>>> wb.get_sheet_names()
```
['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']
```python
>>> wb.remove_sheet(wb.get_sheet_by_name('Middle Sheet'))
>>> wb.remove_sheet(wb.get_sheet_by_name('Sheet1'))
>>> wb.get_sheet_names()
```
['First Sheet', 'Sheet']
The remove_sheet() method takes a Worksheet object, not a string of the sheet name, as its argument. If you know only the name of a sheet you want to remove, call get_sheet_by_name() and pass its return value into remove_sheet().

Remember to call the save() method to save the changes after adding sheets to or removing sheets from the workbook.
# Writing Values to Cells
Writing values to cells is much like writing values to keys in a dictionary. Enter this into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.get_sheet_by_name('Sheet')
>>> sheet['A1'] = 'Hello world!'
>>> sheet['A1'].value
```
'Hello world!'
If you have the cell’s coordinate as a string, you can use it just like a dictionary key on the Worksheet object to specify which cell to write to.

