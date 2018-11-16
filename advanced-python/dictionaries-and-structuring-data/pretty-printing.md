```ngMeta
name: pretty-printing
completionMethod: manual
```
# Pretty Printing
If you import the pprint module into your programs, you’ll have access to the pprint() and pformat() functions that will “pretty print” a dictionary’s values. This is helpful when you want a cleaner display of the items in a dictionary than what print() provides. Modify the previous characterCount.py program and save it as prettyCharacterCount.py.

```python
import pprint
message = 'It was a bright cold day in April, and the clocks were striking'
thirteen.
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
```
This time, when the program is run, the output looks much cleaner, with the keys sorted.


{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.

If you want to obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat() instead. These two lines are equivalent to each other:


pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))