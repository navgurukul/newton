```ngMeta
name: Using Continue
completionMethod: manual
```

![How Continue Statements Work!](assets/how-continue-statement-works.jpg)
Agar aap yeh diagram dekhoge toh aap samjhoge, ki `continue` command se hum loop mei
- jo bhi `continue` ke baad code hai uss loop mei, woh `execute` nahi hota
- loop ki starting mei `control flow` pahuch jaata hai

Ab iss idea ko use karte hue in example codes ka `dry run` karein.

__Ek baar dhyaan se dekhein ki break aur continue mei kya difference hai__

```python
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
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