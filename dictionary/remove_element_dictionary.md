```ngMeta
name:  Removing Elements from a Dictionary
submission_type: url
```
   	 
## Removing Elements from a Dictionary:-

 We can remove dictionary elements by many methods. 
Like given below.

### `pop()` :-

Using the **pop( )** method we can remove a specified element from the dictionary.



```python
CAR_DETAILS={
    "brand": "Ford",
    "model": "jason",
    "year": 1964
}
CAR_DETAILS.pop("model")
print(CAR_DETAILS)
 ```
    
#### Output:-

`{'brand': 'Ford', 'year': 1964}`

### `popitem()`:-

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
#### Output:-

`{'name':'jack','id':22}`

### `del` :-

Using the **del** keyword we can remove a specified element from the dictionary.

```python
person={
    'name':'jack',
    'id':22,
    'place':'dharamsala'
}

del person('place')
print(person)
 ```

#### Output:-

`{'name':'jack','id':22}`
   	 
   	 
