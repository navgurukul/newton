## Edge cases in Prime no


### Calculate first 5 prime no's

Hume is program mai pehle 5 prime no print karne hai

```python
n = 2
count = 0
isPrime = True
while(count < 5):
	i = 2
	while(i<n):
		if n%i == 0:
			isPrime = False
		i = i + 1
	if (isPrime):
		print (str(n) + "is prime")
		count += 1
	n = n + 1 
```

ye program infinite loop mai chala jaat hai

### Task 

Is program ko aap sahi se padhiye or laptop pe chala ke dekhiye
ab aap is program mai aisi kaunsi jagah change karenge, jisse ye program sahi output dene lage
agar aapko nahi nahi samajh aa raha ho to aap dry run kijeye and fir aapna answer compare kijeye


### Solution

Is program mai humne `isPrime` jo variable hai uske ek set na karke baar baar set kar rahe hai, pehle loop ke ander
isse ye program infinite loop mai na jake, `isPrime` ki value ko reset kar raha hai


```python
n = 2
count = 0
while(count < 5):
	isPrime = True
	i = 2
	while(i<n):
		if n%i == 0:
			isPrime = False
		i = i + 1
	if (isPrime):
		print (str(n) + "is prime")
		count += 1
	n = n + 1 
```

