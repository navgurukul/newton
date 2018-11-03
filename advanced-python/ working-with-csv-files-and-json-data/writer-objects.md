```ngMeta
name: writer-objects
completionMethod: manual
```
# Writer Objects
A Writer object lets you write data to a CSV file. To create a Writer object, you use the csv.writer() function. Enter the following into the interactive shell:

```python
   >>> import csv
❶ >>> outputFile = open('output.csv', 'w', newline='')
❷ >>> outputWriter = csv.writer(outputFile)
   >>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
```
   21
```python
   >>> outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
```
   32
```python
   >>> outputWriter.writerow([1, 2, 3.141592, 4])
```
   16
```python
   >>> outputFile.close()
```
First, call open() and pass it 'w' to open a file in write mode ❶. This will create the object you can then pass to csv.writer() ❷ to create a Writer object.

On Windows, you’ll also need to pass a blank string for the open() function’s newline keyword argument. For technical reasons beyond the scope of this book, if you forget to set the newline argument, the rows in output.csv will be double-spaced, as shown in Figure 14-1.

<!-- ![image](assets/000067.png)
 -->
Figure 14-1. If you forget the newline='' keyword argument in open(), the CSV file will be double-spaced.

The writerow() method for Writer objects takes a list argument. Each value in the list is placed in its own cell in the output CSV file. The return value of writerow() is the number of characters written to the file for that row (including newline characters).

This code produces an output.csv file that looks like this:


spam,eggs,bacon,ham
"Hello, world!",eggs,bacon,ham
1,2,3.141592,4
Notice how the Writer object automatically escapes the comma in the value 'Hello, world!' with double quotes in the CSV file. The csv module saves you from having to handle these special cases yourself.

