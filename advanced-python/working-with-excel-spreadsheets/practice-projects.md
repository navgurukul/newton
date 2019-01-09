```ngMeta
name: practice-projects
```
# Practice Projects
For practice, write programs that perform the following tasks.

Multiplication Table Maker
Create a program multiplicationTable.py that takes a number N from the command line and creates an N×N multiplication table in an Excel spreadsheet. For example, when the program is run like this:


py multiplicationTable.py 6
... it should create a spreadsheet that looks like Figure 12-11.

<!-- ![image](assets/000052.jpg)
 -->
Figure 12-11. A multiplication table generated in a spreadsheet

Row 1 and column A should be used for labels and should be in bold.

# Blank Row Inserter
Create a program blankRowInserter.py that takes two integers and a filename string as command line arguments. Let’s call the first integer N and the second integer M. Starting at row N, the program should insert M blank rows into the spreadsheet. For example, when the program is run like this:


python blankRowInserter.py 3 2 myProduce.xlsx
... the “before” and “after” spreadsheets should look like Figure 12-12.

<!-- ![image](assets/000055.jpg)
 -->
Figure 12-12. Before (left) and after (right) the two blank rows are inserted at row 3

You can write this program by reading in the contents of the spreadsheet. Then, when writing out the new spreadsheet, use a for loop to copy the first N lines. For the remaining lines, add M to the row number in the output spreadsheet.