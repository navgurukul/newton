## A program to calculate the sum of elements in a list


###  Python calculator sum of a list

Is program mai hum calculator ka ek function likhenge jo ki 2 number and ek operator dega and uska result return karega


```python
arr = [0, 5, 2, 1]
l = len(arr)
s = 0
i = 1

while(i < l):
	s = s + arr[i]
	i+=1

print(s)
```

ye program list `arr` ka sum calculate karta hai

### Task 

- kya ye program sahi hai?
	- agar nahi to kya galat hai?
- kya is program ka output sahi hai?
- agar hum is program mai `arr` ki value `[45, 1, 5]` rakhenge to kya output aayega?
	- kya ye output sahi hai?
	- sahi output kya hoga
	- sahi output laane ke liye hum program mai kya change karenge?


In saare jawabo ke baad hi aap answer dekhiyega

### Solution

humara loop array ke pehle element ko count nahi kar raha hai, uske liye hum `i` ko `0` se starte karenge

```python
arr = [0, 5, 2, 1]
l = len(arr)
s = 0
i = 0

while(i < l):
	s = s + arr[i]

print(s)
```

