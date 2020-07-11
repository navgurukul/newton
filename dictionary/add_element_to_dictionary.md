```ngMeta
name:  Adding Elements to a  Dictionary
submission_type: url
```

## Adding Elements to a  Dictionary:-

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
   	 

## Key Exists or not

Dictionary mai key exists karti hai ya nahi check karne ke liye hum in keyword ka use karte hai.


```python
car ={
	"brand":  "ford",
	"model":  "mustang",
	"year":  1964
}
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary.")

else:
    print("No, 'model' key dictionary mai nahi hai.")
 ```

`Output :- `

`Yes, 'model' is one of the keys in the thisdict dictionary.`
