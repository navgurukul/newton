```ngMeta
name: spreadsheet-cell-inverter
```
# Spreadsheet Cell Inverter
Write a program to invert the row and column of the cells in the spreadsheet. For example, the value at row 5, column 3 will be at row 3, column 5 (and vice versa). This should be done for all cells in the spreadsheet. For example, the “before” and “after” spreadsheets would look something like Figure 12-13.

<!-- ![image](assets/79.jpg)
 -->
Figure 12-13. The spreadsheet before (top) and after (bottom) inversion

You can write this program by using nested for loops to read in the spreadsheet’s data into a list of lists data structure. This data structure could have sheetData[x][y] for the cell at column x and row y. Then, when writing out the new spreadsheet, use sheetData[y][x] for the cell at column x and row y.

# Text Files to Spreadsheet
Write a program to read in the contents of several text files (you can make the text files yourself) and insert those contents into a spreadsheet, with one line of text per row. The lines of the first text file will be in the cells of column A, the lines of the second text file will be in the cells of column B, and so on.

Use the readlines() File object method to return a list of strings, one string per line in the file. For the first file, output the first line to column 1, row 1. The second line should be written to column 1, row 2, and so on. The next file that is read with readlines() will be written to column 2, the next file to column 3, and so on.

# Spreadsheet to Text Files
Write a program that performs the tasks of the previous program in reverse order: The program should open a spreadsheet and write the cells of column A into one text file, the cells of column B into another text file, and so on.



