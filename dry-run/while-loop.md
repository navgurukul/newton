```ngMeta
name: While Loops
completionMethod: manual
```

While loop kya hota hai yeh samajhne ke liye aap yeh [video](https://www.youtube.com/watch?v=efg169eYEqo) ya [video](https://www.youtube.com/watch?v=oG_jCqPVJYA) dekhein.

```python
c = 0

while c < 3:
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