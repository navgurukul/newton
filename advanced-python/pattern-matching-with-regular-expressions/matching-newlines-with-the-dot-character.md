```ngMeta
name: matching-newlines-with-the-dot-character
```
# Matching Newlines with the Dot Character
The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.

Enter the following into the interactive shell:

```python
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.'
>>> newlineRegex = re.compile('.*', re.DOTALL)
>>> newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'
```
The regex noNewlineRegex, which did not have re.DOTALL passed to the re.compile() call that created it, will match everything only up to the first newline character, whereas newlineRegex, which did have re.DOTALL passed to re.compile(), matches everything. This is why the newlineRegex.search() call matches the full string, including its newline characters.