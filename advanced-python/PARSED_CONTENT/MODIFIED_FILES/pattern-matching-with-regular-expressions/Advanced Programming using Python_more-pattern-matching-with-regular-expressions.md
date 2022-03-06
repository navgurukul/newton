more-pattern-matching-with-regular-expressions_key1
more-pattern-matching-with-regular-expressions_key2


more-pattern-matching-with-regular-expressions_key3
more-pattern-matching-with-regular-expressions_key4


more-pattern-matching-with-regular-expressions_key5


```python
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'
```
more-pattern-matching-with-regular-expressions_key6


```python
>>> mo.groups()
('415', '555-4242')
>>> areaCode, mainNumber = mo.groups()
>>> print(areaCode)
415
>>> print(mainNumber)
555-4242
```
more-pattern-matching-with-regular-expressions_key7


more-pattern-matching-with-regular-expressions_key8


```python
>>> phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
>>> mo.group(1)
'(415)'
>>> mo.group(2)
'555-4242'
```
more-pattern-matching-with-regular-expressions_key9


more-pattern-matching-with-regular-expressions_key10
more-pattern-matching-with-regular-expressions_key11


more-pattern-matching-with-regular-expressions_key12


```python
>>> heroRegex = re.compile (r'Batman|Tina Fey')
>>> mo1 = heroRegex.search('Batman and Tina Fey.')
>>> mo1.group()
'Batman'

>>> mo2 = heroRegex.search('Tina Fey and Batman.')
>>> mo2.group()
'Tina Fey'
```
more-pattern-matching-with-regular-expressions_key13
more-pattern-matching-with-regular-expressions_key14


more-pattern-matching-with-regular-expressions_key15


```python
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
```
more-pattern-matching-with-regular-expressions_key16


more-pattern-matching-with-regular-expressions_key17
