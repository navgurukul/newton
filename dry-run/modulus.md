```ngMeta
name: Modulus
```

Modulus/Remainder yani ki % and divide /, computers mai aise kaam karte hai,
`x = 3`, agar x ko 2 se divide karenge to kya answer aayega?

Modulus kya hota hai, yeh samajhne ke liye yeh yeh video dekho. 

@[youtube](https://www.youtube.com/watch?v=0k-X9XXlp_U)

yaad rakhiyega ki interger nos ke liye, hamesha integer hi answer aata hai, mtlb usme float nahi aata
so jab 3 ko 2 se divide karenge to answer 1 aayega and Remainder bhi 1 hi aayega

Yeh video bhi dekho.

@[youtube](https://www.youtube.com/watch?v=guFq-gTwTG8)

```python
x = 30
a = x % 7
b = x % 8
c = b % a
d = a % b
e = c % d
f = d % c
print x, a, b, c, d, e
```

```python
x = 5
print x/2
print x%2
```

```python
x = 1
print x/2
print x%2
```

```python
x = 5
y = 4
print x / y
print x % y
```


```python
x = 5
y = 4
print x / y
print x % y
```

ye program mai kuch galti hai isko aap ko sahi karna hai
Ye program ye batata hai ki **x** 3 ka multiple hai ya nahi, is program ko dry run kare or fir sahi bhi kare
**x** ki diff values ke liye code likhe jaise 3, 10, 25, 6

```python
x = 12
if (x%3 == 0):
	print "3 ka multiple hai"
else:
	print "3 ka multiple nahi hai"
```
Iska solution verify ya samajhne k liye aap yeh video dekh sakte ho.

@[youtube](https://www.youtube.com/watch?v=xBWa3aN7-84)

```python
a = [23, 28, 12, 7, 49, 87]
for i in a:
	if i%7 == 0:
		print i, "ye no 7 se divisibile hai"
	else:
		print i, "ye no 7 se divisibile nahi hai, iska remainder ye raha", i%7
```

