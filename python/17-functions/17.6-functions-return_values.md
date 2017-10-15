```ngMeta
name: Return Values
completionMethod: manual
```

# How to return a value from a function?

Kuch functions jo humne use kare hain, vapas kuch value dete hain. Matlab kuch data vapas dete hain. Abhi tak humne aise functions likhe hain jo kuch bhi vapas nahi dete. Yeh padho:

```python
>>> x = len([1, 2, 3, 4, 5])
>>> x
5
>>> result = say_hello(‘Junisha’)
Hello Junisha
Aap kaise ho?
>>> result
None
```

Yahan dekho `len` ne jo value vapas di woh `x` mein chali gayi. Yahan `x` ki value 5 hai. Lekin humare `say_hello` function ne sirf kuch print kiya lekin vapas nahiz diya kyunki result variable ki value `None` hai. None ka matlab hota hai `kuch nahi`.

Ek simple addition ka function likhte hain jo data vapas deta hai.

```python
def add_numbers(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum

sum1 = add_numbers(20, 40)
print sum1
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print sum2
print sum3
number_a = add_numbers(20, 40) / add_numbers(5, 1)
print number_a
```

* Yahan humne function ussi tareeke se define kara hai jaise hum abhi tak functions ko define karte aaye hain. Lekin sirf function mein last line aap kuch naya dekhoge.
* Last line mein humne `return` statement ka use kar ke function ko yeh bataya hai ki voh `number_sum` ki value ko vapas karega
* Kyunki yeh function `number_sum` ki value vapas kar raha hai, hum iss value ko ek variable mein aasani se daal sakte hain.
* Jaise humne neeche waali lines mein `sum1` variable mein `20` aur `40` ke sum ki value, 60 daal di hai
* Humne **function definition** ki last line mein `return` ka use kar ke ek value vapas karvai hai function se. Hum isko return statement bolte hain. `Return` ka matlab hi vapas dena hota hai
* Jo functions kuch values return karte hain, hum unn functions ke saath kaafi interesting kaam kar sakte hain jaise `number_a = add_numbers(20,40) / add_numbers(5,1)` waali line ko dekho. Yahan humne ek statement mein do add_numbers ko call kiya hai aur fir unn dono ka jo result mila (pehle ka 60 aur dusre ka 6) usko divide kar diya hai Yeh functions jo kuch return karte hain, hum unka use aise kisi statement mein kar sakte hain. Jaise humne division wali line mein kara hai.

Hum same function ko return value ke bina likhte hain.

```python
def add_numbers_print(number_x, number_y):
    number_sum = number_x + number_y
    print number_sum
sum4 = add_numbers_print(4, 5)
print sum4
print type(sum4)
```

Humne yahan same upar wale function ka code likha hai, lekin return statement ka use nahi kiya. Iss vajah se hume yeh function kuch return nahi karega Kyunki yeh function kuch return nahi karta hai, hum apne numbers ke sum ko dusre variable mein nahi daal sakte jaise humne pichle example mein kiya tha.

Yahan agar aap `sum4` ki value dekhoge toh woh `None` dikhayega. `None` ka matlab hota hai kuch nahi. Basically jo numbers value nahi return karte woh "kuch nahi" return karte hain `None` python mein ek alag tareeke ki type hai integer, float etc. ki tarah. `print type(sum4)` waali line mein dekhoge ki woh sum4 ki type ko NoneType dikhayega. Iska matlab hota hai ki isme kuch nahi hai.


Ek baar yeh neeche wale code ko padho aur socho ki kya hoga,. Ab usko chalao aur dekho ki aapne sahi socha tha

```python
number_b = add_numbers_print(5, 4) / add_numbers_print(2, 1)
```

Yahan humne basically aise function ki values ko divide karne ki koshish kari hai jo koi value return nahi karta. Humne abhi padha tha ki jo function return nahi karte , woh None (matlab kuch nahi) return karte hain. Jab hum yahan None ko None se divide karte hain toh python baukhla jata hai aur samajh nahi pata ki kya karna hai. Iss vajah se error return kar deta hai. Python hume error mein bhi yahi bolta hai:

