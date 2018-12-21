# Ab hum iPython ke bare me sikhenge

<!-- Yahan ipython kya ha aur kyu ushe ishtamal karte hai -->


Jab app Terminal me `python` likhte ho toh apke liye Terminal pe *python shell* khul jaata hai, *python shell* pe app apne python ke code likhte ho usse chalane ke liye.

iPython ka bi kaam yehi hota hai lekin ussme kuch extra feature hume milte hai jin mein se hum kuch feature ke bare meh niche janege.

## python aur iPython me antar

### Phele iPython ke sath
App Terminal pe phele ```ipython``` likhe aur *Enter* dabaye.

Ab app ushme ```cd Downloads``` likhe aur *Enter* dabaye.

Ab app ushme ```ls``` likhe aur *Enter* dabaye.

Apko woh sare *folder aur file* dikh rahe honge joh apne Downloads wale folder me rakhe hai.

Ab iPython ke shell se bahar ane ke liye ```quit``` likhe shell ke andar aur *Enter* dabaye.


### Ab yehi hum python ke sath karne ki kosish karenge

App Terminal pe phele ```ipython``` likhe aur *Enter* dabaye.

Ab app usme ```cd Downloads``` likhe aur *Enter* dabaye.

```python
>>> cd Downloads
  File "<stdin>", line 1
    cd Downloads
               ^
SyntaxError: invalid syntax
>>> 
```

Kuch aisa ahh raha hoga apke Terminal pe?
Jiska matlab app *Downloads* folder me *python shell* ke madad se ni jah sakte

iske liye apko bahar ana hoga *python shell* se aur uske liye apko ```quit``` type karna hoga *python shell* me.

Ab bahar ane ke baad app type kare ```cd Downloads``` aur phir type kare ```ls``` apko Downloads me joh kuch bi tha woh dikh jayega.

Ap normal *python shell* se apna **folder** change nhi karsakte uske liye apko *python shell* se bahar ana hoga lekin python shell ke andar app aram se **folder** change karsakte ho jise apko *iPython shell* se bahar ane ki koi jarurat nhi hogi.


Aur jab app *python shell* me jake type karoge
```python
>>> if True:
... 
```
Toh dhyan dena apka cursor(**|**) ```...``` ke baad bina kisi space ke ahta hai.
Lekin jab app yeh *iPython shell* meh karoge toh woh kuch ish tara ka hoga.

```python
In [1]: if True:
   ...:     |
```
Toh app dekoge apka joh cursor(**|**) hai woh kuch spaces baad aata hai.
Ishe **Indentation** kehte hai. Jab aap phele baar code likh rahe hoge apke **50% error** hogi
woh **Indentation** ko leke hogi.


Aise hi iPython me bohut sare feature hote hai joh ek engineer ki life thodi asan bana deti hai.

Jab iPython khul jaye toh aap usme code likh sakte ho. Agar aap kahin se code copy paste kar rahe ho toh `Ctrl + C` se copy paste kar ke
aapko iPython khol ke usme `%paste` type kar ke paste karna padega.


## Bahot Important Rules
- Har ek example ko iPython shell mei execute kar kar dekhe. Agar aap yeh nahi kar rahe, toh apne aap ko bevkoof bana rahe ho.
- Code ko copy-paste karke chalane se aap seekh nahi payenge dhang se. Aapko har code ko apne haath se chala ke dekhna chaiye.
- UPPER CASE ya **bold letters** mei likhe hue shabed kaafi important hai. Unhe yaad kar lo, woh aapko baar baar milenge.
- Course mein bahot jagah aapko kuch questions ka javab dena hoga. Javab dene ke liye aap humesha file upload kar sakte hain.

## Kuch Code Samples

Iss section mein kuch code samples diye hue hain. iPython se comfortable hone ke liye aap inko iPython mein chala ke dekh sakte ho.

### Example 1

```python
print "Yeh python print kar degi"
print "Cool Stuff "*10
```

### Example 2

```python
time = raw_input("Is it morning or evening? (morning/evening) ")
if time == "morning":
    print "Let's go for a run!"
elif time == "evening":
    print "Let's go out for a coffee."
else:
    print "Mujhe samajh nahi aaya aapne kya input daala."
```
