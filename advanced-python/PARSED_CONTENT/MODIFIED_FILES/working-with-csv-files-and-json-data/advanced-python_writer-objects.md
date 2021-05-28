```ngMeta
writer-objects_key1
```
# writer-objects_key2
writer-objects_key3

```python
   >>> import csv
❶ >>> outputFile = open('output.csv', 'w', newline='')
❷ >>> outputWriter = csv.writer(outputFile)
   >>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
```
writer-objects_key4```python
   >>> outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
```
writer-objects_key5```python
   >>> outputWriter.writerow([1, 2, 3.141592, 4])
```
writer-objects_key6```python
   >>> outputFile.close()
```
writer-objects_key7

writer-objects_key8

writer-objects_key9

writer-objects_key10

writer-objects_key11


writer-objects_key12

