```ngMeta
name: workbooks-sheets-cells
```
# Workbooks, Sheets, Cells
As a quick review, here’s a rundown of all the functions, methods, and data types involved in reading a cell out of a spreadsheet file:

Import the openpyxl module.

Call the openpyxl.load_workbook() function.

Get a Workbook object.

Read the active member variable or call the get_sheet_by_name() workbook method.

Get a Worksheet object.

Use indexing or the cell() sheet method with row and column keyword arguments.

Get a Cell object.

Read the Cell object’s value attribute.
# Project: Reading Data from a Spreadsheet
Say you have a spreadsheet of data from the 2010 US Census and you have the boring task of going through its thousands of rows to count both the total population and the number of census tracts for each county. (A census tract is simply a geographic area defined for the purposes of the census.) Each row represents a single census tract. We’ll name the spreadsheet file censuspopdata.xlsx, and you can download it from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>. Its contents look like Figure 12-2.

<!-- ![image](assets/000026.png)
 -->
Figure 12-2. The censuspopdata.xlsx spreadsheet

Even though Excel can calculate the sum of multiple selected cells, you’d still have to select the cells for each of the 3,000-plus counties. Even if it takes just a few seconds to calculate a county’s population by hand, this would take hours to do for the whole spreadsheet.

In this project, you’ll write a script that can read from the census spreadsheet file and calculate statistics for each county in a matter of seconds.

This is what your program does:

Reads the data from the Excel spreadsheet.

Counts the number of census tracts in each county.

Counts the total population of each county.

Prints the results.

This means your code will need to do the following:

Open and read the cells of an Excel document with the openpyxl module.

Calculate all the tract and population data and store it in a data structure.

Write the data structure to a text file with the .py extension using the pprint module.

# Step 1: Read the Spreadsheet Data
There is just one sheet in the censuspopdata.xlsx spreadsheet, named 'Population by Census Tract', and each row holds the data for a single census tract. The columns are the tract number (A), the state abbreviation (B), the county name (C), and the population of the tract (D).

Open a new file editor window and enter the following code. Save the file as readCensusExcel.py.


   #! python3
   # readCensusExcel.py - Tabulates population and number of census tracts for
   # each county.

❶ import openpyxl, pprint
   print('Opening workbook...')
❷ wb = openpyxl.load_workbook('censuspopdata.xlsx')
❸ sheet = wb.get_sheet_by_name('Population by Census Tract')
   countyData = {}

   # TODO: Fill in countyData with each county's population and tracts.
   print('Reading rows...')
❹ for row in range(2, sheet.max_row + 1):
       # Each row in the spreadsheet has data for one census tract.
       state  = sheet['B' + str(row)].value
       county = sheet['C' + str(row)].value
       pop    = sheet['D' + str(row)].value

   # TODO: Open a new text file and write the contents of countyData to it.
This code imports the openpyxl module, as well as the pprint module that you’ll use to print the final county data ❶. Then it opens the censuspopdata.xlsx file ❷, gets the sheet with the census data ❸, and begins iterating over its rows ❹.

Note that you’ve also created a variable named countyData, which will contain the populations and number of tracts you calculate for each county. Before you can store anything in it, though, you should determine exactly how you’ll structure the data inside it.

# Step 2: Populate the Data Structure
The data structure stored in countyData will be a dictionary with state abbreviations as its keys. Each state abbreviation will map to another dictionary, whose keys are strings of the county names in that state. Each county name will in turn map to a dictionary with just two keys, 'tracts' and 'pop'. These keys map to the number of census tracts and population for the county. For example, the dictionary will look similar to this:


