```ngMeta
name: Writing Code for If Statements
completionMethod: manual
```

# Introduction

Abhi tak humne if conditions ke flowcharts banana seekh liya hai. Lekin hum iska istamaal tab tak nahi kar sakte, jab tak hum code likhe ke apni baat computer ko batana na seekhein. Python mein code likh ke hum computer ko computer ki bhasha mein hi samjhana padega. Isiliye hum python mein code likh ke, Python ko dhang se code likhna sikhayenge.

```python
day = raw_input("Din enter karo\n")
if day == "monday": # Agar din Monday hai toh
	print "Rajma Chawal"
elif day == "tuesday": # Agar uppar wali conditions galat hai (Yaani day Monday nahi hai) aur day Tuesday hai toh
	print "Pao Bhaji"
elif day == "wednesday": # Agar uppar wali conditions galat hai (Yaani day Monday aur Tuesday nahi hai) aur day Wednesday hai toh
	print "Chole Bhature"
elif day == "thursday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday aur Wednesday nahi hai) aur day Thursday hai toh
	print "Dosa"
elif day == "friday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday aur Thursday nahi hai) aur day Friday hai toh
	print "Litti Chokha"
elif day == "saturday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday aur Friday nahi hai) aur day Saturday hai toh
	print "Thukpa"
else: # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday, Friday aur Saturday nahi hai)
	print "Poha"
```

Iss example mein humne pehle user se aaj ke din ki input li, aur fir uske hisaab se menu print kara hai. Comments ko dhyaan se padh ke samjho ki har line pe kya ho raha hai.

*Note: Jab program aapse input mangeka, toh aapko day ki value ko ekdum exact vaisa hi daalna padega jaise if condition ki statements mein dala hua hai. Isliye computer ke liye `Monday` aur `monday` mein bhi farak hai, kyunki `monday` mein `m` chota hai, aur `Monday` mein `M` bada hai.*

# Kuch aur examples

Abhi tak humne sirf `==` comparsion operator ka use karke if statements likhi hain. Humne Booleans waali exercise mein aur comparison operators ke baare mein padha tha. Jaise:

1. `>`: Greater than (Kya yeh bada hai?)
2. `<`: Less than (Kya yeh chota hai)
3. `>=`: Greater than equal to (Kya yeh bada ya barabar hai?)
4. `<=`: Less than equal to (Kya yeh chota ya barabar hai?)
5. `!=`: Not equal to (Kya yeh equal nahi hai?)

Aage ke kuch examples mein, inn operators ka use kar ke, kuch aur examples diye hue hain:

## Example 1
Aapne apne program mein, ek variable mein string daal diya hai. Ab user se woh string guess karvana hai. Iska code aise likhenge:

```python
value = "delhi"
guess = raw_input("Sheher ka naam guess karo> ")
if guess != value:
	print "Aapka guess galat hai"
else:
	print "Aapka guess sahi hai"
```

## Example 2
Maan lo ek aisa rule hai, ki agar humari gaadi ki speed 60 ya 60 se kam hogi toh overspeeding nahi maani jayegi, nahi toh overspeeding maani jayegi. Iska code kuch aise likhenge:

```python
speed = raw_input("Gaadi ki kya speed thi?")
speed = int(speed)
if speed <= 60:
	print "Gaadi speed limit ke andar thi."
else:
	print "Gaadi speed limit ke bahar thi."
```

*Note: Yahan dekho ki kaise humne pehle `speed` variable ki value ko `string` mein convert kiya hai. Yeh isliye kiya hai kyunki `raw_input` a use kar ke pehle hume value string mein mili lekin hum ek string pe `<=` nahi laga sakte.*

# Nested If Condition
Hum ek if condition ke andar doosri if condition bhi aaram se laga sakte hain.

Maan lo humne din ke time ke hisaab se menu dikhana hai. Jaise Monday ko breakfast mein poha, lunch mein rajma chawal aur  dinner mein roti sabzi banegi, lekin tuesday ko breakfast mein poori sabzi, lunch mein thukpa aur dinner mein chicken chawal banenge. Yeh karne ke liye hum kuch aisa code likhenge.

`TODO: We need to add a flowchart here somehow. #studentsShouldIgnore`

```python
day = raw_input("Din enter karo> ")
meal = raw_input("Meal enter karo, jaise breakfast lunch aur dinner mein se ek> ")
if day == "monday"
	# code yahan andar tab hi aayega jab day ki value "monday" hogi, nahi andar aayega hi nahi
	if meal == "breafast":
		print "Poha"
	elif meal == "lunch":
		print "Rajma Chawal"
	else:
		print "Roti Sabzi"
elif day == "tuesday":
	if meal == "breakfast":
		print "Poori Sabzi"
	elif meal == "lunch":
		print "Thukpa"
	else:
		print "Chicken Chawal"
else:
	print "Aur kisi bhi din hum daal roti sabzi khaynege."
```

Yahan dekho ki kaise humne ek if statement ke andar ek aur if statement lagayi hai. Iska use kar ke andar waali if statement mein code tab hi jayega jab upar waali if statement true hogi.