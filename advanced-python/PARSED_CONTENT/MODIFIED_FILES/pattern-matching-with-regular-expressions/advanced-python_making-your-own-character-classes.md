```ngMeta
making-your-own-character-classes_key1
```
# making-your-own-character-classes_key2
making-your-own-character-classes_key3

```python
>>> vowelRegex = re.compile(r'[aeiouAEIOU]')
>>> vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```
making-your-own-character-classes_key4

making-your-own-character-classes_key5\.making-your-own-character-classes_key6```python
>>> consonantRegex = re.compile(r'[^aeiouAEIOU]')
>>> consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```
making-your-own-character-classes_key7