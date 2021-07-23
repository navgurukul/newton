```ngMeta
merging-and-unmerging-cells_key1
```

merging-and-unmerging-cells_key2
merging-and-unmerging-cells_key3


```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.active
>>> sheet.merge_cells('A1:D3')
>>> sheet['A1'] = 'Twelve cells merged together.'
>>> sheet.merge_cells('C5:D5')
>>> sheet['C5'] = 'Two merged cells.'
>>> wb.save('merged.xlsx')
```
merging-and-unmerging-cells_key4


merging-and-unmerging-cells_key5


![image](assets/000040.png)merging-and-unmerging-cells_key6


merging-and-unmerging-cells_key7


```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('merged.xlsx')
>>> sheet = wb.active
>>> sheet.unmerge_cells('A1:D3')
>>> sheet.unmerge_cells('C5:D5')
>>> wb.save('merged.xlsx')
```
merging-and-unmerging-cells_key8
