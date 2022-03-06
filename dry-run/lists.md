03```ngMeta
name: Lists
```

```python
a = [32, 23, 46, 19, 90, 12, 23, 95, 100, 1]

l = len(a)
while (i < l/2):
    a[i] = a[l-i]

print a
```

Yeh `program` kya karta hai, yeh acche se samjhe aur code karne ke style ko bhi samjhein.


```python
a = [32, 23, 46, 19, 90, 12, 23, 95, 100, 1]
l = len(a)
i = 0
s = 0
m1 = a[0]
m2 = a[0]
while (i < l):
    s += a[i]
    if a[i] > m1:
        m1 = a[i]
    if a[i] < m1:
        m2 = a[i]
    i = i + 1
print s, m1, m2
```

Yeh `program` kya karta hai, yeh acche se samjhein. Iss program ko dobara bina dekhe **proper variable names** ke saath, bina dekhein likhnein ki koshish karein.
