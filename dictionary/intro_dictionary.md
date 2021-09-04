```ngMeta
name: Introduction to Dictionary
submission_type: url
```

## Dictionary


### Definition :-

To create a dictionary we put in the `key value pairs` in a comma separated form inside `curly brackets { }` and use the `colon ":"` to assign values to keys`.

#### Example:-

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

#### Output :-

```python
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

## `Keys Case Sensitive` :-


Dictionary keys should be `case sensitive`, means we can write `keys` with same names but different case. Python treats them as different `keys`.

#### Example:-

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

// KeyError tab aati hai jab key dictionay mai nahi hoti hai.
 ```

In the dictionary, *dict* , *ball* a key which has value *"green"*, similarly *"Ball"* is another key which has value *"red"*.

### dict() function

You can create a dictionary using the `dict()` function.

#### Example:-

```python
student=dict(name= "Ravina",age= 20)
print(student)
 ```

#### Output:-

`{'age': 20, 'name': 'Ravina'}`


### DataType of `Keys` and `Values`

A *"dictionary"*  can have values of any data type and can also be same, but keys are always to be unique.


#### Example:- 

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




### `Nested Dictionary` :-



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
#### Output :-

`{1: 'NAVGURUKUL', 2: 'IN', 3: {'A': 'WELCOME', 'B': 'To', 'C': 'DHARAMSALA'}}`

@[youtube](https://www.youtube.com/watch?v=daefaLgNkw0)

@[youtube](https://www.youtube.com/watch?v=0g1ogNP5doA)