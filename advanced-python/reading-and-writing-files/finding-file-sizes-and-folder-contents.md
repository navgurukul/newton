```ngMeta
name: finding-file-sizes-and-folder-contents
```
# Finding File Sizes and Folder Contents
Once you have ways of handling file paths, you can then start gathering information about specific files and folders. The os.path module provides functions for finding the size of a file in bytes and the files and folders inside a given folder.

Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.

Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)

Here’s what I get when I try these functions in the interactive shell:

```python
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
```
776192
```python
>>> os.listdir('C:\\Windows\\System32')
```
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--snip--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
As you can see, the calc.exe program on my computer is 776,192 bytes in size, and I have a lot of files in C:\Windows\system32. If I want to find the total size of all the files in this directory, I can use os.path.getsize() and os.listdir() together.

```python
>>> totalSize = 0
>>> for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

>>> print(totalSize)
```
1117846456
As I loop over each filename in the C:\Windows\System32 folder, the totalSize variable is incremented by the size of each file. Notice how when I call os.path.getsize(), I use os.path.join() to join the folder name with the current filename. The integer that os.path.getsize() returns is added to the value of totalSize. After looping through all the files, I print totalSize to see the total size of the C:\Windows\System32 folder.

# Checking Path Validity
Many Python functions will crash with an error if you supply them with a path that does not exist. The os.path module provides functions to check whether a given path exists and whether it is a file or folder.

Calling os.path.exists(path) will return True if the file or folder referred to in the argument exists and will return False if it does not exist.

Calling os.path.isfile(path) will return True if the path argument exists and is a file and will return False otherwise.

Calling os.path.isdir(path) will return True if the path argument exists and is a folder and will return False otherwise.

Here’s what I get when I try these functions in the interactive shell:

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
You can determine whether there is a DVD or flash drive currently attached to the computer by checking for it with the os.path.exists() function. For instance, if I wanted to check for a flash drive with the volume named D:\ on my Windows computer, I could do that with the following:

```python
>>> os.path.exists('D:\\')
```
False
Oops! It looks like I forgot to plug in my flash drive.

