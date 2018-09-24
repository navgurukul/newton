```ngMeta
name: While Loops
completionMethod: manual
```

```python
n = 6
s = 0
i = 1

while i <= n:
    s = s + i
    i = i + 1

print s
```

`while` ke saath `else` ka bhi use ho sakta hai. Jab `while` loop khatam ho jata hai, toh `else` wala code execute hota hai. Yeh trick kaafi baar useful hoti hai.

```python
c = 0

while c < 3:
    print "Loop Ke Andar"
    c = c + 1
else:
    print "Loop Khatam, Hajmola Hajam, Ab Else Ki Baari hai"
```

```python
num = 407

i = 2
while (i<num):
    if (num%i == 0):
        print num, 'is not a prime number'
        break
    else:
        print num, 'is a prime number'
```