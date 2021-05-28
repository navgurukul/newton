```ngMeta
loops-break_key1
```
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
![loops-break_key2](https://merakidebug.s3.ap-south-1.amazonaws.com/course_images/dry-run/assets/how-break-statement-works.jpg)loops-break_key3`break`loops-break_key4

loops-break_key5`dry run`loops-break_key6

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
### loops-break_key7
### loops-break_key8
### loops-break_key9
### loops-break_key10
### loops-break_key11
### loops-break_key12
### loops-break_key13
loops-break_key14`break`loops-break_key15

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
loops-break_key16`output`loops-break_key17`break`loops-break_key18`dry run`loops-break_key19

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
loops-break_key20`output`loops-break_key21`break`loops-break_key22`dry run`loops-break_key23