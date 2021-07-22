```ngMeta
the-startswith()-and-endswith()-string-methods_key1
```

the-startswith()-and-endswith()-string-methods_key2
the-startswith()-and-endswith()-string-methods_key3


```python
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True
```
the-startswith()-and-endswith()-string-methods_key4


the-startswith()-and-endswith()-string-methods_key5


```python
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```
the-startswith()-and-endswith()-string-methods_key6


the-startswith()-and-endswith()-string-methods_key7


```python
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```
the-startswith()-and-endswith()-string-methods_key8


```python
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```
the-startswith()-and-endswith()-string-methods_key9


```python
>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the'
fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.','
'Sincerely,', 'Bob']
```
the-startswith()-and-endswith()-string-methods_key10


the-startswith()-and-endswith()-string-methods_key11
```python
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'               Hello'
>>> 'Hello World'.rjust(20)
'         Hello World'
>>> 'Hello'.ljust(10)
'Hello     '
```
the-startswith()-and-endswith()-string-methods_key12


the-startswith()-and-endswith()-string-methods_key13


```python
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
```
the-startswith()-and-endswith()-string-methods_key14


```python
>>> 'Hello'.center(20)
'       Hello       '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```
the-startswith()-and-endswith()-string-methods_key15


```python
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```
the-startswith()-and-endswith()-string-methods_key16


the-startswith()-and-endswith()-string-methods_key17


the-startswith()-and-endswith()-string-methods_key18


the-startswith()-and-endswith()-string-methods_key19


the-startswith()-and-endswith()-string-methods_key20


the-startswith()-and-endswith()-string-methods_key21



the-startswith()-and-endswith()-string-methods_key22


the-startswith()-and-endswith()-string-methods_key23


```python
>>> spam = '    Hello World     '
>>> spam.strip()
'Hello World'
>>> spam.lstrip()
'Hello World '
>>> spam.rstrip()
'    Hello World'
```
the-startswith()-and-endswith()-string-methods_key24


```python
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
```
the-startswith()-and-endswith()-string-methods_key25
