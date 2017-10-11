```ngMeta
name: Conversion
completionMethod: manual
```

**Note: Yaad se saare code examples ko chala ke dekhna. Chala ke aur samajh ke hi aap seekh paoge.**

# Type Conversion kya hota hai?

Pichle sections mein humne yeh samjha ki python mein alag alag type ka data hota hai. Kuch types jinke baare mein humne pada hai woh hain:

1. Integer
2. Float
3. String

Neeche kuch examples diye hue hain. Inko dhyan se padhein.

```python
# integer
age = 27
total_apples = 100

# float
weight = 10.5
area = 120.56

# string
day = "Wednesday"
name = "Mahatma Gandhi"
a = "Y"
```
Hum python mein ek `type` se dusre `data type` mein apne data ko convert kar sakte hain. Aage chal ke yeh bahot kaam aayega kyunki humare paas bahot baar data ek type mein hoga aur hume kisi aur type mein convert karna padega. Python mein hum yeh `type conversion` kar sakte hain -

1. Float se String
6. Float se Integer
2. Integer se String
3. Integer se Float
4. String se Float
5. String se Integer


# Variable ya Constants ka type Samajhna 

Variable ka type samajhne ke liye hum `type` naam ka ek function use karenge. Functions ke baarei mei detials aage aayengi. Abhi ke liye bas code dekh ke isko use karna seekh le jiye.

```python
var_a = 23
print type(var_a) # yeh integer print karega 
```

Python mein hum ek integer ko string mein convert kar sakte hain. Jaise:

```python
var_b = str(23)
print type(var_b) # yeh str print karega. str ka matlab string hota hai.
```

Sochiye agar hum do `INTEGERs` ko add karenge toh hume kya output milega. and phir yeh print karke dekhiye
```python
print var_a + var_a
```

Ab sochiye agar hum do `STRINGs` ko add karenge toh hume kya output milega. and phir yeh print karke dekhiye
```python
print var_b + var_b
```

Isi tarah iss code ko dhyaan se chala ke samjhein. 

```python
var_a = 2.1
var_b = str(var_a)
print type(var_a)
print type(var_b)
print var_a + var_a
print var_b + var_b
```

Iss exaxmple se aapne kya samjha? Python mein har data type ka alag use hota hai. Alag type ke variables ke saath same kaam karke bhi alag result aayega.

# String se Integer & String se Float
Ab hum dekhte hai ki INTEGER mei conversion kaise karenge. `12` ko python INTEGER mei type cast karkar 12 store kar leta hai

```python
var_a = '12'
var_b = int(var_a)
print type(var_a)
print type(var_b)
print var_a + var_a
print var_b + var_b
```

`12houses` se INTEGER kaise nikalna hai, python nahi samajh pata
```python
var_a = '12houses'
var_b = int(var_a)
print type(var_a)
print type(var_b)
```

Python `STRING` se `INTEGER` karne ki koshish karta hai, but agar thoda sa bhi confuse hota hai toh **error throw** karta hai. Jaise python 12.2, ya 12houses ko integer mei nahi kar sakta par 12 ko kar sakta hai

`12.2` se INTEGER kaise nikalna hai, python nahi samajh pata
```python
var_a = '12.2'
var_b = int(var_a)
print type(var_a)
print type(var_b)
```

# Float se Integer & Float se String

Kisi bhi `float` se python integer mei convert leta hai, uska dashamlav yaani decimal part hata kar

```python
var_a = 12.2
var_b = int(var_a)
print type(var_a)
print type(var_b)
print var_b
```

Ab hum `FLOATS` mei type cast karna seekhenge. Yeh `INTEGER` mei type cast karne jaise hi hota hai. Khud hi dekhiye.

```python
var_a = '12'
var_b = float(var_a)
print type(var_a)
print type(var_b)
print var_a + var_a
print var_b + var_b
```

```python

var_a = '12.2'
var_b = float(var_a)
print type(var_a)
print type(var_b)
```

`12houses` se FLOAT kaise nikalna hai, python nahi samajh pata

```python
var_a = '12houses'
var_b = float(var_a)
print type(var_a)
print type(var_b)
```

# Integer se Float & Integer se String

Python bas dashamlav yani decimal point jod deta hai jab hum `INTEGER` ko `FLOAT` mein convert karte hain. 

```python
var_a = 12
var_b = float(var_a)
print type(var_a)
print type(var_b)
print var_b
```

Yahan dhyaan se dekho ki python last mein `.0` add kar deta hai. Python mein ek float `12.2` ko `INTEGER` mein convert kar ke dekho. Samjho ki kya ho raha hai.