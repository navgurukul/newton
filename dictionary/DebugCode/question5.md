```ngMeta
name:  Question 5
submission_type: url
``` 

In this code you have to sum the values ​​of key with name a, key b and key c.

Its output should be like this:-  

`{'a': 400, 'b': 400, 'c': 700, 'd': 450}.`



```python
a={'a': 100, 'b': 200, 'c':300}
b={'a': 300, 'b': 200, 'c':400,"d":450}
c={}
for i in a:
	c=a[i]
for j in b:
	if j not in c:
		c[j]=b[j]
	else:
		c[j]+=b[j]
print(c)
 ```
