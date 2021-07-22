```ngMeta
name: Introduction to Dictionary

```

# DICTIONARY  


## DEFINITION :-

Hum dictionary banane ke liye key aur value ke pairs ko curly braces “{ }” me likhte hai aur har pair ko hum separate karne ke liye comma “,” ka use karte hai aur key ko uske nirdharit value ke saath likhne ke liye colon “:” ka use karte hain :

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

Dictionary ki keys case sensitive hoti hain , matlab hum same name ki keys ko alag alag case me likh sakte hai aur python usko alag alag keys ki tarah treat karega.

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

// KeyError tab aati hai jab key dictionay mai nahi hoti hai.
 ```
*Dict* me *“ball”* ek key hai aur *“green”* uski value hai. Isi tarah *“Ball”* dusri key hai aur *“red”* uski value hain.



## dict() function

Aap dict() ka use kar ke dictionary bana sakte hai

`Example:-`

```python
student=dict(name= "Ravina",age= 20)
print(student)
 ```

`Output:- `

`{'age': 20, 'name': 'Ravina'}`


## DataType of Keys and Values

Ek *dictionary* me values kisi bhi datatype ke ho sakte hain aur ye same bhi ho sakti hai lekin keys humesha unique hoti hai.

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