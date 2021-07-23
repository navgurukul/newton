```ngMeta
writing-excel-documents_key1
```

writing-excel-documents_key2
writing-excel-documents_key3


writing-excel-documents_key4


```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb.get_sheet_names()
```
writing-excel-documents_key5
```python
>>> sheet = wb.active
>>> sheet.title
```
writing-excel-documents_key6
```python
>>> sheet.title = 'Spam Bacon Eggs Sheet'
>>> wb.get_sheet_names()
```
writing-excel-documents_key7


writing-excel-documents_key8


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.active
>>> sheet.title = 'Spam Spam Spam'
>>> wb.save('example_copy.xlsx')
```
writing-excel-documents_key9


writing-excel-documents_key10


writing-excel-documents_key11


```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb.get_sheet_names()
```
writing-excel-documents_key12
```python
>>> wb.create_sheet()
```
writing-excel-documents_key13
```python
>>> wb.get_sheet_names()
```
writing-excel-documents_key14
```python
>>> wb.create_sheet(index=0, title='First Sheet')
```
writing-excel-documents_key15
```python
>>> wb.get_sheet_names()
```
writing-excel-documents_key16
```python
>>> wb.create_sheet(index=2, title='Middle Sheet')
```
writing-excel-documents_key17
```python
>>> wb.get_sheet_names()
```
writing-excel-documents_key18


writing-excel-documents_key19


```python
>>> wb.get_sheet_names()
```
writing-excel-documents_key20
```python
>>> wb.remove_sheet(wb.get_sheet_by_name('Middle Sheet'))
>>> wb.remove_sheet(wb.get_sheet_by_name('Sheet1'))
>>> wb.get_sheet_names()
```
writing-excel-documents_key21


writing-excel-documents_key22
writing-excel-documents_key23
writing-excel-documents_key24


```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.get_sheet_by_name('Sheet')
>>> sheet['A1'] = 'Hello world!'
>>> sheet['A1'].value
```
writing-excel-documents_key25
