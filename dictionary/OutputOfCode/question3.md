```ngMeta
name:  Question 3
submission_type: url
```

Niche diye gye code snippet ki output kya hoga?


```python

fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print (len(fruit))
print(fruit)
 ```

