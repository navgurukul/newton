```ngMeta
name:  Removing Elements from a Dictionary :-
submission_type: url
```
   	 
### Removing Elements from a Dictionary:-

Hum dictionary ke elements ko kahin tareeko se remove kar sakte hain.
Jaisa ki niche dikhaya gaya hain.

Hum **pop( )** method ka use karke specified element ko remove kar sakte hain :


```python
CAR_DETAILS={
    "brand": "Ford",
    "model": "jason",
    "year": 1964
}
CAR_DETAILS.pop("model")
print(CAR_DETAILS)
 ```
    
*Output:-*

` {'brand': 'Ford', 'year': 1964}`



The **popitem()** method removes the last inserted item:

```python
person={
    'name':'jack',
    'id':22,
    'place':'dharamsala'
}
person.popitem()
print(person)
 ```
*Output:-*

`{'name':'jack','id':22}`

Hum **del** keyword ka use karke kisi specified element ko delete kar sakte hain :

```python
person={
    'name':'jack',
    'id':22,
    'place':'dharamsala'
}

del person('place')
print(person)
 ```

*Output:-*

` {'name':'jack','id':22}`
   	 
   	 
