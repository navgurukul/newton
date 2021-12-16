# What are loops?

If we want to do a task again and again, so computers can help us with that task.

### Not Translated
Jaise agar mujhe apne 100 friends ko ek eMail bhej ke kisi event ke baare mein batana ho toh main ek ek kar ke har kisi ko eMail bhejne mein bore ho jaungi. Yeh karte karte mujhe bahot mushkil bhi hogi. Aur galti karne ka dar bhi hai. Loops ka istemaal karke same type ka kaam hum baar baar karva sakte hain computers se.


# Writing code for loops

```python
counter = 0
while counter < 5:
	print("NavGurukul")
	counter = counter + 1
```

Iss code mein:

1. `counter` naam ka ek variable define ho raha hai jiski value `0` hai. Flowchart mein bhi same cheez ho rahi hai.
2. Fir ek `while` loop likha hai jiske aage ek condition hai `counter < 5`. `While` ka matlab ho jab tak (जब तक). Toh ek tareeke se `while` loop python ko bolta hai ki jab tak aage di hui condition `True` hai tab tak loop chalao.
3. Jaise hi loop khatam hoga toh while ke bahar wala code chalega. Yeh samajhne ke liye neeche diye hua code chalao:

```python
counter = 0 
while counter < 5:
	print("NavGurukul")
	counter = counter + 1
print("Yeh sirf ek baar print hoga")
```

Yeh code chala ke dekhoge toh `"NavGurukul"` 5 baar print hoga aur last waali line sirf ek baar.

# Ek aur example

Maan lo humne code likhna hai jisme humne 1 se 100 tak saare number print karne hai jo 2 se divide hote hain. Toh hum while loops ka use kar ke aise likhenge:


```python
counter = 1
while counter < 100:
