```ngMeta
name:  project-removing-the-header-from-csv-files
```
# Project: Removing the Header from CSV Files
Say you have the boring job of removing the first line from several hundred CSV files. Maybe you’ll be feeding them into an automated process that requires just the data and not the headers at the top of the columns. You could open each file in Excel, delete the first row, and resave the file—but that would take hours. Let’s write a program to do it instead.

The program will need to open every file with the .csv extension in the current working directory, read in the contents of the CSV file, and rewrite the contents without the first row to a file of the same name. This will replace the old contents of the CSV file with the new, headless contents.

# Note
As always, whenever you write a program that modifies files, be sure to back up the files, first just in case your program does not work the way you expect it to. You don’t want to accidentally erase your original files.

At a high level, the program must do the following:

Find all the CSV files in the current working directory.

Read in the full contents of each file.

Write out the contents, skipping the first line, to a new CSV file.

At the code level, this means the program will need to do the following:

Loop over a list of files from os.listdir(), skipping the non-CSV files.

Create a CSV Reader object and read in the contents of the file, using the line_num attribute to figure out which line to skip.

Create a CSV Writer object and write out the read-in data to the new file.

For this project, open a new file editor window and save it as removeCsvHeader.py.

# Step 1: Loop Through Each CSV File
The first thing your program needs to do is loop over a list of all CSV filenames for the current working directory. Make your removeCsvHeader.py look like this:


   #! python3
   # removeCsvHeader.py - Removes the header from all CSV files in the current
   # working directory.

   import csv, os

   os.makedirs('headerRemoved', exist_ok=True)

   # Loop through every file in the current working directory.
   for csvFilename in os.listdir('.'):
       if not csvFilename.endswith('.csv'):
❶         continue    # skip non-csv files

       print('Removing header from ' + csvFilename + '...')

       # TODO: Read the CSV file in (skipping first row).

       # TODO: Write out the CSV file.
The os.makedirs() call will create a headerRemoved folder where all the headless CSV files will be written. A for loop on os.listdir('.') gets you partway there, but it will loop over all files in the working directory, so you’ll need to add some code at the start of the loop that skips filenames that don’t end with .csv. The continue statement ❶ makes the for loop move on to the next filename when it comes across a non-CSV file.

Just so there’s some output as the program runs, print out a message saying which CSV file the program is working on. Then, add some TODO comments for what the rest of the program should do.

# Step 2: Read in the CSV File
The program doesn’t remove the first line from the CSV file. Rather, it creates a new copy of the CSV file without the first line. Since the copy’s filename is the same as the original filename, the copy will overwrite the original.

The program will need a way to track whether it is currently looping on the first row. Add the following to removeCsvHeader.py.


	#! python3
	# removeCsvHeader.py - Removes the header from all CSV files in the current
	# working directory.

--snip--
	# Read the CSV file in (skipping first row).
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue    # skip first row
    csvRows.append(row)
csvFileObj.close()

	# TODO: Write out the CSV file.
The Reader object’s line_num attribute can be used to determine which line in the CSV file it is currently reading. Another for loop will loop over the rows returned from the CSV Reader object, and all rows but the first will be appended to csvRows.

As the for loop iterates over each row, the code checks whether readerObj.line_num is set to 1. If so, it executes a continue to move on to the next row without appending it to csvRows. For every row afterward, the condition will be always be False, and the row will be appended to csvRows.

# Step 3: Write Out the CSV File Without the First Row
Now that csvRows contains all rows but the first row, the list needs to be written out to a CSV file in the headerRemoved folder. Add the following to removeCsvHeader.py:


   #! python3
   # removeCsvHeader.py - Removes the header from all CSV files in the current
   # working directory.
   --snip--

   # Loop through every file in the current working directory.
❶ for csvFilename in os.listdir('.'):
       if not csvFilename.endswith('.csv'):
           continue    # skip non-CSV files

       --snip--
```python
       # Write out the CSV file.
       csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                    newline='')
       csvWriter = csv.writer(csvFileObj)
       for row in csvRows:
           csvWriter.writerow(row)
       csvFileObj.close()
```
The CSV Writer object will write the list to a CSV file in headerRemoved using csvFilename (which we also used in the CSV reader). This will overwrite the original file.

Once we create the Writer object, we loop over the sublists stored in csvRows and write each sublist to the file.

After the code is executed, the outer for loop ❶ will loop to the next filename from os.listdir('.'). When that loop is finished, the program will be complete.

To test your program, download removeCsvHeader.zip from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> and unzip it to a folder. Run the removeCsvHeader.py program in that folder. The output will look like this:


Removing header from NAICS_data_1048.csv...
Removing header from NAICS_data_1218.csv...
--snip--
Removing header from NAICS_data_9834.csv...
Removing header from NAICS_data_9986.csv...
This program should print a filename each time it strips the first line from a CSV file.

Ideas for Similar Programs
The programs that you could write for CSV files are similar to the kinds you could write for Excel files, since they’re both spreadsheet files. You could write programs to do the following:

Compare data between different rows in a CSV file or between multiple CSV files.

Copy specific data from a CSV file to an Excel file, or vice versa.

Check for invalid data or formatting mistakes in CSV files and alert the user to these errors.

Read data from a CSV file as input for your Python programs.