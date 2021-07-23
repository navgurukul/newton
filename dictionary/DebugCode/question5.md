```ngMeta
name:  Question 5

```


aapko iss code mai  a name ki key hai uski values ka sum karna hai , b name ki key ka sum karna hai aur c name ki key ka sum karna hai. 

Iska output aisa hona chahiye :-   

{'a': 400, 'b': 400, 'c': 700, 'd': 450}.`



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

