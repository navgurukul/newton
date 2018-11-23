```ngMeta
name:  converting-between-column-letters-and-numbers
completionMethod: manual
```
# Converting Between Column Letters and Numbers
To convert from letters to numbers, call the openpyxl.cell.column_index_from_string() function. To convert from numbers to letters, call the openpyxl.cell.get_column_letter() function. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> from openpyxl.cell import get_column_letter, column_index_from_string
>>> get_column_letter(1)
```
'A'
```python
>>> get_column_letter(2)
```
'B'
```python
>>> get_column_letter(27)
```
'AA'
```python
>>> get_column_letter(900)
```
'AHP'
```python
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> get_column_letter(sheet.max_column)
```
'C'
```python
>>> column_index_from_string('A')
```
1
```python
>>> column_index_from_string('AA')
```
27
After you import these two functions from the openpyxl.cell module, you can call get_column_letter() and pass it an integer like 27 to figure out what the letter name of the 27th column is. The function column_index_string() does the reverse: You pass it the letter name of a column, and it tells you what number that column is. You don’t need to have a workbook loaded to use these functions. If you want, you can load a workbook, get a Worksheet object, and call a Worksheet object method like max_column to get an integer. Then, you can pass that integer to get_column_letter().

# Getting Rows and Columns from the Sheets
You can slice Worksheet objects to get all the Cell objects in a row, column, or rectangular area of the spreadsheet. Then you can loop over all the cells in the slice. Enter the following into the interactive shell:

```python
   >>> import openpyxl
   >>> wb = openpyxl.load_workbook('example.xlsx')
   >>> sheet = wb.get_sheet_by_name('Sheet1')
   >>> tuple(sheet['A1':'C3'])
```
   ((<Cell Sheet1.A1>, <Cell Sheet1.B1>, <Cell Sheet1.C1>), (<Cell Sheet1.A2>,
   <Cell Sheet1.B2>, <Cell Sheet1.C2>), (<Cell Sheet1.A3>, <Cell Sheet1.B3>,
   <Cell Sheet1.C3>))
```python
❶ >>> for rowOfCellObjects in sheet['A1':'C3']:
❷         for cellObj in rowOfCellObjects:
               print(cellObj.coordinate, cellObj.value)
           print('--- END OF ROW ---')
```
   A1 2015-04-05 13:34:02
   B1 Apples
   C1 73
   --- END OF ROW ---
   A2 2015-04-05 03:41:23
   B2 Cherries
   C2 85
   --- END OF ROW ---
   A3 2015-04-06 12:46:51
   B3 Pears
   C3 14
   --- END OF ROW ---
Here, we specify that we want the Cell objects in the rectangular area from A1 to C3, and we get a Generator object containing the Cell objects in that area. To help us visualize this Generator object, we can use tuple() on it to display its Cell objects in a tuple.

This tuple contains three tuples: one for each row, from the top of the desired area to the bottom. Each of these three inner tuples contains the Cell objects in one row of our desired area, from the leftmost cell to the right. So overall, our slice of the sheet contains all the Cell objects in the area from A1 to C3, starting from the top-left cell and ending with the bottom-right cell.

To print the values of each cell in the area, we use two for loops. The outer for loop goes over each row in the slice ❶. Then, for each row, the nested for loop goes through each cell in that row ❷.

To access the values of cells in a particular row or column, you can also use a Worksheet object’s rows and columns attribute. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.active
>>> sheet.columns[1]
```
(<Cell Sheet1.B1>, <Cell Sheet1.B2>, <Cell Sheet1.B3>, <Cell Sheet1.B4>,
<Cell Sheet1.B5>, <Cell Sheet1.B6>, <Cell Sheet1.B7>)
```python
>>> for cellObj in sheet.columns[1]:
        print(cellObj.value)
```

Apples
Cherries
Pears
Oranges
Apples
Bananas
Strawberries
Using the rows attribute on a Worksheet object will give you a tuple of tuples. Each of these inner tuples represents a row, and contains the Cell objects in that row. The columns attribute also gives you a tuple of tuples, with each of the inner tuples containing the Cell objects in a particular column. For example.xlsx, since there are 7 rows and 3 columns, rows gives us a tuple of 7 tuples (each containing 3 Cell objects), and columns gives us a tuple of 3 tuples (each containing 7 Cell objects).

To access one particular tuple, you can refer to it by its index in the larger tuple. For example, to get the tuple that represents column B, you use sheet.columns[1]. To get the tuple containing the Cell objects in column A, you’d use sheet.columns[0]. Once you have a tuple representing one row or column, you can loop through its Cell objects and print their values.

