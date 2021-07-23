```ngMeta
converting-between-column-letters-and-numbers_key1
```

converting-between-column-letters-and-numbers_key2
converting-between-column-letters-and-numbers_key3


```python
>>> import openpyxl
>>> from openpyxl.cell import get_column_letter, column_index_from_string
>>> get_column_letter(1)
```
converting-between-column-letters-and-numbers_key4
```python
>>> get_column_letter(2)
```
converting-between-column-letters-and-numbers_key5
```python
>>> get_column_letter(27)
```
converting-between-column-letters-and-numbers_key6
```python
>>> get_column_letter(900)
```
converting-between-column-letters-and-numbers_key7
```python
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> get_column_letter(sheet.max_column)
```
converting-between-column-letters-and-numbers_key8
```python
>>> column_index_from_string('A')
```
converting-between-column-letters-and-numbers_key9
```python
>>> column_index_from_string('AA')
```
converting-between-column-letters-and-numbers_key10


converting-between-column-letters-and-numbers_key11
converting-between-column-letters-and-numbers_key12


```python
   >>> import openpyxl
   >>> wb = openpyxl.load_workbook('example.xlsx')
   >>> sheet = wb.get_sheet_by_name('Sheet1')
   >>> tuple(sheet['A1':'C3'])
```
converting-between-column-letters-and-numbers_key13
```python
❶ >>> for rowOfCellObjects in sheet['A1':'C3']:
❷         for cellObj in rowOfCellObjects:
               print(cellObj.coordinate, cellObj.value)
           print('--- END OF ROW ---')
```
converting-between-column-letters-and-numbers_key14


converting-between-column-letters-and-numbers_key15


converting-between-column-letters-and-numbers_key16


converting-between-column-letters-and-numbers_key17


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.active
>>> sheet.columns[1]
```
converting-between-column-letters-and-numbers_key18
```python
>>> for cellObj in sheet.columns[1]:
        print(cellObj.value)
```
converting-between-column-letters-and-numbers_key19


converting-between-column-letters-and-numbers_key20
