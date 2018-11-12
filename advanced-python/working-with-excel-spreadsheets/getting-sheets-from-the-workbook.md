```ngMeta
name: getting-sheets-from-the-workbook
completionMethod: manual
```
# Getting Sheets from the Workbook
You can get a list of all the sheet names in the workbook by calling the get_sheet_names() method. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> wb.get_sheet_names()
```
['Sheet1', 'Sheet2', 'Sheet3']
```python
>>> sheet = wb.get_sheet_by_name('Sheet3')
>>> sheet
```
<Worksheet "Sheet3">

>>> type(sheet) <class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> sheet.title
'Sheet3'

```python
>>> anotherSheet = wb.active
>>> anotherSheet
```
<Worksheet "Sheet1">
Each sheet is represented by a Worksheet object, which you can obtain by passing the sheet name string to the get_sheet_by_name() workbook method. Finally, you can read the active member variable of a Workbook object to get the workbook’s active sheet. The active sheet is the sheet that’s on top when the workbook is opened in Excel. Once you have the Worksheet object, you can get its name from the title attribute.

# Getting Cells from the Sheets
Once you have a Worksheet object, you can access a Cell object by its name. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet['A1']
```
<Cell Sheet1.A1>
```python
>>> sheet['A1'].value
```
datetime.datetime(2015, 4, 5, 13, 34, 2)
```python
>>> c = sheet['B1']
>>> c.value
```
'Apples'
```python
>>> 'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value
```
'Row 1, Column B is Apples'
```python
>>> 'Cell ' + c.coordinate + ' is ' + c.value
```
'Cell B1 is Apples'
```python
>>> sheet['C1'].value
```
73
The Cell object has a value attribute that contains, unsurprisingly, the value stored in that cell. Cell objects also have row, column, and coordinate attributes that provide location information for the cell.

Here, accessing the value attribute of our Cell object for cell B1 gives us the string 'Apples'. The row attribute gives us the integer 1, the column attribute gives us 'B', and the coordinate attribute gives us 'B1'.

OpenPyXL will automatically interpret the dates in column A and return them as datetime values rather than strings. The datetime data type is explained further in Chapter 16.

Specifying a column by letter can be tricky to program, especially because after column Z, the columns start by using two letters: AA, AB, AC, and so on. As an alternative, you can also get a cell using the sheet’s cell() method and passing integers for its row and column keyword arguments. The first row or column integer is 1, not 0. Continue the interactive shell example by entering the following:

```python
>>> sheet.cell(row=1, column=2)
```
<Cell Sheet1.B1>
```python
>>> sheet.cell(row=1, column=2).value
```
'Apples'
```python
>>> for i in range(1, 8, 2):
        print(i, sheet.cell(row=i, column=2).value)
```

1 Apples
3 Pears
5 Apples
7 Strawberries
As you can see, using the sheet’s cell() method and passing it row=1 and column=2 gets you a Cell object for cell B1, just like specifying sheet['B1'] did. Then, using the cell() method and its keyword arguments, you can write a for loop to print the values of a series of cells.

Say you want to go down column B and print the value in every cell with an odd row number. By passing 2 for the range() function’s “step” parameter, you can get cells from every second row (in this case, all the odd-numbered rows). The for loop’s i variable is passed for the row keyword argument to the cell() method, while 2 is always passed for the column keyword argument. Note that the integer 2, not the string 'B', is passed.

You can determine the size of the sheet with the Worksheet object’s max_row and max_column member variables. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet.max_row
```
7
```python
>>> sheet.max_column
```
3
Note that the max_column method returns an integer rather than the letter that appears in Excel.