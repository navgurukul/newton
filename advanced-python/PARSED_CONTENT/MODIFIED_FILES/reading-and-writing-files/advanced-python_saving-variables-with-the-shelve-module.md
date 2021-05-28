```ngMeta
saving-variables-with-the-shelve-module_key1
```
# saving-variables-with-the-shelve-module_key2
saving-variables-with-the-shelve-module_key3

saving-variables-with-the-shelve-module_key4

```python
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```
saving-variables-with-the-shelve-module_key5

saving-variables-with-the-shelve-module_key6

saving-variables-with-the-shelve-module_key7

saving-variables-with-the-shelve-module_key8

```python
>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
```
saving-variables-with-the-shelve-module_key9

saving-variables-with-the-shelve-module_key10

```python
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()
```
saving-variables-with-the-shelve-module_key11

# saving-variables-with-the-shelve-module_key12
saving-variables-with-the-shelve-module_key13

saving-variables-with-the-shelve-module_key14

```python
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()
```
saving-variables-with-the-shelve-module_key15

saving-variables-with-the-shelve-module_key16

saving-variables-with-the-shelve-module_key17

```python
>>> import myCats
>>> myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
>>> myCats.cats[0]['name']
'Zophie'
```
saving-variables-with-the-shelve-module_key18

