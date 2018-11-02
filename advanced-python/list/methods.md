```ngMeta
name: methods
completionMethod: manual
```
# Methods
A method is the same thing as a function, except it is “called on” a value. For example, if a list value were stored in spam, you would call the index() list method (which I’ll explain next) on that list like so: spam.index('hello'). The method part comes after the value, separated by a period.

Each data type has its own set of methods. The list data type, for example, has several useful methods for finding, adding, removing, and otherwise manipulating values in a list.

# Finding a Value in a List with the index() Method
List values have an index() method that can be passed a value, and if that value exists in the list, the index of the value is returned. If the value isn’t in the list, then Python produces a ValueError error. Enter the following into the interactive shell:

```python
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('howdy howdy howdy')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    spam.index('howdy howdy howdy')
ValueError: 'howdy howdy howdy' is not in list
```
When there are duplicates of the value in the list, the index of its first appearance is returned. Enter the following into the interactive shell, and notice that index() returns 1, not 3:

```python
>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
>>> spam.index('Pooka')
1
```
# Adding Values to Lists with the append() and insert() Methods
To add new values to a list, use the append() and insert() methods. Enter the following into the interactive shell to call the append() method on a list value stored in the variable spam:

```python
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
```
The previous append() method call adds the argument to the end of the list. The insert() method can insert a value at any index in the list. The first argument to insert() is the index for the new value, and the second argument is the new value to be inserted. Enter the following into the interactive shell:

```python
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
```
Notice that the code is spam.append('moose') and spam.insert(1, 'chicken'), not spam = spam.append('moose') and spam = spam.insert(1, 'chicken'). Neither append() nor insert() gives the new value of spam as its return value. (In fact, the return value of append() and insert() is None, so you definitely wouldn’t want to store this as the new variable value.) Rather, the list is modified in place. Modifying a list in place is covered in more detail later in Mutable and Immutable Data Types.

Methods belong to a single data type. The append() and insert() methods are list methods and can be called only on list values, not on other values such as strings or integers. Enter the following into the interactive shell, and note the AttributeError error messages that show up:

```python
>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> bacon = 42
>>> bacon.insert(1, 'world')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    bacon.insert(1, 'world')
AttributeError: 'int' object has no attribute 'insert'
```

