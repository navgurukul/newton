```ngMeta
checking-whether-a-key-or-value-exists-in-a-dictionary_key1
```
# checking-whether-a-key-or-value-exists-in-a-dictionary_key2
checking-whether-a-key-or-value-exists-in-a-dictionary_key3

```python
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False
```
checking-whether-a-key-or-value-exists-in-a-dictionary_key4

# checking-whether-a-key-or-value-exists-in-a-dictionary_key5
checking-whether-a-key-or-value-exists-in-a-dictionary_key6

checking-whether-a-key-or-value-exists-in-a-dictionary_key7

```python
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'
```
checking-whether-a-key-or-value-exists-in-a-dictionary_key8

```python
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
KeyError: 'eggs'
The setdefault() Method
```
checking-whether-a-key-or-value-exists-in-a-dictionary_key9

```python
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
```
checking-whether-a-key-or-value-exists-in-a-dictionary_key10

```python
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
```
checking-whether-a-key-or-value-exists-in-a-dictionary_key11

checking-whether-a-key-or-value-exists-in-a-dictionary_key12

```python
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
```
checking-whether-a-key-or-value-exists-in-a-dictionary_key13


checking-whether-a-key-or-value-exists-in-a-dictionary_key14

