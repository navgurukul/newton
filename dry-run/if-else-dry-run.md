```ngMeta
name: If Else - Dry Run
completionMethod: manual
```

```python
x = 12
y = 17

if x>y:
    print True
print False
```


```python
x = 34
y = 12
z = 90

if x > y:
    if x < z:
        m = y
    else:
        m = z
else: 
    if y > z:
        m = y
    else:
        m = x
print m
```
**Guess karein ki yeh jo program likha hai uppar, woh kya karta hai. Iske liye aap alag alag numbers ke saath yeh programs try karo.**

```python
marks = 53
if marks>25:
  print "F"
elif marks<=25 and marks>45:
  print "E"
elif marks<=45 and marks>50:
  print "D"
elif marks<=50 and marks>60:
  print "C"
elif marks<=60 and marks>80:
  print "B"
else:
  print "A"
```

```python
amount = 5500
if amount<= 2000:
    discount = (amount * .5)
    print ("Paid Amount: ", amount-discount)
elif amount >=5000 and amount <=6000:
    discount = (amount * .25)
    print ("Paid Amount: ", amount-discount)
if amount >= 10000:
    discount = (amount * .35)
    print ("Paid Amount: ", amount-discount)
else:
    discount = (amount *.50)
    print ("Paid Amount: ", amount-discount)
```
Aap alag alag amounts ke liye yeh code run kar kar dekh sakte hai, better practice ke liye.


```python
amount  35000
transaction_type = "L"
if transaction_type == "L":
    if amount <= 25000:
        discount = amount*.0
        print Net Amount:", amount-discount
    if amount <=57000:
        discount = amount*.5
        print Net Amount:", amount-discount
else:
    if amount <=100000:
        discount = amount*.075
        print Net Amount:", amount-discount
    If amount >= 100000:
        discount = amount*.10
        print Net Amount:", amount-discount
```

```python
u1 = "rock"
u2 = "paper"
if u1==u2:
       return("It's a tie!")
elif u1 == 'scissors':
    if u2 ==’rock’:
        return("Rock wins!")
    else:
        return("Paper wins!")
elif u1 == 'paper':
    if u2 == 'scissors':
        return("Scissors win!")
    else:
        return("Rock wins!")
elif u1 == 'rock':
    if u2 == 'paper':
        return("Paper wins!")
    else:
        return("Scissors win!")
else:
    return("Invalid input! You have not entered rock, paper or scissors, try again.")
```

U1 aur U2 ko different different values jaise "rock", "scissors", "paper", etc. de kar try karo aur samjho iss program ka `control flow` kaisa hai.