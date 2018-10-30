```ngMeta
name: chapter-12
completionMethod: manual
```
# Chapter 12
The openpyxl.load_workbook() function returns a Workbook object.

The get_sheet_names() method returns a Worksheet object.

Call wb.get_sheet_by_name('Sheet1').

Call wb.get_active_sheet().

sheet['C5'].value or sheet.cell(row=5, column=3).value

sheet['C5'] = 'Hello' or sheet.cell(row=5, column=3).value = 'Hello'

cell.row and cell.column

They return the highest column and row with values in the sheet, respectively, as integer values.

openpyxl.cell.column_index_from_string('M')

openpyxl.cell.get_column_letter(14)

sheet['A1':'F1']

wb.save('example.xlsx’)

A formula is set the same way as any value. Set the cell’s value attribute to a string of the formula text. Remember that formulas begin with the = sign.

sheet.row_dimensions[5].height = 100

sheet.column_dimensions['C'].hidden = True

OpenPyXL 2.0.5 does not load freeze panes, print titles, images, or charts.

Freeze panes are rows and columns that will always appear on the screen. They are useful for headers.

openpyxl.charts.Reference(), openpyxl.charts.Series(), openpyxl.charts. BarChart(), chartObj.append(seriesObj), and add_chart()