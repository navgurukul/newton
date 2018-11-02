```ngMeta
name: sorting-the-values-in-a-list-with-the-sort()-method
completionMethod: manual
```
# Sorting the Values in a List with the sort() Method
Lists of number values or lists of strings can be sorted with the sort() method. For example, enter the following into the interactive shell:

```python
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
```
You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order. Enter the following into the interactive shell:

```python
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
```
There are three things you should note about the sort() method. First, the sort() method sorts the list in place; don’t try to capture the return value by writing code like spam = spam.sort().

Second, you cannot sort lists that have both number values and string values in them, since Python doesn’t know how to compare these values. Type the following into the interactive shell and notice the TypeError error:

```python
>>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
 File "<pyshell#70>", line 1, in <module>
   spam.sort()
TypeError: unorderable types: str() < int()
```
Third, sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings. This means uppercase letters come before lowercase letters. Therefore, the lowercase a is sorted so that it comes after the uppercase Z. For an example, enter the following into the interactive shell:

```python
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```
If you need to sort the values in regular alphabetical order, pass str. lower for the key keyword argument in the sort() method call.

```python
>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']
```
This causes the sort() method to treat all the items in the list as if they were lowercase without actually changing the values in the list.

# Example Program: Magic 8 Ball with a List
Using lists, you can write a much more elegant version of the previous chapter’s Magic 8 Ball program. Instead of several lines of nearly identical elif statements, you can create a single list that the code works with. Open a new file editor window and enter the following code. Save it as magic8Ball2.py.

```python
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
```
Exceptions to Indentation Rules in Python

In most cases, the amount of indentation for a line of code tells Python what block it is in. There are some exceptions to this rule, however. For example, lists can actually span several lines in the source code file. The indentation of these lines do not matter; Python knows that until it sees the ending square bracket, the list is not finished. For example, you can have code that looks like this:

```python
spam = ['apples',
    'oranges',
                     'bananas',
'cats']
print(spam)
```
Of course, practically speaking, most people use Python’s behavior to make their lists look pretty and readable, like the messages list in the Magic 8 Ball program.

You can also split up a single instruction across multiple lines using the \ line continuation character at the end. Think of \ as saying, “This instruction continues on the next line.” The indentation on the line after a \ line continuation is not significant. For example, the following is valid Python code:

```python
print('Four score and seven ' + \
      'years ago...')
```
These tricks are useful when you want to rearrange long lines of Python code to be a bit more readable.

When you run this program, you’ll see that it works the same as the previous magic8Ball.py program.

Notice the expression you use as the index into messages: random.randint(0, len(messages) - 1). This produces a random number to use for the index, regardless of the size of messages. That is, you’ll get a random number between 0 and the value of len(messages) - 1. The benefit of this approach is that you can easily add and remove strings to the messages list without changing other lines of code. If you later update your code, there will be fewer lines you have to change and fewer chances for you to introduce bugs.

