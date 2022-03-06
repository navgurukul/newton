```ngMeta
name: the-file-reading-process
```
# The File Reading/Writing Process
Once you are comfortable working with folders and relative paths, you’ll be able to specify the location of files to read and write. The functions covered in the next few sections will apply to plaintext files. Plaintext files contain only basic text characters and do not include font, size, or color information. Text files with the .txt extension or Python script files with the .py extension are examples of plaintext files. These can be opened with Windows’s Notepad or OS X’s TextEdit application. Your programs can easily read the contents of plaintext files and treat them as an ordinary string value.

Binary files are all other file types, such as word processing documents, PDFs, images, spreadsheets, and executable programs. If you open a binary file in Notepad or TextEdit, it will look like scrambled nonsense, like in Figure 8-5.

 The Windows calc.exe program opened in Notepad
Figure 8-5. The Windows calc.exe program opened in Notepad

Since every different type of binary file must be handled in its own way, this book will not go into reading and writing raw binary files directly. Fortunately, many modules make working with binary files easier—you will explore one of them, the shelve module, later in this chapter.

There are three steps to reading or writing files in Python.

Call the open() function to return a File object.

Call the read() or write() method on the File object.

Close the file by calling the close() method on the File object.

# Opening Files with the open() Function
To open a file with the open() function, you pass it a string path indicating the file you want to open; it can be either an absolute or relative path. The open() function returns a File object.

Try it by creating a text file named hello.txt using Notepad or TextEdit. Type Hello world! as the content of this text file and save it in your user home folder. Then, if you’re using Windows, enter the following into the interactive shell:

```python
>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')
```
If you’re using OS X, enter the following into the interactive shell instead:

```python
>>> helloFile = open('/Users/your_home_folder/hello.txt')
```
Make sure to replace your_home_folder with your computer username. For example, my username is asweigart, so I’d enter 'C:\\Users\\asweigart\\ hello.txt' on Windows.

Both these commands will open the file in “reading plaintext” mode, or read mode for short. When a file is opened in read mode, Python lets you only read data from the file; you can’t write or modify it in any way. Read mode is the default mode for files you open in Python. But if you don’t want to rely on Python’s defaults, you can explicitly specify the mode by passing the string value 'r' as a second argument to open(). So open('/Users/asweigart/ hello.txt', 'r') and open('/Users/asweigart/hello.txt') do the same thing.

The call to open() returns a File object. A File object represents a file on your computer; it is simply another type of value in Python, much like the lists and dictionaries you’re already familiar with. In the previous example, you stored the File object in the variable helloFile. Now, whenever you want to read from or write to the file, you can do so by calling methods on the File object in helloFile.

# Reading the Contents of Files
Now that you have a File object, you can start reading from it. If you want to read the entire contents of a file as a string value, use the File object’s read() method. Let’s continue with the hello.txt File object you stored in helloFile. Enter the following into the interactive shell:

```python
>>> helloContent = helloFile.read()
>>> helloContent
```
'Hello world!'
If you think of the contents of a file as a single large string value, the read() method returns the string that is stored in the file.

Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text. For example, create a file named sonnet29.txt in the same directory as hello.txt and write the following text in it:


When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
Make sure to separate the four lines with line breaks. Then enter the following into the interactive shell:

```python
>>> sonnetFile = open('sonnet29.txt')
>>> sonnetFile.readlines()
```
[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
look upon myself and curse my fate,']
Note that each of the string values ends with a newline character, \n, except for the last line of the file. A list of strings is often easier to work with than a single large string value.