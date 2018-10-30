```ngMeta
name: the-csv-module
completionMethod: manual
```
# The CSV Module
Each line in a CSV file represents a row in the spreadsheet, and commas separate the cells in the row. For example, the spreadsheet example.xlsx from <span><a href="http://nostarch.com/automatestuff/ ">http://nostarch.com/automatestuff/ </a></span> would look like this in a CSV file:


4/5/2015 13:34,Apples,73
4/5/2015 3:41,Cherries,85
4/6/2015 12:46,Pears,14
4/8/2015 8:59,Oranges,52
4/10/2015 2:07,Apples,152
4/10/2015 18:10,Bananas,23
4/10/2015 2:40,Strawberries,98
I will use this file for this chapter’s interactive shell examples. You can download example.csv from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> or enter the text into a text editor and save it as example.csv.

CSV files are simple, lacking many of the features of an Excel spreadsheet. For example, CSV files

Don’t have types for their values—everything is a string

Don’t have settings for font size or color

Don’t have multiple worksheets

Can’t specify cell widths and heights

Can’t have merged cells

Can’t have images or charts embedded in them

The advantage of CSV files is simplicity. CSV files are widely supported by many types of programs, can be viewed in text editors (including IDLE’s file editor), and are a straightforward way to represent spreadsheet data. The CSV format is exactly as advertised: It’s just a text file of comma-separated values.

Since CSV files are just text files, you might be tempted to read them in as a string and then process that string using the techniques you learned in Chapter 8. For example, since each cell in a CSV file is separated by a comma, maybe you could just call the split() method on each line of text to get the values. But not every comma in a CSV file represents the boundary between two cells. CSV files also have their own set of escape characters to allow commas and other characters to be included as part of the values. The split() method doesn’t handle these escape characters. Because of these potential pitfalls, you should always use the csv module for reading and writing CSV files.

