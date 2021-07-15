```ngMeta
if-statement-code-intro_key1
```

if-statement-code-intro_key2
if-statement-code-intro_key3


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
if-statement-code-intro_key4


if-statement-code-intro_key5


if-statement-code-intro_key6
if-statement-code-intro_key7
1. if-statement-code-intro_key8
2. if-statement-code-intro_key9
3. if-statement-code-intro_key10
4. if-statement-code-intro_key11
5. if-statement-code-intro_key12
if-statement-code-intro_key13


if-statement-code-intro_key14
if-statement-code-intro_key15


```python
value = "delhi"
guess = raw_input("Sheher ka naam guess karo> ")
if guess != value:
    print "Aapka guess galat hai"
else:
    print "Aapka guess sahi hai"
```
if-statement-code-intro_key16
if-statement-code-intro_key17


```python
speed = raw_input("Gaadi ki kya speed thi?")
speed = int(speed)
if speed <= 60:
    print "Gaadi speed limit ke andar thi."
else:
    print "Gaadi speed limit ke bahar thi."
```
if-statement-code-intro_key18


if-statement-code-intro_key19
if-statement-code-intro_key20


if-statement-code-intro_key21


if-statement-code-intro_key22


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
if-statement-code-intro_key23
