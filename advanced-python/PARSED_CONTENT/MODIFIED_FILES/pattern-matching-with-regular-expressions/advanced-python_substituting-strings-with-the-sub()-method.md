```ngMeta
substituting-strings-with-the-sub()-method_key1
```
# substituting-strings-with-the-sub()-method_key2
substituting-strings-with-the-sub()-method_key3

substituting-strings-with-the-sub()-method_key4

```python
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```
substituting-strings-with-the-sub()-method_key5

substituting-strings-with-the-sub()-method_key6

```python
>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent'
Eve knew Agent Bob was a double agent.')'
```
substituting-strings-with-the-sub()-method_key7