{'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1},
        'Aleutians West': {'pop': 5561, 'tracts': 2},
        'Anchorage': {'pop': 291826, 'tracts': 55},
        'Bethel': {'pop': 17013, 'tracts': 3},
        'Bristol Bay': {'pop': 997, 'tracts': 1},
        --snip--
If the previous dictionary were stored in countyData, the following expressions would evaluate like this:

```python
>>> countyData['AK']['Anchorage']['pop']
```
291826
```python
>>> countyData['AK']['Anchorage']['tracts']
```
55
More generally, the countyData dictionary’s keys will look like this:


countyData[state abbrev][county]['tracts']
countyData[state abbrev][county]['pop']
Now that you know how countyData will be structured, you can write the code that will fill it with the county data. Add the following code to the bottom of your program:


   #! python 3
   # readCensusExcel.py - Tabulates population and number of census tracts for
   # each county.

   --snip--
   for row in range(2, sheet.max_row + 1):
       # Each row in the spreadsheet has data for one census tract.
       state  = sheet['B' + str(row)].value
       county = sheet['C' + str(row)].value
       pop    = sheet['D' + str(row)].value

       # Make sure the key for this state exists.
❶     countyData.setdefault(state, {})
       # Make sure the key for this county in this state exists.
❷     countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

       # Each row represents one census tract, so increment by one.
❸     countyData[state][county]['tracts'] += 1
       # Increase the county pop by the pop in this census tract.
❹     countyData[state][county]['pop'] += int(pop)

   # TODO: Open a new text file and write the contents of countyData to it.
The last two lines of code perform the actual calculation work, incrementing the value for tracts ❸ and increasing the value for pop ❹ for the current county on each iteration of the for loop.

The other code is there because you cannot add a county dictionary as the value for a state abbreviation key until the key itself exists in countyData. (That is, countyData['AK']['Anchorage']['tracts'] += 1 will cause an error if the 'AK' key doesn’t exist yet.) To make sure the state abbreviation key exists in your data structure, you need to call the setdefault() method to set a value if one does not already exist for state ❶.

Just as the countyData dictionary needs a dictionary as the value for each state abbreviation key, each of those dictionaries will need its own dictionary as the value for each county key ❷. And each of those dictionaries in turn will need keys 'tracts' and 'pop' that start with the integer value 0. (If you ever lose track of the dictionary structure, look back at the example dictionary at the start of this section.)

Since setdefault() will do nothing if the key already exists, you can call it on every iteration of the for loop without a problem.

# Step 3: Write the Results to a File
After the for loop has finished, the countyData dictionary will contain all of the population and tract information keyed by county and state. At this point, you could program more code to write this to a text file or another Excel spreadsheet. For now, let’s just use the pprint.pformat() function to write the countyData dictionary value as a massive string to a file named census2010.py. Add the following code to the bottom of your program (making sure to keep it unindented so that it stays outside the for loop):


 #! python 3
 # readCensusExcel.py - Tabulates population and number of census tracts for
 # each county.get_active_sheet
--snip--

for row in range(2, sheet.max_row + 1):
--snip--

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
The pprint.pformat() function produces a string that itself is formatted as valid Python code. By outputting it to a text file named census2010.py, you’ve generated a Python program from your Python program! This may seem complicated, but the advantage is that you can now import census2010.py just like any other Python module. In the interactive shell, change the current working directory to the folder with your newly created census2010.py file (on my laptop, this is C:\Python34), and then import it:

```python
>>> import os
>>> os.chdir('C:\\Python34')
>>> import census2010
>>> census2010.allData['AK']['Anchorage']
```
{'pop': 291826, 'tracts': 55}
```python
>>> anchoragePop = census2010.allData['AK']['Anchorage']['pop']
>>> print('The 2010 population of Anchorage was ' + str(anchoragePop))
```
The 2010 population of Anchorage was 291826
The readCensusExcel.py program was throwaway code: Once you have its results saved to census2010.py, you won’t need to run the program again. Whenever you need the county data, you can just run import census2010.

Calculating this data by hand would have taken hours; this program did it in a few seconds. Using OpenPyXL, you will have no trouble extracting information that is saved to an Excel spreadsheet and performing calculations on it. You can download the complete program from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>.
# Ideas for Similar Programs
Many businesses and offices use Excel to store various types of data, and it’s not uncommon for spreadsheets to become large and unwieldy. Any program that parses an Excel spreadsheet has a similar structure: It loads the spreadsheet file, preps some variables or data structures, and then loops through each of the rows in the spreadsheet. Such a program could do the following:

Compare data across multiple rows in a spreadsheet.

Open multiple Excel files and compare data between spreadsheets.

Check whether a spreadsheet has blank rows or invalid data in any cells and alert the user if it does.

Read data from a spreadsheet and use it as the input for your Python programs.




