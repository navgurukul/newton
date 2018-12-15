## Split function Solution



### Solution

Is solution ko sahi se samjho or btao ki galti kahan pe thi and hum usse kaise sahi kar sakte hai

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
	a.append(temp_s)
	return a
```

