```ngMeta
converting-between-column-letters-and-numbers_key1
```
# converting-between-column-letters-and-numbers_key2
converting-between-column-letters-and-numbers_key3

```python
>>> import openpyxl
>>> from openpyxl.cell import get_column_letter, column_index_from_string
>>> get_column_letter(1)
```
converting-between-column-letters-and-numbers_key4```python
>>> get_column_letter(2)
```
converting-between-column-letters-and-numbers_key5```python
>>> get_column_letter(27)
```
converting-between-column-letters-and-numbers_key6```python
>>> get_column_letter(900)
```
converting-between-column-letters-and-numbers_key7```python
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> get_column_letter(sheet.max_column)
```
converting-between-column-letters-and-numbers_key8```python
>>> column_index_from_string('A')
```
converting-between-column-letters-and-numbers_key9```python
>>> column_index_from_string('AA')
```
converting-between-column-letters-and-numbers_key10

# converting-between-column-letters-and-numbers_key11
converting-between-column-letters-and-numbers_key12

```python
   >>> import openpyxl
   >>> wb = openpyxl.load_workbook('example.xlsx')
   >>> sheet = wb.get_sheet_by_name('Sheet1')
   >>> tuple(sheet['A1':'C3'])
```
converting-between-column-letters-and-numbers_key13converting-between-column-letters-and-numbers_key14converting-between-column-letters-and-numbers_key15converting-between-column-letters-and-numbers_key16converting-between-column-letters-and-numbers_key17converting-between-column-letters-and-numbers_key18converting-between-column-letters-and-numbers_key19converting-between-column-letters-and-numbers_key20converting-between-column-letters-and-numbers_key21converting-between-column-letters-and-numbers_key22```python
❶ >>> for rowOfCellObjects in sheet['A1':'C3']:
❷         for cellObj in rowOfCellObjects:
               print(cellObj.coordinate, cellObj.value)
           print('--- END OF ROW ---')
```
converting-between-column-letters-and-numbers_key23

converting-between-column-letters-and-numbers_key24

converting-between-column-letters-and-numbers_key25

converting-between-column-letters-and-numbers_key26

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.active
>>> sheet.columns[1]
```
converting-between-column-letters-and-numbers_key27converting-between-column-letters-and-numbers_key28converting-between-column-letters-and-numbers_key29converting-between-column-letters-and-numbers_key30converting-between-column-letters-and-numbers_key31converting-between-column-letters-and-numbers_key32converting-between-column-letters-and-numbers_key33converting-between-column-letters-and-numbers_key34```python
>>> for cellObj in sheet.columns[1]:
        print(cellObj.value)
```
converting-between-column-letters-and-numbers_key35

converting-between-column-letters-and-numbers_key36

