```ngMeta
name: augmented-assignment-operators
completionMethod: manual
```
# Augmented Assignment Operators
When assigning a value to a variable, you will frequently use the variable itself. For example, after assigning 42 to the variable spam, you would increase the value in spam by 1 with the following code:

```python
>>> spam = 42
>>> spam = spam + 1
>>> spam
43
```
As a shortcut, you can use the augmented assignment operator += to do the same thing:

```python
>>> spam = 42
>>> spam += 1
>>> spam
43
```
There are augmented assignment operators for the +, -, *, /, and % operators, described in Table 4-1.
Table 4-1. The Augmented Assignment Operators
Augmented assignment statement
Equivalent assignment statement
```python
spam += 1		spam = spam + 1

spam -= 1		spam = spam - 1

spam *= 1		spam = spam * 1

spam /= 1		spam = spam / 1

spam %= 1		spam = spam % 1
```
The += operator can also do string and list concatenation, and the *= operator can do string and list replication. Enter the following into the interactive shell:
```python
>>> spam = 'Hello'
>>> spam += ' world!'
>>> spam
'Hello world!'

>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
```