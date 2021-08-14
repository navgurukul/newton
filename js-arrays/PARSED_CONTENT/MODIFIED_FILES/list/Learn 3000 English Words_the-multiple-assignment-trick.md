the-multiple-assignment-trick_key1
the-multiple-assignment-trick_key2


```python
>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
```
the-multiple-assignment-trick_key3


```python
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition = cat
```
the-multiple-assignment-trick_key4


```python
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition, name = cat
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    size, color, disposition, name = cat
ValueError: need more than 3 values to unpack
```
the-multiple-assignment-trick_key5
```python
>>> a, b = 'Alice', 'Bob'
>>> a, b = b, a
>>> print(a)
'Bob'
>>> print(b)
'Alice'
```