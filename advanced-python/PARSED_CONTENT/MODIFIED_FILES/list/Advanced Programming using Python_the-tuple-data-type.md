```ngMeta
the-tuple-data-type_key1
```

the-tuple-data-type_key2
the-tuple-data-type_key3


```python
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'
>>> eggs[1:3]
(42, 0.5)
>>> len(eggs)
3
```
the-tuple-data-type_key4


```python
>>> eggs = ('hello', 42, 0.5)
>>> eggs[1] = 99
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    eggs[1] = 99
TypeError: 'tuple' object does not support item assignment
```
the-tuple-data-type_key5


```python
>>> type(('hello',))
```
the-tuple-data-type_key6
```python
>>> type(('hello'))
```
the-tuple-data-type_key7
