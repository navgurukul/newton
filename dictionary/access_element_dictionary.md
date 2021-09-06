```ngMeta
name:  Accessing Elements from a Dictionary
submission_type: url
```


## `Accessing` Elements from a Dictionary:-


We can `access` dictionary values with the use of square brackets. Look at the example below to understand.

#### Example :-

```python
person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:'organisation'}

result = person['age'] 
x = person.get("gender")
print(person[4])
print(x)
print(result)
 ```
    
#### Output :-

`organisation male 20 ` 

### `get()` :-
We can also make use of the **get()** function to access dictionary values.
 

#### Example :-
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
   
#### Output :-
```
male 
{'organisation': 'navgurukul', 'place': 'dharamsala'}
 dharamsala
```
   	 
