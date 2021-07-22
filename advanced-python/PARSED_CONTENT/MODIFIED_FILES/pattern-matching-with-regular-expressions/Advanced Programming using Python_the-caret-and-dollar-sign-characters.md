```ngMeta
the-caret-and-dollar-sign-characters_key1
```

the-caret-and-dollar-sign-characters_key2
the-caret-and-dollar-sign-characters_key3


the-caret-and-dollar-sign-characters_key4


```python
>>> beginsWithHello = re.compile(r'^Hello')
>>> beginsWithHello.search('Hello world!')
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> beginsWithHello.search('He said hello.') == None
True
```
the-caret-and-dollar-sign-characters_key5


```python
>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your number is 42')
<_sre.SRE_Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty two.') == None
True
```
the-caret-and-dollar-sign-characters_key6


```python
>>> wholeStringIsNum = re.compile(r'^\d+$')
>>> wholeStringIsNum.search('1234567890')
<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
>>> wholeStringIsNum.search('12345xyz67890') == None
True
>>> wholeStringIsNum.search('12 34567890') == None
True
```
the-caret-and-dollar-sign-characters_key7


the-caret-and-dollar-sign-characters_key8
