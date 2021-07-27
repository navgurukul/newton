```ngMeta
name: Introduction to Dictionary
submission_type: url
```

# DICTIONARY  


## DEFINITION :-
To create a dictionary we put in the key value pairs in a comma separated form inside curly brackets "{ } and use the colon ":" to assign values to keys.

**Example:-**

```python 
city_population = {
    "NewYorkCity":8550405,
    "LosAngeles":3971883, 
    "Toronto":2731571, 
    "Chicago":2720546, 
    "Houston":2296224, 
    "Montreal":1704694, 
    "Calgary":1239220, 
    "Vancouver":631486, 
    "Boston":667137
}

print(city_population["NewYorkCity"])
print(city_population)
print(type(city_population))
 ```

`Output`

```
8550405

{
   "NewYorkCity":8550405,
    "LosAngeles":3971883, 
    "Toronto":2731571, 
    "Chicago":2720546, 
    "Houston":2296224, 
    "Montreal":1704694, 
    "Calgary":1239220, 
    "Vancouver":631486, 
    "Boston":667137
}

<type 'dict'>
 ```

## Keys Case Sensitive :-

Keys in a dictionary are case sensitive meaning that keys with same name but different cases will be treated as unique keys by python.

**Example:-** 

```python

 Dict = {
       'ball' : 'green',
       'Ball': 'red'
     }
print(Dict['ball'])
print(Dict['Ball'])
print(Dict['bat'])
```

```
green
red
KeyError: bat

// KeyError occurs when a key is not present in a dictionary.
 ```
 
 In the dictionary *dict* *"ball"* is a key which has value *"green"*, similarly *"Ball"* is another key which has value *"red"*


## dict() function

You can create a dictionary using the dict() function.

`Example:-`

```python
student=dict(name= "Ravina",age= 20)
print(student)
 ```

`Output:- `

`{'age': 20, 'name': 'Ravina'}`


## DataType of Keys and Values

A *"dictionary"*  can have values of any data type and can also be same, but keys are alway to be unique.

**Example:-** 

*dictionary with integer keys:-*


```python
   my_dict = {
    1: 'apple', 
    2: 'ball'
    }

```


*dictionary with mixed keys:-*

```python 
my_dict = {
    'name': 'John',
     1: [2, 4, 3]
    }
 ```




## Nested Dictionary:-



```python
Dic= {
 1: 'NAVGURUKUL',
 2: 'IN',  
 3:{
     'A' : 'WELCOME',
     'B' : 'To', 
     'C' : 'DHARAMSALA'
     }
}
print(Dic)
 ```
*Output :-*

`{1: 'NAVGURUKUL', 2: 'IN', 3: {'A': 'WELCOME', 'B': 'To', 'C': 'DHARAMSALA'}}`

@[youtube](https://www.youtube.com/watch?v=daefaLgNkw0)

@[youtube](https://www.youtube.com/watch?v=0g1ogNP5doA)
