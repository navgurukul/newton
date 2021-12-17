```ngMeta
name: Counter Examples
```

## `Counter Examples`

In this section, some examples are given. You need to understand these examples very carefully, to figure out how they work? You have to do a `dry run` of each of the examples and notice that how the dry run works.

You can also add some more examples as comments so that your, as well as your peer's concept, becomes clear.


#### Example 1

You have to print multiples of 3 from 1 to 40. While writing the code keep in mind that the counter starts from 891.

#### Solution to Example 1
```python
i = 891
while i < 931:
  z = i - 890
  if z % 3 == 0:
    print(z)
  i = i + 1
```

#### Example 2

Write a code to print all the multiples of 5 from 1 to 50. But you don't need to use % (modulus operator). Do without it.

#### Solution to Example 2
```python
i = 0
while i <= 50:
  if i != 0:
    print(i)
  i = i + 5
```


#### Example 3

Print all the odd numbers between 50 to 100.

#### Solution 1 to Example 3

```python
i = 49
while i <= 98:
  i = i + 2
  print(i)
```

### Solution 2 to Example 3
```python
i = 50
while i <= 100:
  if i % 2 != 0:
    print(i)
  i = i + 1
```

### Solution 3 to Example 3
```python
i = 400
while i >= 350:
  z = i - 300
  if z % 2 != 0:
      print(z)
  i = i - 1
```
## Example 4

Print the numbers from 1 to 10 without using increment.

### Solution 1 to Example 4
```python
a = -1
while a >= (-10):
  print(-a)
  a = a -1
```

### Solution 2 to Example 4
```python
a = 1 
while a <= 10:
  print (a)
  a = a-(-1)
```

### Solution 3 to Example 4
```python
a = 1
while a !=11:
  print(a)
  a-=-1
```



