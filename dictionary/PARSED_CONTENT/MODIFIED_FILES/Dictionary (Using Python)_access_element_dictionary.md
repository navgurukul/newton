```ngMeta
access_element_dictionary_key1
```

access_element_dictionary_key2
access_element_dictionary_key3


access_element_dictionary_key4


```python
person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:'organisation'}

result = person['age'] 
x = person.get("gender")
print(person[4])
print(x)
print(result)
```
    
access_element_dictionary_key5


access_element_dictionary_key6


access_element_dictionary_key7


access_element_dictionary_key8
```python
person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:{
        'organisation':'navgurukul','place':'dharamsala'
        }
    }
print(person['gender'])

print(person[4])

result = person[4]['place']

print(result)
```
   
access_element_dictionary_key9
