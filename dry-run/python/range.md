```ngMeta
name: Understanding Range Function
```

Range is a very important Python function. 

```python
range(x, y)
```

se
```python
[x, x+1, x+2, .... , y-1]
```

`array/list` declare hoti hai. 

Jaise humne `range(3,5)` likha toh isse `[3,4]` tak ka array generate hoga.

Aksar hum bas `range(x)` jaisa kuch likhenge. Yeh `range(0,x)` ke sabse closest hota hai. Toh `range(5)` se `[0,1,2,3,4]` list generate hoti hai.

Jab hum 

```python
for i in range(5):
    print i
```

toh batayie kya hoga?