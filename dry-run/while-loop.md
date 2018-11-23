```ngMeta
name: While Loops
completionMethod: manual
```

Aap pehle iss video ko dekhein `while` program ka dry run samajhne ke liye. 

@[youtube](https://www.youtube.com/watch?v=s_7YgktIJFo)

```python
c = 0
d = 1

while c < 3:
    c = c + 1
    d = d * c
    print "Loop Ke Andar", c, d
else:
    print "Loop Ke Bahar", c, d
```

While loop kya hota hai yeh samajhne ke liye aap yeh dono videos dekh sakte ho.  

@[youtube](https://www.youtube.com/watch?v=efg169eYEqo)

@[youtube](https://www.youtube.com/watch?v=oG_jCqPVJYA)

```python
c = 0

while c < 5:
    print "Loop Ke Andar"
    c = c + 1
else:
    print "Loop Khatam, Hajmola Hajam, Ab Else Ki Baari hai"
```

Ab aap yeh questions solve karein.
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
num = 407

i = 2
while (i<num):
    if (num%i == 0):
        print num, 'is not a prime number'
        break
    else:
        print num, 'is a prime number'
```
