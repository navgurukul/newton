```ngMeta
name: installing-the-openpyxl-module
```
# Installing the openpyxl Module
Python does not come with OpenPyXL, so you’ll have to install it. Follow the instructions for installing third-party modules in Appendix A; the name of the module is openpyxl. To test whether it is installed correctly, enter the following into the interactive shell:

```python
>>> import openpyxl
```
If the module was correctly installed, this should produce no error messages. Remember to import the openpyxl module before running the interactive shell examples in this chapter, or you’ll get a NameError: name 'openpyxl' is not defined error.

This book covers version 2.3.3 of OpenPyXL, but new versions are regularly released by the OpenPyXL team. Don’t worry, though: New versions should stay backward compatible with the instructions in this book for quite some time. If you have a newer version and want to see what additional features may be available to you, you can check out the full documentation for OpenPyXL at <span><a href=" http://openpyxl.readthedocs.org/."> http://openpyxl.readthedocs.org/.</a></span>

# Reading Excel Documents
The examples in this chapter will use a spreadsheet named example.xlsx stored in the root folder. You can either create the spreadsheet yourself or download it from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>. Figure 12-1 shows the tabs for the three default sheets named Sheet1, Sheet2, and Sheet3 that Excel automatically provides for new workbooks. (The number of default sheets created may vary between operating systems and spreadsheet programs.)

<!-- ![image](assets/000024.jpg)
 -->
Figure 12-1. The tabs for a workbook’s sheets are in the lower-left corner of Excel.

Sheet 1 in the example file should look like Table 12-1. (If you didn’t download example.xlsx from the website, you should enter this data into the sheet yourself.)

Table 12-1. The example.xlsx Spreadsheet

 	
A

B

C

1

4/5/2015 1:34:02 PM

Apples

73

2

4/5/2015 3:41:23 AM

Cherries

85

3

4/6/2015 12:46:51 PM

Pears

14

4

4/8/2015 8:59:43 AM

Oranges

52

5

4/10/2015 2:07:00 AM

Apples

152

6

4/10/2015 6:10:37 PM

Bananas

23

7

4/10/2015 2:40:46 AM

Strawberries

98

Now that we have our example spreadsheet, let’s see how we can manipulate it with the openpyxl module.

