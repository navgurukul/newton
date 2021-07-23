```ngMeta
getting-sheets-from-the-workbook_key1
```

getting-sheets-from-the-workbook_key2
getting-sheets-from-the-workbook_key3


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> wb.get_sheet_names()
```
getting-sheets-from-the-workbook_key4
```python
>>> sheet = wb.get_sheet_by_name('Sheet3')
>>> sheet
```
getting-sheets-from-the-workbook_key5


getting-sheets-from-the-workbook_key6
```python
>>> anotherSheet = wb.active
>>> anotherSheet
```
getting-sheets-from-the-workbook_key7


getting-sheets-from-the-workbook_key8
getting-sheets-from-the-workbook_key9


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet['A1']
```
getting-sheets-from-the-workbook_key10


getting-sheets-from-the-workbook_key11


getting-sheets-from-the-workbook_key12


```python
>>> sheet.cell(row=1, column=2)
```
getting-sheets-from-the-workbook_key13


getting-sheets-from-the-workbook_key14


getting-sheets-from-the-workbook_key15


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet.max_row
```
getting-sheets-from-the-workbook_key16
```python
>>> sheet.max_column
```
getting-sheets-from-the-workbook_key17
