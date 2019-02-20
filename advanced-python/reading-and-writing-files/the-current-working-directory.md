```ngMeta
name: the-current-working-directory
```
# The Current Working Directory
Every program that runs on your computer has a current working directory, or cwd. Any filenames or paths that do not begin with the root folder are assumed to be under the current working directory. You can get the current working directory as a string value with the os.getcwd() function and change it with os.chdir(). Enter the following into the interactive shell:

```python
>>> import os
>>> os.getcwd()
'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')
>>> os.getcwd()
'C:\\Windows\\System32'
```
Here, the current working directory is set to C:\Python34, so the filename project.docx refers to C:\Python34\project.docx. When we change the current working directory to C:\Windows, project.docx is interpreted as C:\ Windows\project.docx.

Python will display an error if you try to change to a directory that does not exist.

```python
>>> os.chdir('C:\\ThisFolderDoesNotExist')
```
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    os.chdir('C:\\ThisFolderDoesNotExist')
FileNotFoundError: [WinError 2] The system cannot find the file specified:
'C:\\ThisFolderDoesNotExist'

# Note
While folder is the more modern name for directory, note that current working directory (or just working directory) is the standard term, not current working folder.