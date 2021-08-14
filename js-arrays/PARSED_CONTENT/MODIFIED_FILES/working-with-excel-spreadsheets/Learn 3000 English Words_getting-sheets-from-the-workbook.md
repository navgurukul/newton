getting-sheets-from-the-workbook_key1
getting-sheets-from-the-workbook_key2


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> wb.get_sheet_names()
```
getting-sheets-from-the-workbook_key3
```python
>>> sheet = wb.get_sheet_by_name('Sheet3')
>>> sheet
```
getting-sheets-from-the-workbook_key4


>>> getting-sheets-from-the-workbook_key5
```python
>>> anotherSheet = wb.active
>>> anotherSheet
```
getting-sheets-from-the-workbook_key6


getting-sheets-from-the-workbook_key7
getting-sheets-from-the-workbook_key8


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet['A1']
```
```python
>>> sheet['A1'].value
```
getting-sheets-from-the-workbook_key9
```python
>>> c = sheet['B1']
>>> c.value
```
getting-sheets-from-the-workbook_key10
```python
>>> 'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value
```
getting-sheets-from-the-workbook_key11
```python
>>> 'Cell ' + c.coordinate + ' is ' + c.value
```
getting-sheets-from-the-workbook_key12
```python
>>> sheet['C1'].value
```
getting-sheets-from-the-workbook_key13


getting-sheets-from-the-workbook_key14


getting-sheets-from-the-workbook_key15


getting-sheets-from-the-workbook_key16


```python
>>> sheet.cell(row=1, column=2)
```
```python
>>> sheet.cell(row=1, column=2).value
```
getting-sheets-from-the-workbook_key17
```python
>>> for i in range(1, 8, 2):
        print(i, sheet.cell(row=i, column=2).value)
```

getting-sheets-from-the-workbook_key18


getting-sheets-from-the-workbook_key19


getting-sheets-from-the-workbook_key20


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet.max_row
```
getting-sheets-from-the-workbook_key21
```python
>>> sheet.max_column
```
getting-sheets-from-the-workbook_key22
