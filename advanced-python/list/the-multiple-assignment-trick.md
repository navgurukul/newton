```ngMeta
name: the-multiple-assignment-trick
```
# The Multiple Assignment Trick
The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code. So instead of doing this:

```python
>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
```
you could type this line of code:

```python
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition = cat
```
The number of variables and the length of the list must be exactly equal, or Python will give you a ValueError:

```python
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition, name = cat
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    size, color, disposition, name = cat
ValueError: need more than 3 values to unpack
```
The multiple assignment trick can also be used to swap the values in two variables:
```python
>>> a, b = 'Alice', 'Bob'
>>> a, b = b, a
>>> print(a)
'Bob'
>>> print(b)
'Alice'
```