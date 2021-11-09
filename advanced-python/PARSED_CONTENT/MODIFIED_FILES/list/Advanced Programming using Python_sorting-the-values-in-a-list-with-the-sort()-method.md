sorting-the-values-in-a-list-with-the-sort()-method_key1
sorting-the-values-in-a-list-with-the-sort()-method_key2


```python
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
```
sorting-the-values-in-a-list-with-the-sort()-method_key3


```python
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
```
sorting-the-values-in-a-list-with-the-sort()-method_key4


sorting-the-values-in-a-list-with-the-sort()-method_key5


```python
>>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
 File "<pyshell#70>", line 1, in <module>
   spam.sort()
TypeError: unorderable types: str() < int()
```
sorting-the-values-in-a-list-with-the-sort()-method_key6


```python
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```
sorting-the-values-in-a-list-with-the-sort()-method_key7


```python
>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']
```
sorting-the-values-in-a-list-with-the-sort()-method_key8


sorting-the-values-in-a-list-with-the-sort()-method_key9
sorting-the-values-in-a-list-with-the-sort()-method_key10


```python
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
```
sorting-the-values-in-a-list-with-the-sort()-method_key11


sorting-the-values-in-a-list-with-the-sort()-method_key12


```python
spam = ['apples',
    'oranges',
                     'bananas',
'cats']
print(spam)
```
sorting-the-values-in-a-list-with-the-sort()-method_key13


sorting-the-values-in-a-list-with-the-sort()-method_key14


```python
print('Four score and seven ' + \
      'years ago...')
```
sorting-the-values-in-a-list-with-the-sort()-method_key15


sorting-the-values-in-a-list-with-the-sort()-method_key16


sorting-the-values-in-a-list-with-the-sort()-method_key17