**`unsupported operand type(s) for /: 'NoneType' and 'NoneType'`**

Iska matlab yeh hai ki Python NoneType ki value ko NoneType ki value se hi divide nahi kar  aur iss chakar mein error aa gayi hai.

# Understandng function execution with a return statement

Iss example ko chalane se pehle, iska code padh ke socho ki yeh function kya return karega aur kya print karega jab hum isko 2 integer argument denge.

```python
def add_numbers_more(number_x, number_y):
    number_sum = number_x + number_y
    print "Hello from NavGurukul ;)"
    return number_sum
    number_sum = number_x + number_x
    print "Kya main yahan tak pahunchunga?"
    return number_sum

sum6 = add_numbers_more(100, 20)
```

* Yahan yeh function "Hello from NavGurukul ;)" print karega aur 120 ki value return karega. Yeh 120 ki value "return number_sum" waali line ka use kar ke return karega.
* `sum6` ki value 120 ho jayegi
* Pehli `return number_sum` waali line se neeche aapne jo bhi code likha hai uss code mein se kuch bhi nahi chalega. Yeh isliye nahi chalega kyunki function chalate hue jab python ko ek return statement milti hai, toh python uss return statement ka use kar ke value return kar deta hai aur fir uske neeche wala koi bhi code nahi chalata hai.

Thodi aur depth mein jake mein function execution samajhte hain python mein. Pehle iss code ko run kare bina samjahne ki try karo. Fir ek baar run kar ke dekho.

```python
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"

    print "Kya main print ho payungi? :-("

mon_menu = menu("monday")
print mon_menu
tues_menu = menu("tuesday")
print tues_menu
fri_menu = menu("friday")
print fri_menu
```

Humara `menu` function `day` argument ke hisaab se uss din ki menu ki item ki value return kar deta hai

* Yahan mon_menu mein "Butter Chicken" ki value hogi kyunki humari if-elif-else statement yahan dekhti hai ki din "monday" diya hua hai toh "Butter Chicken" return kar deti hai. Jaise hi python ko return statement dikhti hai woh "Butter Chicken" return kar deti hai aur function chalna banda ho jata hai. Iss vajah se aakhir waali print command nahi chalti. Kyunki uss print command se pehle hi humesha return statement ki vajah se function chalna band ho jata hai
* Aise hi jab day ki value "tuesday" hoti hai toh return "Mutton Chaap" waali return statement execute ho jati hai
* Aur jab "monday" aur "tuesday" dono hi nahi hote, toh return "Chole Bhature" wali return statement execute ho jati hai.
* **Lekin kyunki if-elif-else ke andar se hi return statement execute ho jaati hai, humara program kabhi bhi aakhir wali if statement tak pahunchta hi nahi hai aur woh kabhi print nahi hoti.**

Ab hum same function iss dhang se likhenge ki aakhri wali print command bhi run hoye aur `"Kya main priunt ho payungi? :-("` waali line print ho paye :D

```python
def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print "Kya main print ho payungi? :-("
    return food
    print "Lekin main toh pakka nahi print hounga :'("
```

Yahan humne if-elif-else mein directly return statement ka use nahi kiya. Humne ek `food` naam ke variable mein woh value store karva li jo humne return karvani thi. Ab Jab if-elif-else chal jata hai, toh humara program uske neeche wali print statement pe pahunchta hai. Kyunki python ko abhi tak koi return statement nahi mili hai, woh print command chalata hai. Print karne ke baad woh return statement se *food* variable ki value return kar deta hai Lekin jo akhri wali print statement hai woh nahi print hoyegi. Kyunki uss print statement se pehle return statement chal jati hai aur uski vajah se python needche walai print statement tak pahunchti hi nahi hai