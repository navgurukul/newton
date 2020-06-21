```ngMeta
name: Introduction to Dictionary
submission_type: url
```

# DICTIONARY  


### DEFINITION :-

Hum dictionary banane ke liye key aur value ke pairs ko curly braces “{ }” me likhte hai aur har pair ko hum separate karne ke liye comma “,” ka use karte hai aur key ko uske nirdharit value ke saath likhne ke liye colon “:” ka use karte hain :

**Example:-**

```python 
city_population = {
    "NewYorkCity":8550405,
    "LosAngeles":3971883,          "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137
}

print(city_population["New York City"])
print(city_population)
print(type city_population)
 ```

`Output`

```
2731571


{'Toronto': 2731571, 'Houston': 2296224, 'Vancouver': 631486, 'Los Angeles': 3971883, 'Chicago': 2720546, 'Calgary': 1239220, 'New York City': 8550405, 'Boston': 667137, 'Montreal': 1704694}


<type 'dict'>
 ```

### Keys Case Sensitive :-

Dictionary ki keys case sensitive hoti hain , matlab hum same name ki keys ko alag alag case me likh sakte hai aur python usko alag alag keys ki tarah treat karega.

**Example:-** 

```python

 Dict = {
       'ball' : 'green',
       'Ball': 'red'
     }
print(Dict['ball'])
print(Dict['bat'])
```

```
green
KeyError: bat

 ```
*Dict* me *“ball”* ek key hai aur *“green”* uski value hai. Isi tarah *“Ball”* dusri key hai aur *“red”* uski value hain.


### DataType of Keys and Values

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




### Nested Dictionary:-



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

