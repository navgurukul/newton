```ngMeta
name:  Question 3
submission_type: url
```

What would be the output of the below code snippet ?


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

