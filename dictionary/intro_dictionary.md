```ngMeta
name: Introduction to Dictionary
submission_type: url
```

# DICTIONARY  


### DEFINITION :-

Hum dictionary banane ke liye key aur value ke pairs ko curly braces “{ }” me likhte hai aur har pair ko hum separate karne ke liye comma “,” ka use karte hai aur key ko uske nirdharit value ke saath likhne ke liye colon “:” ka use karte hain :
**Example:-**  
```python
data = {
        key1: value1,
   	key2: value2,
   	.
   	.
   	.
   	key N: value N

   	}
```  
### Keys Case Sensitive :-
Dictionary ki keys case sensitive hoti hain , matlab hum same name ki keys ko alag alag case me likh sakte hai aur python usko alag alag keys ki tarah treat karega.

**Example:-** 

```python

 Dict = {
       'ball' : 'green',
       'Ball': 'red'
     }
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

### Adding Elements to a  Dictionary:-

Python dictionary me hum ek baar me ek hi key-value add kar sakte hai aur add karne ke liye humein key ko square brackets “[ ]” me likhte hain aur uski value ko “=” operator ka use karke assign kar dete hain.

**Example 1:-** 
```python
dic= {
    'Name': 'RAM', 
    'Age': 17,
    }
    
dic['ORGANIZATION'] = "NAV GURUKUL"

dic['place'] = 'dharamsala'

print(dic)
 ```
*Output:- * 

`{'Name': 'RAM', 'Age': 17,'ORGANIZATION': 'NAVGURUKUL', 'place':'dharamsala}`


**Example 2:-**
   	 
 ```python   
dic= {
    'Name': 'RAM',
    'Age': 17,
     }

dic['student']={
    'id':22, 
    'place':'dharamsala'
    }
print(dic)
 ```
    
*Output:-*

`{'Name': 'RAM', 'Age': 17, 'student': {'id': 22, 'place': 'dharamsala'}}`
   	 

### UPDATING A DICTIONARY:-

Hum dictionary ko update karne ke liye usme ek entry kar sakte hai ya fir key-value pair add kar sakte hai aur jo key pehle se present hai uski value change kar sakte hai. Jaisa ki niche example me dikhaya gaya hain.

**Example 1:-**

```python
person= {'1': 'RAM', '2': 17,}
person[3] = 'male'
print(person)
 ```
*Output:-*
` {'1': 'Abhi', 2: 17,3:'male'}`

**Example 2-**

```python
details={
    'Name': 'RAM',
     'Age': 17, 
     'student': {'id': 22, 'place': 'dharamsala'}
     }   
 ```
   	 
   	 details['student']['id']=35
    OUTPUT:-
   	 {'Name': 'RAM', 'Age': 17, 'student': {'id': 35, 'place': 'dharamsala'}}
