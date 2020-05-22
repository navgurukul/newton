```ngMeta
name: Conversion
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