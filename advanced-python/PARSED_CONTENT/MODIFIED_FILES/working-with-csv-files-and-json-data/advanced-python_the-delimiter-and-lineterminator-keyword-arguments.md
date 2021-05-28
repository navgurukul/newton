```ngMeta
the-delimiter-and-lineterminator-keyword-arguments_key1
```
# the-delimiter-and-lineterminator-keyword-arguments_key2
the-delimiter-and-lineterminator-keyword-arguments_key3

```python
   >>> import csv
   >>> csvFile = open('example.tsv', 'w', newline='')
❶ >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
   >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
```
the-delimiter-and-lineterminator-keyword-arguments_key4```python
   >>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
   17
   >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
```
the-delimiter-and-lineterminator-keyword-arguments_key5```python
   >>> csvFile.close()
```
the-delimiter-and-lineterminator-keyword-arguments_key6

the-delimiter-and-lineterminator-keyword-arguments_key7

the-delimiter-and-lineterminator-keyword-arguments_key8


the-delimiter-and-lineterminator-keyword-arguments_key9

the-delimiter-and-lineterminator-keyword-arguments_key10