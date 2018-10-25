```ngMeta
name: Reading ZIP Files
completionMethod: manual
```
# Reading ZIP Files
To read the contents of a ZIP file, first you must create a ZipFile object (note the capital letters Z and F). ZipFile objects are conceptually similar to the File objects you saw returned by the open() function in the previous chapter: They are values through which the program interacts with the file. To create a ZipFile object, call the zipfile.ZipFile() function, passing it a string of the .zip file’s filename. Note that zipfile is the name of the Python module, and ZipFile() is the name of the function.

For example, enter the following into the interactive shell:

```python
   >>> import zipfile, os
   >>> os.chdir('C:\\')    # move to the folder with example.zip
   >>> exampleZip = zipfile.ZipFile('example.zip')
   >>> exampleZip.namelist()
   ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
   >>> spamInfo = exampleZip.getinfo('spam.txt')
   >>> spamInfo.file_size
   13908
   >>> spamInfo.compress_size
   3828
❶ >>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
   .compress_size, 2))
   'Compressed file is 3.63x smaller!'
   >>> exampleZip.close()
```
A ZipFile object has a namelist() method that returns a list of strings for all the files and folders contained in the ZIP file. These strings can be passed to the getinfo() ZipFile method to return a ZipInfo object about that particular file. ZipInfo objects have their own attributes, such as file_size and compress_size in bytes, which hold integers of the original file size and compressed file size, respectively. While a ZipFile object represents an entire archive file, a ZipInfo object holds useful information about a single file in the archive.

The command at ❶ calculates how efficiently example.zip is compressed by dividing the original file size by the compressed file size and prints this information using a string formatted with %s.

Extracting from ZIP Files
The extractall() method for ZipFile objects extracts all the files and folders from a ZIP file into the current working directory.

```python
   >>> import zipfile, os
   >>> os.chdir('C:\\')    # move to the folder with example.zip
   >>> exampleZip = zipfile.ZipFile('example.zip')
❶ >>> exampleZip.extractall()
   >>> exampleZip.close()
```
After running this code, the contents of example.zip will be extracted to C:\. Optionally, you can pass a folder name to extractall() to have it extract the files into a folder other than the current working directory. If the folder passed to the extractall() method does not exist, it will be created. For instance, if you replaced the call at ❶ with exampleZip.extractall('C:\\ delicious'), the code would extract the files from example.zip into a newly created C:\delicious folder.

The extract() method for ZipFile objects will extract a single file from the ZIP file. Continue the interactive shell example:

```python
>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
```
The string you pass to extract() must match one of the strings in the list returned by namelist(). Optionally, you can pass a second argument to extract() to extract the file into a folder other than the current working directory. If this second argument is a folder that doesn’t yet exist, Python will create the folder. The value that extract() returns is the absolute path to which the file was extracted.

# Creating and Adding to ZIP Files
To create your own compressed ZIP files, you must open the ZipFile object in write mode by passing 'w' as the second argument. (This is similar to opening a text file in write mode by passing 'w' to the open() function.)

When you pass a path to the write() method of a ZipFile object, Python will compress the file at that path and add it into the ZIP file. The write() method’s first argument is a string of the filename to add. The second argument is the compression type parameter, which tells the computer what algorithm it should use to compress the files; you can always just set this value to zipfile.ZIP_DEFLATED. (This specifies the deflate compression algorithm, which works well on all types of data.) Enter the following into the interactive shell:

```python
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
```
This code will create a new ZIP file named new.zip that has the compressed contents of spam.txt.

Keep in mind that, just as with writing to files, write mode will erase all existing contents of a ZIP file. If you want to simply add files to an existing ZIP file, pass 'a' as the second argument to zipfile.ZipFile() to open the ZIP file in append mode.