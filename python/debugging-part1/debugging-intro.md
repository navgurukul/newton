```ngMeta
name: Debugging
completionMethod: manual
```

# What is debugging?

![debugging-intro](assets/debugging-intro.jpg)


Abhi tak humne sirf code likhna seekha hai. Bahot baar jab hum codelikh rahe honge toh humari galti ki vajah se humara code chalega nahi. Ya hume dusron ke likhe hue code ke saath bhi kaam karna padega. Inn cases mein hume code ke andar ki galtiyon ko sahi karna hota hai. Iss process ko debugging kehte hain. Neeche diye gaye coe ko chalao:

```python
	number1 = 234
	print numer1
```

Jab hum iPython shell mein code chalayenge toh python kuch aisa print karega.

```python
<ipython-input-1-2a33fa4e8a92> in <module>()
      1 number1 = 234
----> 2 print numer1

NameError: name 'numer1' is not defined
```

Yeh ek error hai jo bata rahi hai ki 2 number line pe (2 ke saamne ek arrow dekhiye) kuch error hai. Iske end mein error ka naam aur description bhi likhi hui hai. Yahan dekho ki python bol raha hai ki error ka naam `NameError` hai aur error ki description mein `name 'numer1' is not defined`. 

Iss error ko padh ke hume samajh aa raha hai ki `numer1` defined nahi hai. Matlab humne `numer1` naam ka variable nahi banaya. Dhyaan se dekho, humne ek spelling mistake kar di hai. Hum `m` lagana bhul gaye aur humne `numer1` likh diya `number1` ki jagah.

Isko sahi kar ke chaloge toh chal jayega.

# Kuch aur problems

Yeh code dekho aur error samjho.

```python
number1 = 234
number2 = "1"
print number1 + number2
```

Yahan python yeh error print kar dega.

```python
<ipython-input-2-56b79ffda8bc> in <module>()
      1 cnumber1 = 234
      2 number2 = "1"
----> 3 print number1 + number2

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Yeh bata raha hai ki Line number `3` par error hai. Error ko samajhne ke liye error ko google karo. `TypeError: unsupported operand type(s) for +: 'int' and 'str'` ko google karo. Normally aapko google ke pehle ya doosre results mein hi error ko sahi karne ka tareeka mil jayega.

Ab agli kuch assignments mein aapko kuch pehle se likha hua code milega. Aapko uss code mein galti sahi kar ke final sahi file upload kar ke submit karna hai.