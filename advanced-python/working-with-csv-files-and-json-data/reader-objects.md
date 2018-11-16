```ngMeta
name: reader-objects
completionMethod: manual
```
# Reader Objects
To read data from a CSV file with the csv module, you need to create a Reader object. A Reader object lets you iterate over lines in the CSV file. Enter the following into the interactive shell, with example.csv in the current working directory:

```python
❶ >>> import csv
❷ >>> exampleFile = open('example.csv')
❸ >>> exampleReader = csv.reader(exampleFile)
❹ >>> exampleData = list(exampleReader)
❹ >>> exampleData
```
   [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
   ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
   ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
   ['4/10/2015 2:40', 'Strawberries', '98']]
The csv module comes with Python, so we can import it ❶ without having to install it first.

To read a CSV file with the csv module, first open it using the open() function ❷, just as you would any other text file. But instead of calling the read() or readlines() method on the File object that open() returns, pass it to the csv.reader() function ❸. This will return a Reader object for you to use. Note that you don’t pass a filename string directly to the csv.reader() function.

The most direct way to access the values in the Reader object is to convert it to a plain Python list by passing it to list() ❹. Using list() on this Reader object returns a list of lists, which you can store in a variable like exampleData. Entering exampleData in the shell displays the list of lists ❺.

Now that you have the CSV file as a list of lists, you can access the value at a particular row and column with the expression exampleData[row][col], where row is the index of one of the lists in exampleData, and col is the index of the item you want from that list. Enter the following into the interactive shell:

```python
>>> exampleData[0][0]
```
'4/5/2015 13:34'
```python
>>> exampleData[0][1]
```
'Apples'
```python
>>> exampleData[0][2]
```
'73'
```python
>>> exampleData[1][1]
```
'Cherries'
```python
>>> exampleData[6][1]
```
'Strawberries'
exampleData[0][0] goes into the first list and gives us the first string, exampleData[0][2] goes into the first list and gives us the third string, and so on.