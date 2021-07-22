```ngMeta
reading-data-from-reader-objects-in-a-for-loop_key1
```

reading-data-from-reader-objects-in-a-for-loop_key2
reading-data-from-reader-objects-in-a-for-loop_key3


```python
>>> import csv
>>> exampleFile = open('example.csv')
>>> exampleReader = csv.reader(exampleFile)
>>> for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
```
reading-data-from-reader-objects-in-a-for-loop_key4


reading-data-from-reader-objects-in-a-for-loop_key5


reading-data-from-reader-objects-in-a-for-loop_key6
