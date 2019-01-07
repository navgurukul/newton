```ngMeta
name: the-delimiter-and-lineterminator-keyword-arguments
```
# The delimiter and lineterminator Keyword Arguments
Say you want to separate cells with a tab character instead of a comma and you want the rows to be double-spaced. You could enter something like the following into the interactive shell:

```python
   >>> import csv
   >>> csvFile = open('example.tsv', 'w', newline='')
❶ >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
   >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
```
   24
```python
   >>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
   17
   >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
```
   32
```python
   >>> csvFile.close()
```
This changes the delimiter and line terminator characters in your file. The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline. You can change characters to different values by using the delimiter and lineterminator keyword arguments with csv.writer().

Passing delimeter='\t' and lineterminator='\n\n' ❶ changes the character between cells to a tab and the character between rows to two newlines. We then call writerow() three times to give us three rows.

This produces a file named example.tsv with the following contents:


apples  oranges grapes

eggs    bacon   ham
spam    spam    spam    spam    spam    spam
Now that our cells are separated by tabs, we’re using the file extension .tsv, for tab-separated values.