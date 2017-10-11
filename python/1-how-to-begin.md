```ngMeta
name: Kaise shuru karein?
completionMethod: manual
```

# Iss course ko kaise use karein?

Python kaise use karte hai, iss [**video**](https://www.youtube.com/watch?v=ccPrUbz1oto) ko dekh kar samjhe

Aage chal ke saare course mein har jagah alag alag tareeke se python ke code ke examples diye gaye hain. Inn examples ko aapko chala ke dekhna padega. 

```python
print "Yeh python mein print hoga"
print "Yeh ek aur line print hoyegi"
print 2 + 5
i = 0
while i < 100:
    print "Main baar baar print hounga :)"
```

Iss tareeke se pure course mein code likha hoga. Iss code ko aapko chalake dekhna padega. Isko chalane ke liye aapko Terminal naam ka application
apne laptop pe kholna padega. Usko khol ke usme yeh type kar ke python chalani padega.

```sh
$ ipython
```

Jab iPython khul jaye toh aap usme code likh sakte ho. Agar aap kahin se code copy paste kar rahe ho toh `Ctrl + C` se copy paste kar ke
aapko iPython khol ke usme `%paste` type kar ke paste karna padega.


## Bahot Important Rules

1. Har ek example ko iPython shell mei execute kar kar dekhe. Agar aap yeh nahi kar rahe, toh apne aap ko bevkoof bana rahe ho.
2. Code ko copy-paste karke chalane se aap seekh nahi payenge dhang se. Aapko har code ko apne haath se chala ke dehna chaiye.
3. UPPER CASE ya **bold letters** mei likhe hue shabd kaafi important hai. Unhe yaad kar lo, woh aapko baar baar milenge.
4. Course mein bahot jagah aapko kuch questions ka javab dena hoga. Javab dene ke liye aap humesha file upload kar sakte hain.

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