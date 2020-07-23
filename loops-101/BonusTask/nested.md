```ngMeta
name:  Nested While Loop
submission_type: url
```
Nested while loop woj hota hai jo loop ke andar loops hota hai.Usme phele andar wala loop run hota hai.Jab andar wala loop false ho jata hai tab woh bahar wala loop run karta aur yeh processes tab tak chata rehta hai jab tak bahar wale loop ki condition false nahi ho jati.

Example:-

```python
i = 1
j = 5
while i < 4:
    while j < 8:
        print(i, ",", j)
        j = j + 1
    i = i + 1
```
