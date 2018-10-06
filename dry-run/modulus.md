```ngMeta
name: Modulus
completionMethod: manual
```

Modulus/Remainder yani ki % and divide /, computers mai aise kaam karte hai,
`x = 3`, agar x ko 2 se divide karenge to kya answer aayega?

yaad rakhiyega ki interger nos ke liye, hamesha integer hi answer aata hai, mtlb usme float nahi aata
so jab 3 ko 2 se divide karenge to answer 1 aayega and Remainder bhi 1 hi aayega


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
Iska solution verify ya samajhne k liye aap yeh [video](https://www.youtube.com/watch?v=xBWa3aN7-84) dekh sakte ho.

is program mai humne int or float dono daale hai, isko dhyaan se kijeyega

```python
x = 5
y = 4
z = y*1.0

if x/y == x/z:
	print "same hai"
else:
	print "same nahi hai"	


print x/y
print x/z
```
<!-- todo division of floats and integers -->

```python
a = [23, 28, 12, 7, 49, 87]
for i in a:
	if i%7 == 0:
		print i, "ye no 7 se divisibile hai"
	else:
		print i, "ye no 7 se divisibile nahi hai, iska remainder ye raha", i%7
```

