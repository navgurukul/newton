## A program to make a calculator


###  Python calculator function

Is program mai hum calculator ka ek function likhenge jo ki 2 number and ek operator dega and uska result return karega


```python
def calc(a, b, operator):
	if operator == '+':
		return a + b
	elif operator == '*':
		return a * b
	elif operator == '/':
		return a / b
	elif operator == '-':
		return a - b
```

is function ko agar hum call karta huun aise `calc(5, 10, '*')` to kya output hoga

and agar is function ko aise call kare `calc(5, 10, '%')` to kya putput hoga

Hum aise cases ke liye kya kar sakte hai?

Hamesha hum sirf ek limited no of cases ko hi handle kar sakte hai and isilye humme baki input ke liye `Not supported` wala case banana chahiye

### Task 

Is program mai aap ek aisa case ya `if` statement dijeye jo ki saare unwanted operators ko handle kare

### Solution

Hum yahan pe ye keh rahe hai ki ye program ` +, -, /, * ` ke alawa kisi aur operator ko nahi support karta hai

```python
def calc(a, b, operator):
	if operator == '+':
		return a + b
	elif operator == '*':
		return a * b
	elif operator == '/':
		return a / b
	elif operator == '-':
		return a - b
	else:
		print "Unsupoorted operator"
```

