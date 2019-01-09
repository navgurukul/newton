```ngMeta
name: Using Breaks
```

<!-- TODO Aap pehle iss video ko dekhein `break` command ka loop mei kaam samajhne ke liye. Iss understanding ko use kar kar, humein aage likhe hue code ka dry run karna hai. -->

```python
counter = 0
string = "navgurukul"
while (counter < len(string)):
    if string[counter] == "g":
        break
    
    print(string[counter])
    counter += 1

print("The end", string[counter])
```


![How Break Statements Work!](assets/how-break-statement-works.jpg)
Agar aap yeh diagram dekhoge toh aap samjhoge, ki `break` command se hum jiss bhi loop ke andar aapne woh command likhi hai, uss loop se immediately bahar nikal jaate hai.

Ab iss idea ko use karte hue in example codes ka `dry run` karein.

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
```
Iss program ka `output` likh kar, iss program ko bina `break` statement ke likhiye.
Apne likhe hue naye program ka bhi `dry run` karein.

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
```
Iss program ka `output` likh kar, iss program ko bina `break` statement ke likhiye.
Apne likhe hue naye program ka bhi `dry run` karein.