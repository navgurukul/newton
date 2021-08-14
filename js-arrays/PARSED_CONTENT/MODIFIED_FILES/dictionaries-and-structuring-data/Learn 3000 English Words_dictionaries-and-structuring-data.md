dictionaries-and-structuring-data_key1
dictionaries-and-structuring-data_key2


dictionaries-and-structuring-data_key3
dictionaries-and-structuring-data_key4


dictionaries-and-structuring-data_key5


```python
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
```
dictionaries-and-structuring-data_key6


```python
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
```
dictionaries-and-structuring-data_key7


```python
>>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}
```
dictionaries-and-structuring-data_key8


```python
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
```
dictionaries-and-structuring-data_key9


dictionaries-and-structuring-data_key10


```python
>>> spam = {'name': 'Zophie', 'age': 7}
>>> spam['color']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    spam['color']
KeyError: 'color'
```
dictionaries-and-structuring-data_key11


```python
❶ birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

   while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break

❷     if name in birthdays:
❸         print(birthdays[name] + ' is the birthday of ' + name)
       else:
           print('I do not have birthday information for ' + name)
           print('What is their birthday?')
           bday = input()
❹         birthdays[name] = bday
           print('Birthday database updated.')
```
dictionaries-and-structuring-data_key12


dictionaries-and-structuring-data_key13



dictionaries-and-structuring-data_key14
