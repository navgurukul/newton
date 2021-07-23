```ngMeta
finding-patterns-of-text-with-regular-expressions_key1
```

finding-patterns-of-text-with-regular-expressions_key2
finding-patterns-of-text-with-regular-expressions_key3


finding-patterns-of-text-with-regular-expressions_key4


finding-patterns-of-text-with-regular-expressions_key5


finding-patterns-of-text-with-regular-expressions_key6
finding-patterns-of-text-with-regular-expressions_key7


```python
>>> import re
```
finding-patterns-of-text-with-regular-expressions_key8


finding-patterns-of-text-with-regular-expressions_key9


finding-patterns-of-text-with-regular-expressions_key10


```python
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```
finding-patterns-of-text-with-regular-expressions_key11


finding-patterns-of-text-with-regular-expressions_key12


finding-patterns-of-text-with-regular-expressions_key13


finding-patterns-of-text-with-regular-expressions_key14


finding-patterns-of-text-with-regular-expressions_key15
finding-patterns-of-text-with-regular-expressions_key16


```python
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
```
finding-patterns-of-text-with-regular-expressions_key17


finding-patterns-of-text-with-regular-expressions_key18


finding-patterns-of-text-with-regular-expressions_key19
finding-patterns-of-text-with-regular-expressions_key20


finding-patterns-of-text-with-regular-expressions_key21


finding-patterns-of-text-with-regular-expressions_key22


finding-patterns-of-text-with-regular-expressions_key23


finding-patterns-of-text-with-regular-expressions_key24


finding-patterns-of-text-with-regular-expressions_key25
finding-patterns-of-text-with-regular-expressions_key26
