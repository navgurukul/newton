```ngMeta
name: Project: Renaming Files with American-Style Dates to European-Style Dates
completionMethod: manual
```
# Project: Renaming Files with American-Style Dates to European-Style Dates
Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to European-style dates (DD-MM-YYYY). This boring task could take all day to do by hand! Let’s write a program to do it instead.

Here’s what the program does:

It searches all the filenames in the current working directory for American-style dates.

When one is found, it renames the file with the month and day swapped to make it European-style.

This means the code will need to do the following:

Create a regex that can identify the text pattern of American-style dates.

Call os.listdir() to find all the files in the working directory.

Loop over each filename, using the regex to check whether it has a date.

If it has a date, rename the file with shutil.move().

For this project, open a new file editor window and save your code as renameDates.py.

# Step 1: Create a Regex for American-Style Dates
The first part of the program will need to import the necessary modules and create a regex that can identify MM-DD-YYYY dates. The to-do comments will remind you what’s left to write in this program. Typing them as TODO makes them easy to find using IDLE’s CTRL-F find feature. Make your code look like the following:


   #! python3
    # renameDates.py - Renames filenames with American MM-DD-YYYY date format
    # to European DD-MM-YYYY.

❶ import shutil, os, re

    # Create a regex that matches files with the American date format.
❷ datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
❸     """, re.VERBOSE)

    # TODO: Loop over the files in the working directory.

    # TODO: Skip files without a date.

    # TODO: Get the different parts of the filename.

    # TODO: Form the European-style filename.

    # TODO: Get the full, absolute file paths.

    # TODO: Rename the files.
From this chapter, you know the shutil.move() function can be used to rename files: Its arguments are the name of the file to rename and the new filename. Because this function exists in the shutil module, you must import that module ❶.

But before renaming the files, you need to identify which files you want to rename. Filenames with dates such as spam4-4-1984.txt and 01-03-2014eggs.zip should be renamed, while filenames without dates such as littlebrother.epub can be ignored.

You can use a regular expression to identify this pattern. After importing the re module at the top, call re.compile() to create a Regex object ❷. Passing re.VERBOSE for the second argument ❸ will allow whitespace and comments in the regex string to make it more readable.

The regular expression string begins with ^(.*?) to match any text at the beginning of the filename that might come before the date. The ((0|1)?\d) group matches the month. The first digit can be either 0 or 1, so the regex matches 12 for December but also 02 for February. This digit is also optional so that the month can be 04 or 4 for April. The group for the day is ((0|1|2|3)?\d) and follows similar logic; 3, 03, and 31 are all valid numbers for days. (Yes, this regex will accept some invalid dates such as 4-31-2014, 2-29-2013, and 0-15-2014. Dates have a lot of thorny special cases that can be easy to miss. But for simplicity, the regex in this program works well enough.)
While 1885 is a valid year, you can just look for years in the 20th or 21st century. This will keep your program from accidentally matching nondate filenames with a date-like format, such as 10-10-1000.txt.
The (.*?)$ part of the regex will match any text that comes after the date.

# Step 2: Identify the Date Parts from the Filenames
Next, the program will have to loop over the list of filename strings returned from os.listdir() and match them against the regex. Any files that do not have a date in them should be skipped. For filenames that have a date, the matched text will be stored in several variables. Fill in the first three TODOs in your program with the following code:


   #! python3
    # renameDates.py - Renames filenames with American MM-DD-YYYY date format
    # to European DD-MM-YYYY.

   --snip--
```python
   # Loop over the files in the working directory.
   for amerFilename in os.listdir('.'):
       mo = datePattern.search(amerFilename)

       # Skip files without a date.
❶     if mo == None:
❷         continue

❸     # Get the different parts of the filename.
       beforePart = mo.group(1)
       monthPart  = mo.group(2)
       dayPart    = mo.group(4)
       yearPart   = mo.group(6)
       afterPart  = mo.group(8)
```
   --snip--
If the Match object returned from the search() method is None ❶, then the filename in amerFilename does not match the regular expression. The continue statement ❷ will skip the rest of the loop and move on to the next filename.

Otherwise, the various strings matched in the regular expression groups are stored in variables named beforePart, monthPart, dayPart, yearPart, and afterPart ❸. The strings in these variables will be used to form the European-style filename in the next step.

To keep the group numbers straight, try reading the regex from the beginning and count up each time you encounter an opening parenthesis. Without thinking about the code, just write an outline of the regular expression. This can help you visualize the groups. For example:


datePattern = re.compile(r"""^(1) # all text before the date
    (2 (3) )-                     # one or two digits for the month
    (4 (5) )-                     # one or two digits for the day
    (6 (7) )                      # four digits for the year
    (8)$                          # all text after the date
    """, re.VERBOSE)
Here, the numbers 1 through 8 represent the groups in the regular expression you wrote. Making an outline of the regular expression, with just the parentheses and group numbers, can give you a clearer understanding of your regex before you move on with the rest of the program.

# Step 3: Form the New Filename and Rename the Files
As the final step, concatenate the strings in the variables made in the previous step with the European-style date: The date comes before the month. Fill in the three remaining TODOs in your program with the following code:


   #! python3
    # renameDates.py - Renames filenames with American MM-DD-YYYY date format
    # to European DD-MM-YYYY.

   --snip--
```python
       # Form the European-style filename.
❶     euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart +
                      afterPart

       # Get the full, absolute file paths.
       absWorkingDir = os.path.abspath('.')
       amerFilename = os.path.join(absWorkingDir, amerFilename)
       euroFilename = os.path.join(absWorkingDir, euroFilename)

       # Rename the files.
❷     print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
❸     #shutil.move(amerFilename, euroFilename)   # uncomment after testing
```
Store the concatenated string in a variable named euroFilename ❶. Then, pass the original filename in amerFilename and the new euroFilename variable to the shutil.move() function to rename the file ❸.

This program has the shutil.move() call commented out and instead prints the filenames that will be renamed ❷. Running the program like this first can let you double-check that the files are renamed correctly. Then you can uncomment the shutil.move() call and run the program again to actually rename the files.
