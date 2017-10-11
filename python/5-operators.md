```ngMeta
name: Operators
completionMethod: manual
```

# Introduction

Operation se aap kya samajhte hai? Ise kuch examples se samajhte hai.

1. 3 + 4 mei `addition (+)` ek operator hai jo 3 aur 4 par operate kar raha hai. Iska result `7` hoga.
2. 8 / 2 mei `division (/)` ek operator hai jo 8 aur 2 par operate kar raha hai. Iska result `4` hoga.
3. 9 * 2 mei `multiply (*)` ek operator hai jo 3 aur 4 par operate kar raha hai. Isko 

# Modulus Operator

Python mein ek special operator hota hai jiske baare mein shayad aapne pehle na suna ho. Isko `modulus` operator kehte hain. Iske liye normally `%` (percentage) sign use kiya jata hai.

```python
print 9 % 2
```

Iska result 1 hoga kyunki 9 ko jab 2 se divide karenge toh `remainder` (yaani `sheshfal`/`शेषफल`) 1 aaega. Yeh operator ek number ko dusre se divide kar ke bachna wale remainder ka result deta hai. Aage jake programming yeh aapke liye programming ke sabse useful operators mein se ek ban jayega :)

Neeche modulus operator ke kuch aur examples hain.

**Yaad Rakhein:** Aapko kuch bhi cheez ko ache se samajhne ke liye toh apne aap har ek chote chote code ko chala ke dekhna padega.

```python
print 7 % 2 # 1 
print 9 % 3 # 0
print 25 % 4 # 1
print 97 % 3 # 1
print 12 % 5 # 2
print 98 % 5 # 3
```

# Types aur Operators ka Sambandh

Agar hum integer ko integer se divide karenge toh humein javab bhi integer mein milega. Jaise `10 / 2` ka javab `5` hoga. Ek baar apne python shell mein `9` ko `2` se divide karne ki koshih karo.

```python
9 / 2
```

Dekho, kaise aapko iska javab `4` mila. Aap soch rahe hoge ki iska javab toh `4.5` milna chaiye tha. Lekin python do integers ki division ka javab integer mein hi deti hai. Aise hi agar inme se ek bhi `float` hoga, toh python javab bhi `float` mein degi. Jaise:

```python
print 9.0 / 2
```

Iska javab aapko `4.5` milega. Neeche kuch aur examples diye hue hain. 

## Example 1
```python
print 100 / 3
print 100 / 3.0
```

## Example 2
```python
print 35 / 4
print 35 / 4.0
```

Kuch aur examples ke saath apne aap experiment kar ke dekhein.


# Yaad Karein

Yeh python mein saare operators aur unke kuch examples hain.

| **Name**       	| **Operator** 	    | **Example**                         	    |
|----------------	|-------------------|----------------------------------------   |
| Multiplication 	| `*`            	| 10 * 3 = 30 <br> 6* 2 = 12               	|
| Division       	| `/`            	| 10 / 3 = 3 <br> 10 / 3.33333333333333335 	|
| Addition       	| `+`            	| 3 + 30 = 33 <br> 70 + 20 = 90            	|
| Subtraction    	| `-`            	| 20 - 2 = 20 <br> 9 - 8 = 1               	|
| Modulus        	| `%`            	| 8 % 3 = 2 <br> 10 % 9 = 1                	|