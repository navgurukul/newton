```ngMeta
name: project-updating-a-spreadsheet
completionMethod: manual
```
# Project: Updating a Spreadsheet
In this project, you’ll write a program to update cells in a spreadsheet of produce sales. Your program will look through the spreadsheet, find specific kinds of produce, and update their prices. Download this spreadsheet from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>. Figure 12-3 shows what the spreadsheet looks like.

<!-- ![image](assets/000030.jpg)
 -->
Figure 12-3. A spreadsheet of produce sales

Each row represents an individual sale. The columns are the type of produce sold (A), the cost per pound of that produce (B), the number of pounds sold (C), and the total revenue from the sale (D). The TOTAL column is set to the Excel formula =ROUND(B3*C3, 2), which multiplies the cost per pound by the number of pounds sold and rounds the result to the nearest cent. With this formula, the cells in the TOTAL column will automatically update themselves if there is a change in column B or C.
Now imagine that the prices of garlic, celery, and lemons were entered incorrectly, leaving you with the boring task of going through thousands of rows in this spreadsheet to update the cost per pound for any garlic, celery, and lemon rows. You can’t do a simple find-and-replace for the price because there might be other items with the same price that you don’t want to mistakenly “correct.” For thousands of rows, this would take hours to do by hand. But you can write a program that can accomplish this in seconds.
Your program does the following:
Loops over all the rows.
If the row is for garlic, celery, or lemons, changes the price.
This means your code will need to do the following:
Open the spreadsheet file.
For each row, check whether the value in column A is Celery, Garlic, or Lemon.
If it is, update the price in column B.
Save the spreadsheet to a new file (so that you don’t lose the old spreadsheet, just in case).
# Step 1: Set Up a Data Structure with the Update Information
The prices that you need to update are as follows:
Celery
1.19
Garlic
3.07
Lemon
1.27
You could write code like this:
if produceName == 'Celery':
    cellObj = 1.19
if produceName == 'Garlic':
    cellObj = 3.07
if produceName == 'Lemon':
    cellObj = 1.27
Having the produce and updated price data hardcoded like this is a bit inelegant. If you needed to update the spreadsheet again with different prices or different produce, you would have to change a lot of the code. Every time you change code, you risk introducing bugs.
A more flexible solution is to store the corrected price information in a dictionary and write your code to use this data structure. In a new file editor window, enter the following code:
#! python3
# updateProduce.py - Corrects costs in produce sales spreadsheet.
import openpyxl
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
# The produce types and their updated prices
PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}
# TODO: Loop through the rows and update the prices.
Save this as updateProduce.py. If you need to update the spreadsheet again, you’ll need to update only the PRICE_UPDATES dictionary, not any other code.
# Step 2: Check All Rows and Update Incorrect Prices
The next part of the program will loop through all the rows in the spreadsheet. Add the following code to the bottom of updateProduce.py:
   #! python3
   # updateProduce.py - Corrects costs in produce sales spreadsheet.
   --snip--
   # Loop through the rows and update the prices.
❶ for rowNum in range(2, sheet.max_row):  # skip the first row
❷     produceName = sheet.cell(row=rowNum, column=1).value
❸     if produceName in PRICE_UPDATES:
           sheet.cell(row=rowNum, column=2).value = PRICE_UPDATES[produceName]
❹ wb.save('updatedProduceSales.xlsx')
We loop through the rows starting at row 2, since row 1 is just the header ❶. The cell in column 1 (that is, column A) will be stored in the variable produceName ❷. If produceName exists as a key in the PRICE_UPDATES dictionary ❸, then you know this is a row that must have its price corrected. The correct price will be in PRICE_UPDATES[produceName].
Notice how clean using PRICE_UPDATES makes the code. Only one if statement, rather than code like if produceName == 'Garlic':, is necessary for every type of produce to update. And since the code uses the PRICE_UPDATES dictionary instead of hardcoding the produce names and updated costs into the for loop, you modify only the PRICE_UPDATES dictionary and not the code if the produce sales spreadsheet needs additional changes.
After going through the entire spreadsheet and making changes, the code saves the Workbook object to updatedProduceSales.xlsx ❹. It doesn’t overwrite the old spreadsheet just in case there’s a bug in your program and the updated spreadsheet is wrong. After checking that the updated spreadsheet looks right, you can delete the old spreadsheet.
You can download the complete source code for this program from <span><a href="http://nostarch.com/automatestuff/.">http://nostarch.com/automatestuff/.</a></span>
Ideas for Similar Programs
Since many office workers use Excel spreadsheets all the time, a program that can automatically edit and write Excel files could be really useful. Such a program could do the following:
Read data from one spreadsheet and write it to parts of other spreadsheets.
Read data from websites, text files, or the clipboard and write it to a spreadsheet.
Automatically “clean up” data in spreadsheets. For example, it could use regular expressions to read multiple formats of phone numbers and edit them to a single, standard format.