```ngMeta
name: type conversion
completionMethod: peer
```

# Introduction

Iss section mein hum python ka use kar user se input lena seekhenge. Fir hum uss input ke saath type conversion karna bhi seekhenge.

Aage jake bahot baar hume apne users se kuch input leni padegi. Input lene ke liye hum. Python mein `raw_input` ka use karte hain. Jaise:

```python
user_input = raw_input("Kuch input daaliye ")
```

Jab yeh run hoga, toh python ruk jayegi aur ek cursor dikhayegi. Yahan aapko kuch input daalni hogi. Kuch bhi input daal ke `Enter` press kar do. Ab jab aap user_input ko `print` kar ke dekhoge, toh aapne jo bhi value daali hai woh `user_input` variable ke andar string ke roop mein hogi.

```python
print user_input
```

# Ek Aur Example

Ek aur raw_input ka example leke isko aur detail mein samajhte hain.

```python
number1 = raw_input("Ek number daalo ")
```

Yahan dekho ki raw_input ke brackets ke andar humne ek string daala hai. Iss string ki value "Ek number daalo" hai. Hum inn brackets ke andar jo bhi string daalte hain, woh string python use se input maangne se pehle print kar deti hai. Isse user ko kuch hint mil jata hai ki kya input karna hai. Jaise upar wale example mein, python input maangne se pehle `"Ek number daalo"` print kar dega. Aur jab user number (input) daal ke `Enter`
press karega, toh `number1` variable mein woh value chali jayegi. 

Python shell mein `print number1` karenge toh humne jo bhi value daali hai, woh print ho jayegi. 

# User Input ka Type Conversion

Hum jab bhi `raw_input` se kisi variable mein user input lete hain woh string. Type ki form mein hoti hai. Matlab, user jo bhi daalta hai raw_input usko string bana deta hai.

```python
number2 = raw_input("Ek number daalo ")
```	

Yahan `number2` ka data type string hoga. Jab bhi hum kisi variable ki value `raw_input` se input lete hain toh woh value string ki roop mein hoti hai. Agar user ne number bhi input dala hai toh, woh string ke roop mein hoga.

```python
print type(number2)
```

Jaise agar yahan humne 25 enter kia toph `number2` ki value "25" hogi. Kisi bhi value ke aage peeche `quotes` hote hain toh woh string hota hai. Usko integer mein convert karne ke liye hume `int()` ka use karna padega.

```python
number3 = int(number2)
print type(number3)
```

## Ek Aur Type Conversion aur `raw_input` ka Example

Neeche ek final example hai inn sab cheezon ko ache se samajhne ke liye. Yeh example do numbers ko input ko leke unko multiple kar ke print karta hai. 

```python
number_x = raw_input("Pehla number daaliye ")
number_y = raw_input("Dusra number daaliye")
number_x = int(number_x) # raw_input se hume number_x string type mein mila
number_y = int(number_y) # raw_input se hume number_y string type mein mila
print number_x * number_y # number_x aur number_y ka multiple kar ke result print hoga
```

Yahan yeh samajhna bahot zaroori hai ki humne multiply karne se pehle `number_x` aur `number_y` ko integer mein convert kiya kyunki `raw_input` se hume input humesha string ki form mein milti hai.

**Fun Activity:** Iss example mein `number_x` aur `number_y` ko `int` mein convert kare bina chalao aur dekho kya error aati hai. Iss error ko google kar ke aur samajhne ki koshish karo. Apne aas paas peers se bhi discuss karo. Iske liye aapko `number_x = int(number_x)` aur `number_y = int(number_y)` waali lines ko hatana padega.