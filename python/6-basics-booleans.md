```ngMeta
name: Booleans
completionMethod: manual
```

# Booleans kya hote hain?

Booleans special type ke constants hote hai (humne abhi tak `Strings`, `Integers` aur `Floats` ke baarein mein padha tha).

Do hi Boolean values hoti hai:

1. True 
2. False

Yeh boolean values humein kaafi interesting cheezein karne mein help karti hai. Inka use kar ke hum kaafi interesting kaam karva sakte hain. 

Jaise agar kisi variable mein True hai toh toh hum computer kuch karne ko, aur agar usme False hai toh kuch aur karne ke liye bol sakte hain.

Abhi ke liye itna samajhne kaafi hai, lekin aage chal ke hum isko aur depth mein samjhenge :)

# Booleans javab dene wale operators

Jab bhi humein computer se question puchne hote hain, toh humnein kuch special type ke operators ka use kar ke puchne padte hain. Yeh operators humesha javab ek boolean mein dete hain jo ki `True` ya `False` hota hai. Neeche diye hue table yeh saare operators listed hain.

| **Operator** | **Meaning**               | **Example**                                                                                                                 |
|:------------:|---------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <            | kya chota hai?            | 7 < 6 # False kyun 7 6 se bada hai <br> 6 < 10 # True kyunki 6 10 se chota hai                                              |
| <=           | kya chota ya barabar hai? | 7 <= 10 # True kyunki 7 10 se chota hai <br> 23 <= 23 # True kyunki 23 23 ke barabar hai                                    |
| ==           | kya barabar hai?          | varx = 10 <br> varx == 10 # True kyunki varx ki value bhi 10 hai <br> 67 == 43 # False kyunki 67 aur 43 ek barabar nahi hai |
| >=           | kya bada ya barabar hai?  | 56 >= 32 # True kyunki 56 32 se bada hai. <br> 43 >= 70 # False kyun 43 `na hi 70 se bada hai` aur `na hi barabar`          |
| >            | kya bada hai?             | number1 = 43 <br> number1 > 20 # True kyunki number1 ki value mein 43 hai aur woh 20 se bada hai                            |
| !=           | kya barabar nahi hai?     | 45 != 45 # False kyunki 45 45 ke barabar hai. <br> 45 != 34 # True kyunki 45 34 ke barabar nahi hai                         |

Python shell mein inn sab operators ke saath khel ke dekho. Aur ache se samajh aayega.

```python
4 < 5 # True
```

```python
56 == 45 # False
```

Python shell mein inn operators ka use karoge toh woh apne aap inka boolean javab dikha dega.