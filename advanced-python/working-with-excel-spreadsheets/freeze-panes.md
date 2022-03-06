```ngMeta
name: freeze-panes
```
# Freeze Panes
For spreadsheets too large to be displayed all at once, it’s helpful to “freeze” a few of the top rows or leftmost columns onscreen. Frozen column or row headers, for example, are always visible to the user even as they scroll through the spreadsheet. These are known as freeze panes. In OpenPyXL, each Worksheet object has a freeze_panes attribute that can be set to a Cell object or a string of a cell’s coordinates. Note that all rows above and all columns to the left of this cell will be frozen, but the row and column of the cell itself will not be frozen.

To unfreeze all panes, set freeze_panes to None or 'A1'. Table 12-3 shows which rows and columns will be frozen for some example settings of freeze_panes.

Table 12-3. Frozen Pane Examples

freeze_panes setting 							Rows and columns frozen

sheet.freeze_panes = 'A2' 						Row 1

sheet.freeze_panes = 'B1'						Column A

sheet.freeze_panes = 'C1'						Columns A and B

sheet.freeze_panes = 'C2'       				Row 1 and columns A and B

sheet.freeze_panes = 'A1' or sheet.freeze_panes = No frozen panes
None
Make sure you have the produce sales spreadsheet from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>. Then enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('produceSales.xlsx')
>>> sheet = wb.active
>>> sheet.freeze_panes = 'A2'
>>> wb.save('freezeExample.xlsx')
```
If you set the freeze_panes attribute to 'A2', row 1 will always be viewable, no matter where the user scrolls in the spreadsheet. You can see this in Figure 12-8.

<!-- ![image](assets/000044.jpg)
 -->
Figure 12-8. With freeze_panes set to 'A2', row 1 is always visible even as the user scrolls down.



