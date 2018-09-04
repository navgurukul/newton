```ngMeta
name: Indentation
completionMethod: manual
```

# Indentation kya hoti hai?

Neeche diye gaye code ko dekhiye. Ek baar code ko run kare bina sochiye ki iss code ka output kya hoga. 

```python
a = 10
if a * 2 == 20:
print "a variable ko 2 se multiply kar ke 20 aata hai"
else:
print "Nah! a variable ko 2 se multiply kar ke 20 nahi aata."
```

Aapne kya answer socha? Ab ek baar ekdum aise hi copy paste kar yeh code ek file mein save kar ke run kariye. Aap yeh notice karenge ki yeh code koi output nahi print karta, lekin error de deta hai. Iss error ko samajhne ke liye hume python ke nazariye se sochna padega. Iss program ko python kuch aise chalayegi:

1. Pehli line mein "a" mein 10 ki value daal dega
2. Dusri line mein python yeh check karegi ki a ko 2 se multiply kar ke kya remainder 0 aayega ya nahi.
3. Teesri line pe aate aate python ko pata chalta hai ki a ko 2 se divide karne se remainder 0 aayega. Lekin yahan tak python confuse ho jati hai. Usko samajh nahi aata ki mujhe sirf "The number is divisible by 2" print karna hai ya uske neeche waala code bhi run karna hai. Aapko yeh insaanon ke nazariye se bahot simple problem lag rahi hogi, lekin computer baukhla sa jata aur error de deta hai.

Iss program ko sahi se aise likhenge:

```python
a = 10
if a * 2 == 20:
    print "a variable ko 2 se multiply kar ke 20 aata hai"
else:
    print "Nah! a variable ko 2 se multiply kar ke 20 nahi aata."
```

Jab python iss sahi program ko run karegi toh uska dimaag kuch aise chalega.

1. Pehli line mein "a" mein 10 ki value daal degi.
2. Dusri line mein python yeh check karegi ki a ko 2 se divide kar ke kya remainder 0 aayega ya nahi.
3. Teesri line mein python "The number is divisible by 2" print karegi. Ab aap sochenge ki agar isme python print karegi toh fir usko pichle wale example mein bhi print karni chaiye thi. Lekin yahan dhyaan se dekho teesri print waali line kuch space ke baad shuru ho rahi hai. Inn spaces ko python mein indent kehte hain. Isse python ko samajh aati hai agar "a" 2 se divisible hai toh if ke neeche jin lines (iss example mein ek hi line hai) ko indent kara hua hai sirf woh chalani hai.
4. 4th line pe python ko else milta hai, lekin woh else run karta hi nahi hai kyunki if already chal chuka hai. Iske liye if statement kaise use karte hain woh yaad karne ki koshi kariye.

Iss spacing ko python mein indentation kehte hain. Aur jab bhi indentation related koi bhi problem aati hai toh python IndentationError naam ki error dikhayega. Yeh error kuch aisi dikhti hai:

```python
  File "<ipython-input-5-9eaf99c4383b>", line 3
    print "a variable ko 2 se multiply kar ke 20 aata hai"
        ^
IndentationError: expected an indented block
```


# Ek aur example

Hum ek aur example lete hain isko aur ache se samajhne ke liye. Pehle neeche wale program ko ek baar run kariye. Usko baad neeche diye gaye text ko padiye.

```python
counter = 1
while counter < 10:
	print "The counter is" + str(counter)
	counter = counter + 1
	print '--------'
```	

Iss program mein neeche waali 3 lines (‘print "The counter is" + str(counter)’, ‘counter = counter + 1’, ‘print "--------"’) ko indent nahi karoge toh python ko samajh nahi aayegi ki while loop ke baad mujhe kya chalana hai. Wahan woh confuse ho jayegi aur error de degi. Isiliye python mein code ko indent karna bahot important hai. Aap agar sochenge toh realize karenge ki iss program mein code kuch hisson mein bata hua hai:

1. Pehle hisse mein hum `counter` variable define karte hain aur `while counter < 10` waali line likhte hain.
2. Dusre hisse mein humne Humne woh code likha jo for loop run hone ka baad baar baar run hoga jab tak for loop run hota hai.

In code ke hisson ko hum blocks kehte hain aur python mein blocks ko indent karne ke liye tab ka use hota hai.

Isko samajhne ke liye ek baar ek nayi file neeche diye gaye code ko save kariye aur fir dekho ki iska output upar wale code se kaise different hai. Iske baad apne ke saath discuss karo ki yeh kya hua.

```python
counter = 1
while counter < 10:
	print "The counter is" + str(counter)
	counter = counter + 1
print '--------'
```

**Note: Waise toh aap jab code likh rahe hain toh aapke editor ko khud hi indent kar dena chaiye, agar woh nahi karta hai toh aap abhi ke liye Tab key ka use karke indent kar sakte hain.**

# Multiple Levels of Indentation

Ek indented code block ke andar dusra indented code block bhi ho sakta hai. Jaise iss code ko padho aur samjho ki iska kya output aayega. Fir is code ko chala ke dekho aur dekho ki aapne sahi socha tha ya nahi. Agar nahi toh fir aur dimaag laga ke sochne ki koshish karo.

```python
counter = 1
while counter < 10:
	if counter % 2 == 0:
		print "Counter even number hai."
	print "The counter is" + str(counter)
	counter = counter + 1
print '--------'
```

Yahan yeh dekhiye ki iss code mein indented code blocks ke 2 level exist karte hain.

1. Pehle level ke neeche ‘if counter % 2 == 0’ hai.
2. Uske neeche waale level pe `print "Counter even number hai."` hai.

Yahan python if aur else sirf tab chalati hai jab while loop chal raha hai kyunki woh loop ke neeche hai. `print "Counter even number hai."` sirf tab chalta hai jab loop chal raha hai aur loop ke andar `counter` ki value mein even number hai.
