```ngMeta
name: Logical Operators in If Statements
```

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