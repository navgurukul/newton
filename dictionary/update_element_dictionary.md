```ngMeta
name:   Update Dictionary
submission_type: url
```

## Updating Dictionary :-
To update dictionary ,we can make an entry in it or we can add a key-value pair or we can change the value of an existing key.As given in the example explained below:-

**Example 1:-**

```python
person= {'1': 'RAM', '2': 17,}
person[3] = 'male'
print(person)
 ```

*Output:-*
` {'1': 'RAM', '2': 17,'3':'male'}`

**Example 2-**

```python
details={
    'Name': 'RAM',
     'Age': 17, 
     'student': {
      'id': 22,
      'place': 'dharamsala'
      }
     } 
details['student']['id']=35
print(details); 
 ```
   	 
*Output:-*

`{'Name': 'RAM', 'Age': 17, 'student': {'id': 35, 'place': 'dharamsala'}}`




## Copy of Dictionary :- 


We can copy a dictionary in two ways,first method is using `copy()` and second method by using built-in function `dict()`.


`Example 1 :-`

```python
classes ={
	"room1":  "6th",
	"room2":  "7th",
	"room3":  "8th"
		}
mydict=classes.copy()
print(mydict)
 ```

*Output:-*

`{'room2': '7th', 'room3': '8th', 'room1': '6th}'`

If we write, mydict=dict(classes) in example 1,it will also give the same result as you can see below.

 ```python
classes ={
	"room1":  "6th",
	"room2":  "7th",
	"room3":  "8th"
		}
mydict=dict(classes)
print(mydict)
 ```
*Output:-*

`{'room2': '7th', 'room3': '8th', 'room1': '6th}'`