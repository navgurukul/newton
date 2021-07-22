```ngMeta
removing-values-from-lists-with-remove()_key1
```

removing-values-from-lists-with-remove()_key2
removing-values-from-lists-with-remove()_key3


```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
```
removing-values-from-lists-with-remove()_key4


```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('chicken')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    spam.remove('chicken')
ValueError: list.remove(x): x not in list
```
removing-values-from-lists-with-remove()_key5


```python
>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
```
removing-values-from-lists-with-remove()_key6
