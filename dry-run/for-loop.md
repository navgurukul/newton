```ngMeta
name: For Loops
completionMethod: manual
```

Yeh [video](https://www.youtube.com/watch?v=nh2mdtFrpl4) dekh kar aap for loop ko ek baar samjhein.
Iss video dekhne ke baad iss program ka dry run phir se karein. 
```python
for i in range(4):
    for j in range(i):
        print x,
    print ''
```

Phir Yeh:
```python
for i in range(4):
    for j in range(4):
        if j<i:
            print x,
    print ''
```

Ab Yeh:
```python
for i in range(4):
    for j in range(4):
        if j>i:
            print x,
    print ''
```

Saath saath samjhiye, ki kya badalne se kya badal raha hai.

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
sum_var = 0
for x in [0, 1, 2, 3]:
    if n % (x+1) == 0:
        sum_var += x
print sum_var
```

Alag alag `n` ki values ke saath iss program ko `dry run` kar kar samjhein ki `for` loop kaise kaam karta hai.
### Dhyaan rakhiye, ki hum variable ka naam `sum` nahi rakh sakte hai. Kyuki woh python ka reserved keyword hai.

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
Iss question ko solve karne ke baad aap [yaha](https://youtu.be/FwCrNOCz8pM) se iska solution verify kar sakte hai.

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

```python
for x in range(7):
    if (x == 3 or x==5):
        continue
    print(x)
```
Iska solution verify ya samajhne k liye aap yeh [video](https://www.youtube.com/watch?v=FHpxgqGDZhM) dekh sakte ho.

```python
for x in range (10,20):
    if (x == 15):
        break
    if (x % 2 == 0):
        continue
    print x
```

```python
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num
```
Iss program ko `execute` karo. Iss program ko bina `continue` statement ke dobara likho.

```python
for i in range(5):
    for j in range(5):
        if (j>2):
            break
        else:
            print 'x',
    print ''
```
Iska solution verify ya samajhne k liye aap yeh [video](https://www.youtube.com/watch?v=5s2Uo9333Mo) ya yeh [video](https://www.youtube.com/watch?v=pXbIsbvmKLQ) dekh sakte ho. Kaunsi video aapko jyada clear lagi?

```python
for a in range(4):
    for b in range(4):
        if (a==b):
            break
        print 'x',
    print ''
```
Iska solution verify ya samajhne k liye aap yeh [video](https://www.youtube.com/watch?v=pXbIsbvmKLQ) dekh sakte ho.

```python
for val in "navgurukul":
    if val == "g":
        break
    print(val)

print("The end")
```

**Hints**
- h - HCF nikalne ke liye hai.
