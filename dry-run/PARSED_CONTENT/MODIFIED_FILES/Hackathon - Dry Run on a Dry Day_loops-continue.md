```ngMeta
loops-continue_key1
```
loops-continue_key2`continue`loops-continue_key3

loops-continue_key4[loops-continue_key5](https://www.youtube.com/watch?v=rOfNF7gj5t0)


```python
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
```
![loops-continue_key6](https://merakidebug.s3.ap-south-1.amazonaws.com/course_images/dry-run/assets/how-continue-statement-works.jpg)loops-continue_key7`continue`loops-continue_key8- loops-continue_key9
- loops-continue_key10
loops-continue_key11`dry run`loops-continue_key12

**loops-continue_key13**

```python
x = 0
while(x<7):
    if (x == 3 or x==5):
        x = x + 1
        continue
    print(x)
    x = x + 1
```
```python
x = 10
while(x<20):
    if (x == 15):
        break
    if (x % 2 == 0):
        x = x + 1
        continue
    print x
    x = x + 1
```
```python
num = 2
while(num < 10):
    if num % 2 == 0:
        print "Found an even number", num
        num = num + 1
        continue
    print "Found a number", num
    num = num + 1
```
loops-continue_key14`execute`loops-continue_key15`continue`loops-continue_key16