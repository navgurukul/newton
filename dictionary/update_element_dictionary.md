```ngMeta
name:   Update Dictionary
submission_type: url
```

### Updating Dictionary :-

Hum dictionary ko update karne ke liye usme ek entry kar sakte hai ya fir key-value pair add kar sakte hai aur jo key pehle se present hai uski value change kar sakte hai. Jaisa ki niche example me dikhaya gaya hain.

**Example 1:-**

```python
person= {'1': 'RAM', '2': 17,}
person[3] = 'male'
print(person)
 ```
*Output:-*
` {'1': 'Abhi', '2': 17,'3':'male'}`

**Example 2-**

```python
details={
    'Name': 'RAM',
     'Age': 17, 
     'student': {'id': 22, 'place': 'dharamsala'}
     } 
details['student']['id']=35
print(details); 
 ```
   	 
*Output:-*

`{'Name': 'RAM', 'Age': 17, 'student': {'id': 35, 'place': 'dharamsala'}}`




