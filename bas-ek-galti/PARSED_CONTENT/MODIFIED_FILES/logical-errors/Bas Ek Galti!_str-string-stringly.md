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
print(add_string('abc'))
print(add_string('abcing'))
```
str-string-stringly_key1
str-string-stringly_key2
str-string-stringly_key3
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
print(add_string('abc'))
print(add_string('abcing'))
```
str-string-stringly_key4
str-string-stringly_key5
str-string-stringly_key6
