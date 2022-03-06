writing-to-files_key1
writing-to-files_key2


writing-to-files_key3


writing-to-files_key4


writing-to-files_key5


```python
>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.write('Hello world!\n')
```
writing-to-files_key6
```python
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a')
>>> baconFile.write('Bacon is not a vegetable.')
```
writing-to-files_key7
```python
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
```
writing-to-files_key8


writing-to-files_key9


writing-to-files_key10
