```ngMeta
name: The shutil Module
completionMethod: manual
```
#The shutil Module
The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs. To use the shutil functions, you will first need to use import shutil.

Copying Files and Folders
The shutil module provides functions for copying files, as well as entire folders.

Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination. (Both source and destination are strings.) If destination is a filename, it will be used as the new name of the copied file. This function returns a string of the path of the copied file.

Enter the following into the interactive shell to see how shutil.copy() works:

```python
   >>> import shutil, os
   >>> os.chdir('C:\\')
❶ >>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
```
   'C:\\delicious\\spam.txt'
```python
❷ >>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
```
   'C:\\delicious\\eggs2.txt'
The first shutil.copy() call copies the file at C:\spam.txt to the folder C:\delicious. The return value is the path of the newly copied file. Note that since a folder was specified as the destination ❶, the original spam.txt filename is used for the new, copied file’s filename. The second shutil.copy() call ❷ also copies the file at C:\eggs.txt to the folder C:\delicious but gives the copied file the name eggs2.txt.

While shutil.copy() will copy a single file, shutil.copytree() will copy an entire folder and every folder and file contained in it. Calling shutil.copytree(source, destination) will copy the folder at the path source, along with all of its files and subfolders, to the folder at the path destination. The source and destination parameters are both strings. The function returns a string of the path of the copied folder.

Enter the following into the interactive shell:

```python
>>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
```
'C:\\bacon_backup'
The shutil.copytree() call creates a new folder named bacon_backup with the same content as the original bacon folder. You have now safely backed up your precious, precious bacon.