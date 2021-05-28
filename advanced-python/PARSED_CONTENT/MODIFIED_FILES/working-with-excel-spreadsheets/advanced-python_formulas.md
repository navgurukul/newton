```ngMeta
formulas_key1
```
# formulas_key2
formulas_key3

```python
>>> sheet['B9'] = '=SUM(B1:B8)'
```
formulas_key4

formulas_key5

formulas_key6

```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.active
>>> sheet['A1'] = 200
>>> sheet['A2'] = 300
>>> sheet['A3'] = '=SUM(A1:A2)'
>>> wb.save('writeFormula.xlsx')
```
formulas_key7

formulas_key8