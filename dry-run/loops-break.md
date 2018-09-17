```ngMeta
name: Using Breaks
completionMethod: manual
```

![How Break Statements Work!](assets/how-break-statement-works.jpg)
Agar aap yeh diagram dekhoge toh aap samjhoge, ki `break` command se hum jiss bhi loop ke andar aapne woh command likhi hai, uss loop se immediately bahar nikal jaate hai.

Ab iss idea ko use karte hue in example codes ka `dry run` karein.

```python
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")
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