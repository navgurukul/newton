lists_key1lists_key2`program`lists_key3


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
lists_key4`program`lists_key5**lists_key6**lists_key7