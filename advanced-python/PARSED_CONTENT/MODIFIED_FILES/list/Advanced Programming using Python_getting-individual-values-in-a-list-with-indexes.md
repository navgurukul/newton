getting-individual-values-in-a-list-with-indexes_key1
getting-individual-values-in-a-list-with-indexes_key2


getting-individual-values-in-a-list-with-indexes_key3


getting-individual-values-in-a-list-with-indexes_key4


```python
   >>> spam = ['cat', 'bat', 'rat', 'elephant']
   >>> spam[0]
   'cat'
   >>> spam[1]
   'bat'
   >>> spam[2]
   'rat'
   >>> spam[3]
   'elephant'
   >>> ['cat', 'bat', 'rat', 'elephant'][3]
   'elephant'
❶ >>> 'Hello ' + spam[0]
❷ 'Hello cat'
   >>> 'The ' + spam[1] + ' ate the ' + spam[0] + '.'
   'The bat ate the cat.'
```
getting-individual-values-in-a-list-with-indexes_key5


getting-individual-values-in-a-list-with-indexes_key6


```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[10000]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    spam[10000]
IndexError: list index out of range
```
getting-individual-values-in-a-list-with-indexes_key7


```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1]
'bat'
>>> spam[1.0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    spam[1.0]
TypeError: list indices must be integers, not float
>>> spam[int(1.0)]
'bat'
Lists can also contain other list values. The values in these lists of lists can be accessed using multiple indexes, like so:


>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50
```
getting-individual-values-in-a-list-with-indexes_key8
