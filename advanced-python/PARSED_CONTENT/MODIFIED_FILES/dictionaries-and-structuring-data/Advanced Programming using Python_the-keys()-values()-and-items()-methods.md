the-keys()-values()-and-items()-methods_key1
the-keys()-values()-and-items()-methods_key2


```python
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
        print(v)

red
42
Here, a for loop iterates over each of the values in the spam dictionary. A for loop can also iterate over the keys or both keys and values:


>>> for k in spam.keys():
        print(k)

color
age
>>> for i in spam.items():
        print(i)

('color', 'red')
('age', 42)
```
the-keys()-values()-and-items()-methods_key3


the-keys()-values()-and-items()-methods_key4


```python
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
```
the-keys()-values()-and-items()-methods_key5


the-keys()-values()-and-items()-methods_key6


```python
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))

Key: age Value: 42
Key: color Value: red
```