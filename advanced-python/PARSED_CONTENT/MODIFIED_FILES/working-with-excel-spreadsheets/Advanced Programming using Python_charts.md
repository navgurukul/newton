charts_key1
charts_key2


charts_key3


charts_key4


charts_key5


charts_key6


charts_key7


charts_key8


charts_key9


charts_key10


charts_key11


charts_key12


![image](assets/000047.jpg)
charts_key13


charts_key14


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

![image](assets/000028.jpg)
charts_key15


charts_key16


charts_key17


charts_key18
charts_key19


charts_key20


charts_key21
