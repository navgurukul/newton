## Split function


###  Rewriting python's split function, Splitting a string into smaller strings

is program mai hum split function ko code karenge

```python
def split(s, delim):
	a = []
	i = 0
	temp_s = ''
	while(i<len(s)):
		if s[i] != delim:
			temp_s += s[i]
		else:
			a.append(temp_s)
			temp_s = ''
		i += 1
	return a
```

is program ko aap run karke dekhiye
```
split("Hello this is NG", " ")
```

### Task 

- kya ye program sahi hai?
	- agar nahi to kya galat hai?
- kya is program ka output sahi hai?

Is program ko sahi karne ke liye humme kya karna hoga?
is program mai kya galti thi?
agar galti nahi samajh mai aa rahi to dry karo is program ka?
is program ka solution is file pe nahi hai, balki next file mai hai


