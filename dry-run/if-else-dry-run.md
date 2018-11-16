```ngMeta
name: If Else - Dry Run
completionMethod: manual
```

Aap pehle iss [video](https://www.youtube.com/watch?v=5jlV9b1GB9k&feature=youtu.be) ko dekhein if-else program ka dry run karne ke liye. 

```python
x = 15
y = 12

if x > y:
    print "y se bada x hai"
else:
    print "x se bada y hai"

x = 12
y = 15
z = 18

if x > y:
    print "y se bada x hai"
elif y > z:
    print "z se bada y hai"
else:
    print "x se bada y hai, aur y se bada z hai"
```


```python
x = 12
y = 17

if x>y:
    print True
print False
```

```python
x = 10
y = 5
if x > y:
    smaller = y
else:
    smaller = x
```

```python
x = 10
y = 5
smaller = x
if x > y:
    smaller = y
```
Kya yeh dono program same hai ya alag? Kyu same hai? Thoda socho.

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

### Questions
- Kya kabhi `marks <= 25 and marks>45` True ho sakta hai? Agar ho sakta hai, toh marks ki kaunsi value par?
- Iss program ko marks ki values - `20, 24, 28, 30` ke liye **execute** karo. Dekho ki kaun kaun si conditions execute nahi ho payengi.
- Kya aap iss program ko modify kar sakte hai, jisse ki hum sahi se student ko uske marks ke hisaab se usko grade de payein.

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
amount = 2400
transaction_type = "L"
if transaction_type == "L":
    if amount <= 25000:
        discount = amount*.0
        print "Net Amount:", discount
    if amount <=57000:
        discount = amount*.5
        print "Net Amount:", discount
else:
    if amount <=100000:
        discount = amount*.075
        print "Net Amount:", discount
    if amount >= 100000:
        discount = amount*.10
        print "Net Amount:", discount
```

```python
u1 = "rock"
u2 = "paper"
if u1==u2:
       print "It's a tie!"
elif u1 == 'scissors':
    if u2 ==’rock’:
        print "Rock wins!"
    else:
        print "Paper wins!"
elif u1 == 'paper':
    if u2 == 'scissors':
        print "Scissors win!"
    else:
        print "Rock wins!"
elif u1 == 'rock':
    if u2 == 'paper':
        print "Paper wins!"
    else:
        print "Scissors win!"
else:
    print "Invalid input! You have not entered rock, paper or scissors, try again."
```

u1 aur u2 ko different different values jaise "**rock**", "**scissors**", "**paper**", etc. de kar try karo aur samjho iss program ka `control flow` kaisa hai.

Iska solution verify ya samajhne k liye aap yeh [video](https://www.youtube.com/watch?v=5v0Ie9ig0Qs) dekh sakte ho.