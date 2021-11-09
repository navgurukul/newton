```python
counter = 0
string = "navgurukul"
while (counter < len(string)):
    if string[counter] == "g":
        break
    
    print(string[counter])
    counter += 1

print("The end", string[counter])
```![How Break Statements Work!](assets/how-break-statement-works.jpg)loops-break_key1


loops-break_key2


```python
var = 10
while var > 0:              
   print 'Current variable value :', var
   var = var - 1
   if var == 5:
      break

print "Good bye!"
``````python
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

loops-break_key3
loops-break_key4


```python
i = 0
while(i<5):
    j = 0
    while(j<5): #loop2
        if (j > 3): 
            break 
        else:
            print "*", 
        j = j + 1    
    print ''
    i = i + 1
```loops-break_key5


```python
a = 0
while(a<6):
    b = 0
    while(b<6):
        if (a == b):
            break
        print '*',
        b = b + 1
    print ''
    a = a + 1
```loops-break_key6
