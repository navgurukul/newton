loops-continue_key1


@[youtube](https://www.youtube.com/watch?v=rOfNF7gj5t0)```python
counter = 0
string = "navgurukul"
while (counter < len(string)):
    counter += 1

    if string[counter] == "a":
        continue

    if string[counter] == "u":
        continue
    
    print(string[counter])

print("The end", string[counter])
```![How Continue Statements Work!](assets/how-continue-statement-works.jpg)loops-continue_key2
- loops-continue_key3
- loops-continue_key4
loops-continue_key5


loops-continue_key6


```python
x = 0
while(x<7):
    if (x == 3 or x==5):
        x = x + 1
        continue
    print(x)
    x = x + 1
``````python
x = 10
while(x<20):
    if (x == 15):
        break
    if (x % 2 == 0):
        x = x + 1
        continue
    print x
    x = x + 1
``````python
num = 2
while(num < 10):
    if num % 2 == 0:
        print "Found an even number", num
        num = num + 1
        continue
    print "Found a number", num
    num = num + 1
```loops-continue_key7
