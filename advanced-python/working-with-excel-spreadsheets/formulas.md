```ngMeta
name: formulas
completionMethod: manual
```
# Formulas
Formulas, which begin with an equal sign, can configure cells to contain values calculated from other cells. In this section, you’ll use the openpyxl module to programmatically add formulas to cells, just like any normal value. For example:

```python
>>> sheet['B9'] = '=SUM(B1:B8)'
```
This will store =SUM(B1:B8) as the value in cell B9. This sets the B9 cell to a formula that calculates the sum of values in cells B1 to B8. You can see this in action in Figure 12-5.

<!-- ![image](assets/000012.jpg)
 -->
Figure 12-5. Cell B9 contains the formula =SUM(B1:B8), which adds the cells B1 to B8.

A formula is set just like any other text value in a cell. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.active
>>> sheet['A1'] = 200
>>> sheet['A2'] = 300
>>> sheet['A3'] = '=SUM(A1:A2)'
>>> wb.save('writeFormula.xlsx')
```
The cells in A1 and A2 are set to 200 and 300, respectively. The value in cell A3 is set to a formula that sums the values in A1 and A2. When the spreadsheet is opened in Excel, A3 will display its value as 500.

Excel formulas offer a level of programmability for spreadsheets but can quickly become unmanageable for complicated tasks. For example, even if you’re deeply familiar with Excel formulas, it’s a headache to try to decipher what =IFERROR(TRIM(IF(LEN(VLOOKUP(F7, Sheet2!$A$1:$B$10000, 2, FALSE))>0,SUBSTITUTE(VLOOKUP(F7, Sheet2!$A$1:$B$10000, 2, FALSE), “ ”, “”),“”)), “”) actually does. Python code is much more readable.