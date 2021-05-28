```ngMeta
optional-matching-with-the-question-mark_key1
```
# optional-matching-with-the-question-mark_key2
optional-matching-with-the-question-mark_key3

```python
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
```
optional-matching-with-the-question-mark_key4

optional-matching-with-the-question-mark_key5

```python
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo1 = phoneRegex.search('My number is 415-555-4242')
>>> mo1.group()
'415-555-4242'

>>> mo2 = phoneRegex.search('My number is 555-4242')
>>> mo2.group()
'555-4242'
```
optional-matching-with-the-question-mark_key6

optional-matching-with-the-question-mark_key7\?optional-matching-with-the-question-mark_key8

# optional-matching-with-the-question-mark_key9
optional-matching-with-the-question-mark_key10

```python
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'

>>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'
```
optional-matching-with-the-question-mark_key11

optional-matching-with-the-question-mark_key12\*optional-matching-with-the-question-mark_key13

# optional-matching-with-the-question-mark_key14
optional-matching-with-the-question-mark_key15

```python
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'

>>> mo2 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'

>>> mo3 = batRegex.search('The Adventures of Batman')
>>> mo3 == None
True
```
optional-matching-with-the-question-mark_key16

optional-matching-with-the-question-mark_key17\+optional-matching-with-the-question-mark_key18

