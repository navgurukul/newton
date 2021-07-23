```ngMeta
the-os-path-module_key1
```

the-os-path-module_key2
the-os-path-module_key3


the-os-path-module_key4


the-os-path-module_key5
the-os-path-module_key6


the-os-path-module_key7


the-os-path-module_key8


the-os-path-module_key9


the-os-path-module_key10


```python
>>> os.path.abspath('.')
'C:\\Python34'
>>> os.path.abspath('.\\Scripts')
'C:\\Python34\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True
```
the-os-path-module_key11


the-os-path-module_key12


the-os-path-module_key13


```python
>>> os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'
>>> os.getcwd() 'C:\\Python34'
```
the-os-path-module_key14


the-os-path-module_key15


```python
>>> path = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(path)
'calc.exe'
>>> os.path.dirname(path)
'C:\\Windows\\System32'
```
the-os-path-module_key16


```python
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
```
the-os-path-module_key17


```python
>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
```
the-os-path-module_key18


the-os-path-module_key19


the-os-path-module_key20


```python
>>> calcFilePath.split(os.path.sep)
```
the-os-path-module_key21


```python
>>> '/usr/bin'.split(os.path.sep)
```
the-os-path-module_key22
