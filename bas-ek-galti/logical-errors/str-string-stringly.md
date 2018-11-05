```python
def add_string(str1):
  length = len(str1)

  if length < 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'
  return str1


print(add_string('ab'))
'OUTPUT: ab'
print(add_string('abc'))
'OUTPUT: abcing'
print(add_string('abcing'))
'OUTPUT: abcingly'
```

```python
def add_string(str1):
  length = len(str1)

  if length < 2:
    if str1[-3:] == 'ing':
      str1 = 'ly'
    else:
      str1 = 'ing'
  return str1


print(add_string('ab'))
'OUTPUT: ab'
print(add_string('abc'))
'OUTPUT: abcing'
print(add_string('abcing'))
'OUTPUT: abcingly'
```
