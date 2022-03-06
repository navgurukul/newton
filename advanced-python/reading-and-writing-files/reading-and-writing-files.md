```ngMeta
name: reading-and-writing-files
```
# Reading and Writing Files
Variables are a fine way to store data while your program is running, but if you want your data to persist even after your program has finished, you need to save it to a file. You can think of a file’s contents as a single string value, potentially gigabytes in size. In this chapter, you will learn how to use Python to create, read, and save files on the hard drive.

# Files and File Paths
A file has two key properties: a filename (usually written as one word) and a path. The path specifies the location of a file on the computer. For example, there is a file on my Windows 7 laptop with the filename project.docx in the path C:\Users\asweigart\Documents. The part of the filename after the last period is called the file’s extension and tells you a file’s type. project.docx is a Word document, and Users, asweigart, and Documents all refer to folders (also called directories). Folders can contain files and other folders. For example, project.docx is in the Documents folder, which is inside the asweigart folder, which is inside the Users folder. Figure 8-1 shows this folder organization.

<!-- ![image](assets/000027.jpg)
 -->
A file in a hierarchy of folders

The C:\ part of the path is the root folder, which contains all other folders. On Windows, the root folder is named C:\ and is also called the C: drive. On OS X and Linux, the root folder is /. In this book, I’ll be using the Windows-style root folder, C:\. If you are entering the interactive shell examples on OS X or Linux, enter / instead.

Additional volumes, such as a DVD drive or USB thumb drive, will appear differently on different operating systems. On Windows, they appear as new, lettered root drives, such as D:\ or E:\. On OS X, they appear as new folders under the /Volumes folder. On Linux, they appear as new folders under the /mnt (“mount”) folder. Also note that while folder names and filenames are not case sensitive on Windows and OS X, they are case sensitive on Linux.

# Backslash on Windows and Forward Slash on OS X and Linux
On Windows, paths are written using backslashes (\) as the separator between folder names. OS X and Linux, however, use the forward slash (/) as their path separator. If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases.

Fortunately, this is simple to do with the os.path.join() function. If you pass it the string values of individual file and folder names in your path, os.path.join() will return a string with a file path using the correct path separators. Enter the following into the interactive shell:

```python
>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'
```
I’m running these interactive shell examples on Windows, so os.path.join('usr', 'bin', 'spam') returned 'usr\\bin\\spam'. (Notice that the backslashes are doubled because each backslash needs to be escaped by another backslash character.) If I had called this function on OS X or Linux, the string would have been 'usr/bin/spam'.

The os.path.join() function is helpful if you need to create strings for filenames. These strings will be passed to several of the file-related functions introduced in this chapter. For example, the following example joins names from a list of filenames to the end of a folder’s name:

```python
>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
        print(os.path.join('C:\\Users\\asweigart', filename))
```
C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv
C:\Users\asweigart\invite.docx