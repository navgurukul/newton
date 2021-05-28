```ngMeta
finding-file-sizes-and-folder-contents_key1
```
# finding-file-sizes-and-folder-contents_key2
finding-file-sizes-and-folder-contents_key3

finding-file-sizes-and-folder-contents_key4

finding-file-sizes-and-folder-contents_key5

finding-file-sizes-and-folder-contents_key6

```python
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
```
finding-file-sizes-and-folder-contents_key7```python
>>> os.listdir('C:\\Windows\\System32')
```
finding-file-sizes-and-folder-contents_key8

```python
>>> totalSize = 0
>>> for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

>>> print(totalSize)
```
finding-file-sizes-and-folder-contents_key9

# finding-file-sizes-and-folder-contents_key10
finding-file-sizes-and-folder-contents_key11

finding-file-sizes-and-folder-contents_key12

finding-file-sizes-and-folder-contents_key13

finding-file-sizes-and-folder-contents_key14

finding-file-sizes-and-folder-contents_key15

```python
>>> os.path.exists('C:\\Windows')
True
>>> os.path.exists('C:\\some_made_up_folder')
False
>>> os.path.isdir('C:\\Windows\\System32')
True
>>> os.path.isfile('C:\\Windows\\System32')
False
>>> os.path.isdir('C:\\Windows\\System32\\calc.exe')
False
>>> os.path.isfile('C:\\Windows\\System32\\calc.exe')
True
```
finding-file-sizes-and-folder-contents_key16

```python
>>> os.path.exists('D:\\')
```
finding-file-sizes-and-folder-contents_key17

