```ngMeta
dump_key1
```
## dump_key2
**dump_key3**dump_key4

dump_key5
    
```python
import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
```
  
*dump_key6*

```python
out_file = open("myfile.json", "w")
  
json.dump(dict1, out_file, indent = 6)
  
out_file.close()
```
**dump_key7**dump_key8

*dump_key9*dump_key10

```python

import json

a={‘lalalala’: 3}
mystring = json.dumps(a)
print(mystring)

```