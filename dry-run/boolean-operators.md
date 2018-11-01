```ngMeta
name: Variables - Boolean operators ki Understanding
completionMethod: manual
```

Aap booleans ke liye yaha se concepts revise kar sakte ho - http://saral.navgurukul.org/course?id=18&slug=python__logical-operators%2Flogical-operators-intro

Ab inn exercises ka dry run karo - http://saral.navgurukul.org/course?id=18&slug=python__logical-operators%2Flogical-operators-question1

<!-- TODO Aap iss video ko dekhein. -->

```python
x = True
y = False
z = x and y
a = x or y
b = not a
c = not (a and b)
d = not (a or b)
e = (a and b) or (c or d)
```

```python
if (4 >= 4) and (6 == 5):
	print "Yes"
else:
	print "No"
```

```python
x = 7
print not(((x > 4) and (x < 6)) or (x == 9))
```
Yeh programs inn values ke liye bhi karo
```python
x = 5
```

```python
x = 9
```

```python
x = 7
y = 3
print not(((x > 4) and (x < 6)) or (x == y))
```

Yeh program inn values ke liye bhi karo
```python
x = 5
y = 5
```

```python
x = 8
y = 4
print not (((x>4) and (x<6)) or (x==y))
```
Iska solution verify ya samajhne k liye aap yeh [video](https://www.youtube.com/watch?v=1G9UY3yrkWw) dekh sakte ho.
