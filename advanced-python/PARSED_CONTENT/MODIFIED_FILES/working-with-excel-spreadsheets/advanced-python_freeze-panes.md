```ngMeta
freeze-panes_key1
```
# freeze-panes_key2
freeze-panes_key3

freeze-panes_key4

freeze-panes_key5

freeze-panes_key6

freeze-panes_key7

freeze-panes_key8

freeze-panes_key9

freeze-panes_key10

freeze-panes_key11freeze-panes_key12freeze-panes_key13

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('produceSales.xlsx')
>>> sheet = wb.active
>>> sheet.freeze_panes = 'A2'
>>> wb.save('freezeExample.xlsx')
```
freeze-panes_key14

freeze-panes_key15



