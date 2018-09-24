```ngMeta
name: For Loops
completionMethod: manual
```

```python
a = 1
b = 1
for i in [0, 1, 2, 3, 4, 5, 6]:
    c = a + b
    b = a
    a = c

print c
```

Alag alag `n` ki values ke saath iss program ko `dry run` kar kar samjhein ki `for` loop kaise kaam karta hai.



```python
sum = 0
for x in [0, 1, 2, 3]:
    if n % (x+1) == 0:
        sum += x
print sum
```

Alag alag `n` ki values ke saath iss program ko `dry run` kar kar samjhein ki `for` loop kaise kaam karta hai.

```python
string = "she sells sea shells"
count = 0
for i in string:
	if i != 's':
		count+=1
print s
```
Yeh program kya karta hai, yeh samjhiye. Aapko bhi aise code likhna seekhna hai.

```python
a = [2,3,4,5,5,3,2,2]
b=[]
for i in a:
	if i not in b:
		b.append(i)

print b
```
Yeh program kya karta hai, yeh samjhiye. Aapko bhi aise code likhna seekhna hai.

```python
x = 100
y = 120
if x > y:
    smaller = y
else:
    smaller = x
i = 1
while(i <= smaller):
    if ( (x % i == 0) and (y % i == 0) ):
        h = i
    i = i + 1
print h
```
Yeh program kya karta hai? Kya aapne aise kisi cheez ki baarein mei school mei padha hai? Hints last mei diye hue hai.

Neeche diye hue program mei, `print` ke baad `,` daalne se nayi line print nahi hoti. Aur `print ''` se new line print hoti hai.
```python
for i in [0, 1, 2, 3, 4] :
    for j in [0, 1, 2, 3, 4] :
        if i==j:
            print 0,
        else:
            print "x",
    print ''
```

```python
for i in [0, 1, 2, 3, 4] :
    for j in [0, 1, 2, 3, 4] :
        if (i==j) or (i+j==n-1):
            print 'x'
        else:
            print '0'
    print ''
```

```python
for i in [0, 1, 2, 3]:
    j = 0
    while(j<i):
        print 'x',
        j = j + 1
    print ''
```

**Hints**
- h - HCF nikalne ke liye hai.