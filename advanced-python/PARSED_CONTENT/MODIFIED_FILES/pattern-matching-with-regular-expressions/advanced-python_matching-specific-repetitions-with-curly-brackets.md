```ngMeta
matching-specific-repetitions-with-curly-brackets_key1
```
# matching-specific-repetitions-with-curly-brackets_key2
matching-specific-repetitions-with-curly-brackets_key3

matching-specific-repetitions-with-curly-brackets_key4

matching-specific-repetitions-with-curly-brackets_key5


matching-specific-repetitions-with-curly-brackets_key6


matching-specific-repetitions-with-curly-brackets_key7

```python
>>> haRegex = re.compile(r'(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'

>>> mo2 = haRegex.search('Ha')
>>> mo2 == None
True
```
matching-specific-repetitions-with-curly-brackets_key8

# matching-specific-repetitions-with-curly-brackets_key9
matching-specific-repetitions-with-curly-brackets_key10

matching-specific-repetitions-with-curly-brackets_key11

matching-specific-repetitions-with-curly-brackets_key12

```python
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
```
matching-specific-repetitions-with-curly-brackets_key13