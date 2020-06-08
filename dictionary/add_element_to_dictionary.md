```ngMeta
name:  Adding Elements to a  Dictionary
submission_type: url
```

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
   	 

