```ngMeta
name: opening-excel-documents-with-openpyxl
completionMethod: manual
```
# Opening Excel Documents with OpenPyXL
Once you’ve imported the openpyxl module, you’ll be able to use the openpyxl.load_workbook() function. Enter the following into the interactive shell:

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> type(wb)
```
<class 'openpyxl.workbook.workbook.Workbook'>
The openpyxl.load_workbook() function takes in the filename and returns a value of the workbook data type. This Workbook object represents the Excel file, a bit like how a File object represents an opened text file.

Remember that example.xlsx needs to be in the current working directory in order for you to work with it. You can find out what the current working directory is by importing os and using os.getcwd(), and you can change the current working directory using os.chdir().