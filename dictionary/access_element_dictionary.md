```ngMeta
name:  Accessing Elements from a Dictionary:-
submission_type: url
```


### Accessing Elements from a Dictionary:-


Hum square brackets ka use karke dictionary ke values ko access kar sakte hain. Jaisa ki niche dikhaya gaya hai.

**Example 1:-**

```python
person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:'organisation'}

result = person['age'] 
print(person[4])
print(result)
 ```
    
*Output:-*

`organisation 20 ` 

**Example 2:-**
```python
person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:{
        'organisation':'navgurukul','place':'dharamsala'
        }
    }
print(person['gender'])

print(person[4])

result = person[4]['place']

print(result)
 ```
   
*Output:-*
`  male {'organisation': 'navgurukul', 'place': 'dharamsala'}
 dharamsala
`
   	 
