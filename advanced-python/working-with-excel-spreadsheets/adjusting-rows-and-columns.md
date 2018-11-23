```ngMeta
name: adjusting-rows-and-columns
completionMethod: manual
```
# Adjusting Rows and Columns
In Excel, adjusting the sizes of rows and columns is as easy as clicking and dragging the edges of a row or column header. But if you need to set a row or column’s size based on its cells’ contents or if you want to set sizes in a large number of spreadsheet files, it will be much quicker to write a Python program to do it.

Rows and columns can also be hidden entirely from view. Or they can be “frozen” in place so that they are always visible on the screen and appear on every page when the spreadsheet is printed (which is handy for headers).

# Setting Row Height and Column Width
Worksheet objects have row_dimensions and column_dimensions attributes that control row heights and column widths. Enter this into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.active
>>> sheet['A1'] = 'Tall row'
>>> sheet['B2'] = 'Wide column'
>>> sheet.row_dimensions[1].height = 70
>>> sheet.column_dimensions['B'].width = 20
>>> wb.save('dimensions.xlsx')
```
A sheet’s row_dimensions and column_dimensions are dictionary-like values; row_dimensions contains RowDimension objects and column_dimensions contains ColumnDimension objects. In row_dimensions, you can access one of the objects using the number of the row (in this case, 1 or 2). In column_dimensions, you can access one of the objects using the letter of the column (in this case, A or B).

The dimensions.xlsx spreadsheet looks like Figure 12-6.

<!-- ![image](assets/000098.jpg)
 -->
Figure 12-6. Row 1 and column B set to larger heights and widths

Once you have the RowDimension object, you can set its height. Once you have the ColumnDimension object, you can set its width. The row height can be set to an integer or float value between 0 and 409. This value represents the height measured in points, where one point equals 1/72 of an inch. The default row height is 12.75. The column width can be set to an integer or float value between 0 and 255. This value represents the number of characters at the default font size (11 point) that can be displayed in the cell. The default column width is 8.43 characters. Columns with widths of 0 or rows with heights of 0 are hidden from the user.



