```ngMeta
review-of-regex-symbols_key1
```
# review-of-regex-symbols_key2
review-of-regex-symbols_key3

review-of-regex-symbols_key4

review-of-regex-symbols_key5

review-of-regex-symbols_key6

review-of-regex-symbols_key7

review-of-regex-symbols_key8

review-of-regex-symbols_key9

review-of-regex-symbols_key10

review-of-regex-symbols_key11# review-of-regex-symbols_key12
review-of-regex-symbols_key13```python
>>> regex1 = re.compile('Robocop')
>>> regex2 = re.compile('ROBOCOP')
>>> regex3 = re.compile('robOcop')
>>> regex4 = re.compile('RobocOp')
```
review-of-regex-symbols_key14```python
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('Robocop is part man, part machine, all cop.').group()
'Robocop'

>>> robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

>>> robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'
```
