```ngMeta
name:  Iteration
submission_type: url
```

## Iterate through all keys:-
 
  ```python
states_capitals = {
    'Gujarat' : 'Gandhinagar',
    'Maharashtra' : 'Mumbai',
    'Rajasthan' : 'Jaipur',
    'Bihar' : 'Patna'
    }
for state in states_capitals:
    	print(state)
 ```

*Output:-*
`Gujarat Maharashtra Rajasthan Bihar`


## Iterate through all values:-

`Example :-`

```python 
states_capitals = {
    'Gujarat' : 'Gandhinagar',
    'Maharashtra' : 'Mumbai',
    'Rajasthan' : 'Jaipur',
    'Bihar' : 'Patna'
    }
    
for state in states_capitals:
    print(states_capitals[state])
 ```

*Output :-*
   ` Gandhinagar
   	 Mumbai
   	 Jaipur
   	 Patna`

`Example :-`


```python
details ={
	"name":  "Bijender",
	"age":  17,
	"class":  "10th"
	}
for x in details.values():
	print(x)
 ```


`Output: `


`17
Bijender
10th
`


`Example  :-`

How to print *keys* and *values* together from a dictionary?


```python
movie ={
	"name":  "Puli",
	"hero":  "Vijay",
	"rating":  7.5
	}
for x,y in movie.items():
	print(x,y)
 ```

`Output :-`

`('rating', 7.5)
('hero', 'Vijay')
('name', 'Puli')
`
   

## Dictionary length

We use **Dictionary length** to find the number of items/key value pairs in a dictionary.

`Example:- `


```python
meal ={
	"monday":  "Chole chawal",
	"sunday":  "Fried rice",
	"wednesday":  "dosa"
	}
print(len(meal))
 ```

*Output :-*
   `3`
