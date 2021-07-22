```ngMeta
setting-the-font-style-of-cells_key1
```

setting-the-font-style-of-cells_key2
setting-the-font-style-of-cells_key3


setting-the-font-style-of-cells_key4



setting-the-font-style-of-cells_key5


setting-the-font-style-of-cells_key6


```python
   >>> import openpyxl
   >>> from openpyxl.styles import Font
   >>> wb = openpyxl.Workbook()
   >>> sheet = wb.get_sheet_by_name('Sheet')
❶ >>> italic24Font = Font(size=24, italic=True)
❷ >>> sheet['A1'].font = italic24Font
   >>> sheet['A1'] = 'Hello world!'
   >>> wb.save('styled.xlsx')
```
setting-the-font-style-of-cells_key7


setting-the-font-style-of-cells_key8


setting-the-font-style-of-cells_key9
setting-the-font-style-of-cells_key10


setting-the-font-style-of-cells_key11


setting-the-font-style-of-cells_key12


setting-the-font-style-of-cells_key13


setting-the-font-style-of-cells_key14


setting-the-font-style-of-cells_key15


setting-the-font-style-of-cells_key16


setting-the-font-style-of-cells_key17


```python
>>> import openpyxl
>>> from openpyxl.styles import Font
>>> wb = openpyxl.Workbook()
>>> sheet = wb.get_sheet_by_name('Sheet')

>>> fontObj1 = Font(name='Times New Roman', bold=True)
>>> sheet['A1'].font = fontObj1
>>> sheet['A1'] = 'Bold Times New Roman'

>>> fontObj2 = Font(size=24, italic=True)
>>> sheet['B3'].font = fontObj2
>>> sheet['B3'] = '24 pt Italic'

>>> wb.save('styles.xlsx')
```
setting-the-font-style-of-cells_key18


![image](assets/000033.png)setting-the-font-style-of-cells_key19


setting-the-font-style-of-cells_key20
