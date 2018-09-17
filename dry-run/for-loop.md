```ngMeta
name: For Loops
completionMethod: manual
```

```python
a = 1
b = 1
n = 7
for i in range(n):
    c = a + b
    b = a
    a = c

print c
```

Alag alag `n` ki values ke saath iss program ko `dry run` kar kar samjhein ki `range` aur `for` loop kaise kaam karta hai.



```python
n = 5
sum = 0
for x in range(n):
    if n % (x+1) == 0:
        sum += x
print sum
```

Alag alag `n` ki values ke saath iss program ko `dry run` kar kar samjhein ki `range` aur `for` loop kaise kaam karta hai.

```python
string = "she sells sea shells"
count = 0
for i in string:
	if i != s:
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

for i in range(1, smaller+1):
    if ( (x % i == 0) and (y % i == 0) ):
        h = i

print h
```
Yeh program kya karta hai? Kya aapne aise kisi cheez ki baarein mei school mei padha hai? Hints last mei diye hue hai.

Neeche diye hue program mei, `print` ke baad `,` daalne se nayi line print nahi hoti. Aur `print ''` se new line print hoti hai.
```python
n=5
for i in range(5) :
    for j in range(5) :
        if i==j:
            print 0,
        else:
            print "x",
    print ''
```

```python
n=5
for i in range(n) :
    for j in range(n) :
        if (i==j) or (i+j==n-1):
            print 'x'
        else:
            print '0'
    print ''
```

```python
n = 4
for i in range(4):
    for j in range(i):
        print 'x',
    print ''
```

**Hints**
- h - HCF nikalne ke liye hai.