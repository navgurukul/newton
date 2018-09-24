```ngMeta
name: Using Breaks
completionMethod: manual
```

![How Break Statements Work!](assets/how-break-statement-works.jpg)
Agar aap yeh diagram dekhoge toh aap samjhoge, ki `break` command se hum jiss bhi loop ke andar aapne woh command likhi hai, uss loop se immediately bahar nikal jaate hai.

Ab iss idea ko use karte hue in example codes ka `dry run` karein.

```python
for val in "navgurukul":
    if val == "g":
        break
    print(val)

print("The end")
```

```python
var = 10
while var > 0:              
   print 'Current variable value :', var
   var = var - 1
   if var == 5:
      break

print "Good bye!"
```

```python
num = 407

i = 2
prime = True
first_divisor = -1
while (i<num):
    if (num%i == 0):
        prime = False
        first_divisor = i
        break
    i += 1

print prime
if not prime:
    print first_divisor
```

### Jab `nested loops` hote hai, toh `break` command se hum uss loop se bahar aate hai, jo immediately pehla loop hota hai jiske `andar` break likha hota hai.

Jaise neeche diye hue program mei `break` statement sirf loop2 se bahar nikalega.

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

```python
for x in range(7):
    if (x == 3 or x==5):
        continue
    print(x)
```

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

