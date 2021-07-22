```ngMeta
reading-and-writing-files_key1
```

reading-and-writing-files_key2
reading-and-writing-files_key3


reading-and-writing-files_key4
reading-and-writing-files_key5


![image](assets/000027.jpg)reading-and-writing-files_key6


reading-and-writing-files_key7


reading-and-writing-files_key8


reading-and-writing-files_key9
reading-and-writing-files_key10


reading-and-writing-files_key11


```python
>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'
```
reading-and-writing-files_key12


reading-and-writing-files_key13


```python
>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
        print(os.path.join('C:\\Users\\asweigart', filename))
```
reading-and-writing-files_key14
