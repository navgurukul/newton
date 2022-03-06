```ngMeta
name: keyword-arguments-and-print()
```
# Keyword Arguments and print()
Most arguments are identified by their position in the function call. For example, random.randint(1, 10) is different from random.randint(10, 1). The function call random.randint(1, 10) will return a random integer between 1 and 10, because the first argument is the low end of the range and the second argument is the high end (while random.randint(10, 1) causes an error).

However, keyword arguments are identified by the keyword put before them in the function call. Keyword arguments are often used for optional parameters. For example, the print() function has the optional parameters end and sep to specify what should be printed at the end of its arguments and between its arguments (separating them), respectively.

If you ran the following program:


print('Hello')
print('World')
the output would look like this:


Hello
World
The two strings appear on separate lines because the print() function automatically adds a newline character to the end of the string it is passed. However, you can set the end keyword argument to change this to a different string. For example, if the program were this:


print('Hello', end='')
print('World')
the output would look like this:


HelloWorld
The output is printed on a single line because there is no longer a new-line printed after 'Hello'. Instead, the blank string is printed. This is useful if you need to disable the newline that gets added to the end of every print() function call.

Similarly, when you pass multiple string values to print(), the function will automatically separate them with a single space. Enter the following into the interactive shell:

```python
>>> print('cats', 'dogs', 'mice')
```
cats dogs mice
But you could replace the default separating string by passing the sep keyword argument. Enter the following into the interactive shell:

```python
>>> print('cats', 'dogs', 'mice', sep=',')
```
cats,dogs,mice
You can add keyword arguments to the functions you write as well, but first you’ll have to learn about the list and dictionary data types in the next two chapters. For now, just know that some functions have optional keyword arguments that can be specified when the function is called.