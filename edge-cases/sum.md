## A program to calculate the sum of 2 numbers


###  Python sum function

Is program mai hum ek add ka function ka use karenge


```python
def add(a, b):
	print(a+b)

add(5, 6) # Gives 11
```

ab agar hum ye call karenge to kya hoga?

```python
ans = add(5, 6) + add(2, 3)
print(ans)
```

### Task 

Upar wale statements run karne per kya answer aaya?
agar hum sahi answer chahte hai to hume kya change karna padega?
add function ko fir se likho jisse 2nd wale statement ke liye output sahi ho

### Solution

Add function mai return hona chahiye

```python
def add(a, b):
	return(a+b)
```

