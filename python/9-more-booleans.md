```ngMeta
name: More about Booleans
completionMethod: manual
```

# Introduction

Abhi tak humne yeh padha hai ki booleans ek special type ke data types hote hain. Jaise `integer` aur `float` mein numbers aur `string` mein kuch bhi aa sakta hai. Waise hi `booleans` mein sirf `True` ya `False` aa sakta hai.

Python mein hum `type` function ka use kar ke kisi bhi value ki type dekh sakte hain.

```python
number1 = 124
type(number1) # yeh int karega. `int` ka matlab integer hota hai.

number2 = 123.4
type(number2) # float

string1 = "NavGurukul"
type(string1) # str

x = True
type(x) # bool. iska matlab boolean hota hai
type(4 < 5) # socho iska javab bool kyun aata hai?
```

# If Conditions & Booleans

Programmign mein computer ko apni baat samjhane ke liye hume usse batana padta hai ki kya karna hai. Iske liye hume computer ka batana padhta hai ki alag alag conditons mein alag alag kaam karna hai. Jaise:

1. Lift ke andar ka computer 1 dabane pe 1st floor pe lift ko rok deta hai aur 2 dabane par 2nd floor pe.
2. WhatsApp message padhe ya nah pade jane par blue ya gray tick dikhata hai.

Aisi conditions likhne ke liye humne if statements ka use karna seekha hai pichle sections. If statements booleans ka use karti hai. Yaad karo ki if statements mein hum kuch comparison operators ka use karte the:

1. `<`
2. `<=`
3. `>`
4. `>=`
5. `>`
6. `!=`

Yeh saare comparison operators kuch sawal puchte hain. Jaise

```python
number1 = 45
number2 = 56
if number2 > number1:
	print "Bada hai number2"
else:
	print "Number 2 bada nahi hai"
```

Yahan `>` ek saval puch raha hai. Woh saval hai **Kya number2 number1 se bada hai?** Dhyan se dekho iss saval ke sirf do javab ho sakte hain:

1. Haan / Yes / True
2. Nahi / No / False

Jab iss saval ka javab haan hota hai toh `>` ka output True hota hai aur jab nahi hota hai toh `>` ka output False hota hai. Aur if statement True ya False ke hisaab se code ko execute karti hai. Agar javab True hai toh if ke andar wala code chalega nahi toh else ka andar wala code chalega.

Yeh code chala ke dekho.

```python
if True:
	print "Only I will run"
else:
	print "I will never run"
```

Yahan dekho ki humesha `Only I will run` waali line print hoyegi, kyunki humne direct if ke aage True laga diya hai. If ko humesha True milega aur woh hi chalega.

**Note: Aise code likh kar if-elif-else ke saath try karo aur apne saath waalon ke saath discuss karo.**