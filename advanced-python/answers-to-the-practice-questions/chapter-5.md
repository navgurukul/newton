```ngMeta
name: chapter-5
completionMethod: manual
```
# Chapter 5
Two curly brackets: {}

{'foo': 42}

The items stored in a dictionary are unordered, while the items in a list are ordered.

You get a KeyError error.

There is no difference. The in operator checks whether a value exists as a key in the dictionary.

'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

spam.setdefault('color', 'black')

pprint.pprint()