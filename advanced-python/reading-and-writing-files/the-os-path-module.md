```ngMeta
name: the-os-path-module
```
# The os.path Module
The os.path module contains many helpful functions related to filenames and file paths. For instance, you’ve already used os.path.join() to build paths in a way that will work on any operating system. Since os.path is a module inside the os module, you can import it by simply running import os. Whenever your programs need to work with files, folders, or file paths, you can refer to the short examples in this section. The full documentation for the os.path module is on the Python website at<span><a href=" http://docs.python.org/3/library/os.path.html."> http://docs.python.org/3/library/os.path.html.</a></span>

Note
Most of the examples that follow in this section will require the os module, so remember to import it at the beginning of any script you write and any time you restart IDLE. Otherwise, you’ll get a NameError: name 'os' is not defined error message.

# Handling Absolute and Relative Paths
The os.path module provides functions for returning the absolute path of a relative path and for checking whether a given path is an absolute path.

Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.

Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.

Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

Try these functions in the interactive shell:

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
Since C:\Python34 was the working directory when os.path.abspath() was called, the “single-dot” folder represents the absolute path 'C:\\Python34'.

Note
Since your system probably has different files and folders on it than mine, you won’t be able to follow every example in this chapter exactly. Still, try to follow along using folders that exist on your computer.

Enter the following calls to os.path.relpath() into the interactive shell:

```python
>>> os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'
>>> os.getcwd() 'C:\\Python34'
```
Calling os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument. Calling os.path.basename(path) will return a string of everything that comes after the last slash in the path argument. The dir name and base name of a path are outlined in Figure
![](assets/000041.png)
 The base name follows the last slash in a path and is the same as the filename. The dir name is everything before the last slash.

For example, enter the following into the interactive shell:

```python
>>> path = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(path)
'calc.exe'
>>> os.path.dirname(path)
'C:\\Windows\\System32'
```
If you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple value with these two strings, like so:

```python
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
```
('C:\\Windows\\System32', 'calc.exe')
Notice that you could create the same tuple by calling os.path.dirname() and os.path.basename() and placing their return values in a tuple.

```python
>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
```
('C:\\Windows\\System32', 'calc.exe')
But os.path.split() is a nice shortcut if you need both values.

Also, note that os.path.split() does not take a file path and return a list of strings of each folder. For that, use the split() string method and split on the string in os.sep. Recall from earlier that the os.sep variable is set to the correct folder-separating slash for the computer running the program.

For example, enter the following into the interactive shell:

```python
>>> calcFilePath.split(os.path.sep)
```
['C:', 'Windows', 'System32', 'calc.exe']
On OS X and Linux systems, there will be a blank string at the start of the returned list:

```python
>>> '/usr/bin'.split(os.path.sep)
```
['', 'usr', 'bin']
The split() string method will work to return a list of each part of the path. It will work on any operating system if you pass it os.path.sep.

