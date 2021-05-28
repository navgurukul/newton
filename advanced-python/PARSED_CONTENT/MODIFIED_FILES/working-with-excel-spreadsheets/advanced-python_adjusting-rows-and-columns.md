```ngMeta
adjusting-rows-and-columns_key1
```
# adjusting-rows-and-columns_key2
adjusting-rows-and-columns_key3

adjusting-rows-and-columns_key4

# adjusting-rows-and-columns_key5
adjusting-rows-and-columns_key6

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
adjusting-rows-and-columns_key7

adjusting-rows-and-columns_key8

adjusting-rows-and-columns_key9

adjusting-rows-and-columns_key10



