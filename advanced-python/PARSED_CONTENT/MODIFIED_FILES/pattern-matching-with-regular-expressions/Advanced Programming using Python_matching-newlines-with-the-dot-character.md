```ngMeta
matching-newlines-with-the-dot-character_key1
```

matching-newlines-with-the-dot-character_key2
matching-newlines-with-the-dot-character_key3


matching-newlines-with-the-dot-character_key4


```python
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.'
>>> newlineRegex = re.compile('.*', re.DOTALL)
>>> newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'
```
matching-newlines-with-the-dot-character_key5
