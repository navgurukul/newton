```ngMeta
name: charts
```
# Charts
OpenPyXL supports creating bar, line, scatter, and pie charts using the data in a sheet’s cells. To make a chart, you need to do the following:

Create a Reference object from a rectangular selection of cells.

Create a Series object by passing in the Reference object.

Create a Chart object.

Append the Series object to the Chart object.

Add the Chart object to the Worksheet object, optionally specifying which cell the top left corner of the chart should be positioned..

The Reference object requires some explaining. Reference objects are created by calling the openpyxl.chart.Reference() function and passing three arguments:

The Worksheet object containing your chart data.

A tuple of two integers, representing the top-left cell of the rectangular selection of cells containing your chart data: The first integer in the tuple is the row, and the second is the column. Note that 1 is the first row, not 0.

A tuple of two integers, representing the bottom-right cell of the rectangular selection of cells containing your chart data: The first integer in the tuple is the row, and the second is the column.

Figure 12-9 shows some sample coordinate arguments.

<!-- ![image](assets/000047.jpg)
 -->
Figure 12-9. From left to right: (1, 1), (10, 1); (3, 2), (6, 4); (5, 3), (5, 3)

Enter this interactive shell example to create a bar chart and add it to the spreadsheet:

```python
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> sheet = wb.active
>>> for i in range(1, 11):         # create some data in column A
        sheet['A' + str(i)] = i

>>> refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

>>> seriesObj = openpyxl.chart.Series(refObj, title='First series')

>>> chartObj = openpyxl.chart.BarChart()
>>> chartObj.title = 'My Chart'
>>> chartObj.append(seriesObj)
>>> sheet.add_chart(chartObj, 'C5')
>>> wb.save('sampleChart.xlsx')
This produces a spreadsheet that looks like Figure 12-10.
```

<!-- ![image](assets/000028.jpg)
 -->
Figure 12-10. A spreadsheet with a chart added

We’ve created a bar chart by calling openpyxl.chart.BarChart(). You can also create line charts, scatter charts, and pie charts by calling openpyxl.chart.LineChart(), openpyxl.chart.ScatterChart(), and openpyxl.chart.PieChart().

Unfortunately, in the current version of OpenPyXL (2.3.3), the load_workbook() function does not load charts in Excel files. Even if the Excel file has charts, the loaded Workbook object will not include them. If you load a Workbook object and immediately save it to the same .xlsx filename, you will effectively remove the charts from it.

# Summary
Often the hard part of processing information isn’t the processing itself but simply getting the data in the right format for your program. But once you have your spreadsheet loaded into Python, you can extract and manipulate its data much faster than you could by hand.

You can also generate spreadsheets as output from your programs. So if colleagues need your text file or PDF of thousands of sales contacts transferred to a spreadsheet file, you won’t have to tediously copy and paste it all into Excel.

Equipped with the openpyxl module and some programming knowledge, you’ll find processing even the biggest spreadsheets a piece of cake.