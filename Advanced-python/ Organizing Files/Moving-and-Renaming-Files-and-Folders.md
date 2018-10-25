```ngMeta
name: Moving and Renaming Files and Folders
completionMethod: manual
```
# Moving and Renaming Files and Folders
Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.

If destination points to a folder, the source file gets moved into destination and keeps its current filename. For example, enter the following into the interactive shell:

```python
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
```
'C:\\eggs\\bacon.txt'
Assuming a folder named eggs already exists in the C:\ directory, this shutil.move() calls says, “Move C:\bacon.txt into the folder C:\eggs.”

If there had been a bacon.txt file already in C:\eggs, it would have been overwritten. Since it’s easy to accidentally overwrite files in this way, you should take some care when using move().

The destination path can also specify a filename. In the following example, the source file is moved and renamed.

```python
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
```
'C:\\eggs\\new_bacon.txt'
This line says, “Move C:\bacon.txt into the folder C:\eggs, and while you’re at it, rename that bacon.txt file to new_bacon.txt.”

Both of the previous examples worked under the assumption that there was a folder eggs in the C:\ directory. But if there is no eggs folder, then move() will rename bacon.txt to a file named eggs.

```python
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
```
'C:\\eggs'
Here, move() can’t find a folder named eggs in the C:\ directory and so assumes that destination must be specifying a filename, not a folder. So the bacon.txt text file is renamed to eggs (a text file without the .txt file extension)—probably not what you wanted! This can be a tough-to-spot bug in your programs since the move() call can happily do something that might be quite different from what you were expecting. This is yet another reason to be careful when using move().

Finally, the folders that make up the destination must already exist, or else Python will throw an exception. Enter the following into the interactive shell:

```python
>>> shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
```
Traceback (most recent call last):
  File "C:\Python34\lib\shutil.py", line 521, in move
    os.rename(src, real_dst)
FileNotFoundError: [WinError 3] The system cannot find the path specified:
'spam.txt' -> 'c:\\does_not_exist\\eggs\\ham'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
  File "C:\Python34\lib\shutil.py", line 533, in move
    copy2(src, real_dst)
  File "C:\Python34\lib\shutil.py", line 244, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Python34\lib\shutil.py", line 108, in copyfile
    with open(dst, 'wb') as fdst:
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\does_not_exist\\
eggs\\ham'
Python looks for eggs and ham inside the directory does_not_exist. It doesn’t find the nonexistent directory, so it can’t move spam.txt to the path you specified.