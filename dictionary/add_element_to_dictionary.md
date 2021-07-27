```ngMeta
name:  Adding Elements to a  Dictionary
submission_type: url
```

## Adding Elements to a  Dictionary:-

In a python dictionary we can add only one key value pair at a time. To add to a dictionary we make mention the key inside square brackets "[ ]" and use the "=" operator to assign a value.

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

We use the 'in' keyword to check whether a given key exists or not in a dictionary.

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
