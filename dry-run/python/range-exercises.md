```ngMeta
name: Exercises on Range
```

<!-- fixme: wrong example -->
<!-- ```python
my_string = 'Hello world'
for i in range(len(my_string)):
    my_string[i].upper()
print (my_string)
``` -->

<!-- TODO: Put this as an edge case -->

<!-- ```python
my_string = 'hello world'
for i in range(len(my_string)):
    print (my_string)
    my_string = 'ng' -->

<!-- todo: introduce range properly -->
```python
list1 = range(100, 110)
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
	if i != "s":
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
x = 12
y = 18
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

**Hints**: HCF

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

```python
for i in range(5): #loop1
    for j in range(10): #loop2
        if (j > 3): 
            break 
        else:
            print "*", 
    print ''
```
Iss program ka `output` likh kar, iss program ko bina `break` statement ke likhiye.
Apne likhe hue naye program ka bhi `dry run` karein.

```python
for a in range(6):
    for b in range(6):
        if (a == b):
            break
        print '*',
    print ''
```
Iss program ka `output` likh kar, iss program ko bina `break` statement ke likhiye.
Apne likhe hue naye program ka bhi `dry run` karein.

```python
def a(l):
    al = len(l)
    for ( i in range()/2 ):
        l[i] = a[al-i]


example = [3, 9, 1, 2, 7]
a(example)
print example
```

Yeh question karte waqt, aap uppar wale example ka dhyaan rakhiye.
```python
def partition(l, s, e):
    pos = s
    for i in range(s, e):
        if l[i] < l[e]:
            l[i],l[pos] = l[pos],l[i]
            pos += 1

    l[pos],l[e] = l[e],l[pos]
    return pos

def so(l, s, e):
    if s < e:
        pos = partition(l, s, e)
        so(l, s, pos - 1)
        so(l, pos + 1, e)

example = [3, 9, 1, 2, 7]
so(example, 0, len(example) - 1)
print example
```

```python
def so(l):
    for i in range(len(l)-1):
        n = l[i]
        if l[i+1] < n:
            l[i] = l[i+1]
            l[i+1] = n
            so(l)
    return l
 
l = [9, 2, 7, 5]
so(l)
 
print l
```