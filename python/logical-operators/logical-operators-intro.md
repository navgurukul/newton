```ngMeta
name: Logical Operators
completionMethod: manual
```

# What are boolean operators?

Abhi tak humne booleans data type ke baare mein bahot samjha hai. Booleans special type ke constants hote hai (humne abhi tak Strings, Integers aur Floats ke baarein mei padha tha). Do hi boolean values hoti hai:

1. True
2. False

Jaise integers ko add, subtract, divide, multiply, etc. kiya ja sakta hai (isko operation kehte hai - jaise integers par add operation). Aise hi Booleans par bhi kuch special operations kiye ja sakte hai. Iske liye, yeh example and yeh exercise karo. Inn operators ko **logical operators** kehte hain.

Jab hum addition subtraction karte hain toh `+`,`-` ko operators kehte hain. Aise hi boolean operators hote hain. Jaise integers ko `+` karke result bhi integer aata hai, waise hi booleans pe boolean operators ka use kar ke result bhi boolean mein hi aata hai.

3 logical operators hote hain:

1. `and`
2. `or`
3. `not`

Yeh kuch examples hain.

```python
print True and True
print True or False
print not True
```

Dhyaan se iska output dekho aur fir samajhne ki koshish karo ki yeh operators kya karte hain. Neeche humne aur depth mein inki explaination di hui hai.

| Operator | Kya Matlab Hai?                                                                                | Kuch Examples                                                                                                                                                                                           |
|----------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `and`    | `True` agar dono side ki values `True` hai                                                         | `True and True` iska javab True hoga kyunki dono True hain <br> `True and False `iska javab False hoga kyunki inme se ek False hai                                                                      |
| `or`     | `True` agar dono side ki values mein se ek bhi `True` hai. Nahi toh `False`                                      | `True or False `iska javab True hoga kyunki inme se ek True hai <br> `True or True `iska javab True hoga kyunki dono hi True hain <br> `False or False `iska javab False hoga kyunki dono hi False hain |
| `not`    | Yeh ek value leta hai aur usko `ulta` kar deta hai. True ko False kar deta hai aur False ko True | `not False` iska javab True hoga kyunki False ki ulti value true hogi                                                                                                                                   |


## AND Examples

```python
print (True and True)
print (True and False)
print (False and True)
print (False and False)
```

Inn saaron ko python shell mein chala ke dekho aur results ko upar waale table ke hisaab se samjho.

## OR Examples

```python
print (True or True)
print (True or False)
print (False or True)
print (False or False)
```

Inn example ko bhi chala ke samjho.

## NOT Examples

```python
print (not True)
print (not False)
```

Ab yeh examples bhi chala hi lo bhai. Itni sunni hai, toh yahan bhi sun lo :D

# Using Logical Operators in If Statements

Booleans par logical operators lagane ke baad result bhi ek boolean hi hota hai. Aur humne pehle yeh samjha tha ki basically **if statement** booleans pe kaam karti hai. Toh basically hum if statements mein logical operators use kar sakte hain.

Maan lo humne ek program banana hai jo weight input le aur check kar ki kya woh 50 se zyada aur 60 se kam hai. Usko hum `and` ke bina ek if ke andar ek `if` likh ke karenge. Jaise:

```python
weight = raw_input("Apna weight daaliye > ")
weight = int(weight)
if weight > 50:
	if weight < 60:
		print "Aapka weight 50 aur 60 se beech mein hai."
else:
	print "Nahi hai"
```

Yeh program mein pehli waali if statement chalegi. Aur agar woh if statement True hogi toh hi uske neeche waali chalegi. 

Issi ka better tareeka likhne ka yeh hai:

```python
weight = raw_input("Apna weight daaliye > ")
weight = int(weight)
if weight > 50 and weight < 60:
	print "Aapka weight 50 aur 60 se beech mein hai."
```

Humne and ka use kar ke bahot better code likh liya hai.

Yeh ek aur example hai. Hum user se username/password input karvaeynge aur agar woh humare paas stored username password se match karega hum toh hi success message dikhayenge. Jaise:

```python
username = raw_input("Apna username daalo > ")
password = raw_inpit("Apna password daalo > ")
if username == "rishabh" and password = "hello123":
	print "username aur password sahi hai."
```

Aise hi apne aap thode aur examples likhne ki koshish karo.