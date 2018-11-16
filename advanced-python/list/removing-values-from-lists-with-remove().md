```ngMeta
name: removing-values-from-lists-with-remove()
completionMethod: manual
```	
# Removing Values from Lists with remove()
The remove() method is passed the value to be removed from the list it is called on. Enter the following into the interactive shell:

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
```
Attempting to delete a value that does not exist in the list will result in a ValueError error. For example, enter the following into the interactive shell and notice the error that is displayed:

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('chicken')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    spam.remove('chicken')
ValueError: list.remove(x): x not in list
```
If the value appears multiple times in the list, only the first instance of the value will be removed. Enter the following into the interactive shell:

```python
>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
```
The del statement is good to use when you know the index of the value you want to remove from the list. The remove() method is good when you know the value you want to remove from the list.

