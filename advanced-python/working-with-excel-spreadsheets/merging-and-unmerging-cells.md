```ngMeta
name:  merging-and-unmerging-cells
```
# Merging and Unmerging Cells
A rectangular area of cells can be merged into a single cell with the merge_cells() sheet method. Enter the following into the interactive shell:

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
The argument to merge_cells() is a single string of the top-left and bottom-right cells of the rectangular area to be merged: 'A1:D3' merges 12 cells into a single cell. To set the value of these merged cells, simply set the value of the top-left cell of the merged group.

When you run this code, merged.xlsx will look like Figure 12-7.

<!-- ![image](assets/000040.png)
 -->
Figure 12-7. Merged cells in a spreadsheet

To unmerge cells, call the unmerge_cells() sheet method. Enter this into the interactive shell.

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('merged.xlsx')
>>> sheet = wb.active
>>> sheet.unmerge_cells('A1:D3')
>>> sheet.unmerge_cells('C5:D5')
>>> wb.save('merged.xlsx')
```
If you save your changes and then take a look at the spreadsheet, you’ll see that the merged cells have gone back to being individual cells.


