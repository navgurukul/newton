```ngMeta
name: Ideas for Similar Programs
completionMethod: manual
```
#Ideas for Similar Programs
There are many other reasons why you might want to rename a large number of files.

To add a prefix to the start of the filename, such as adding spam_ to rename eggs.txt to spam_eggs.txt

To change filenames with European-style dates to American-style dates

To remove the zeros from files such as spam0042.txt

Project: Backing Up a Folder into a ZIP File
Say you’re working on a project whose files you keep in a folder named C:\AlsPythonBook. You’re worried about losing your work, so you’d like to create ZIP file “snapshots” of the entire folder. You’d like to keep different versions, so you want the ZIP file’s filename to increment each time it is made; for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip, AlsPythonBook_3.zip, and so on. You could do this by hand, but it is rather annoying, and you might accidentally misnumber the ZIP files’ names. It would be much simpler to run a program that does this boring task for you.

For this project, open a new file editor window and save it as backupToZip.py.

#Step 1: Figure Out the ZIP File’s Name
The code for this program will be placed into a function named backupToZip(). This will make it easy to copy and paste the function into other Python programs that need this functionality. At the end of the program, the function will be called to perform the backup. Make your program look like this:


   #! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

❶ import zipfile, os

   def backupToZip(folder):
       # Backup the entire contents of "folder" into a ZIP file.

       folder = os.path.abspath(folder) # make sure folder is absolute

       # Figure out the filename this code should use based on
       # what files already exist.
❷     number = 1
❸     while True:
           zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
           if not os.path.exists(zipFilename):
               break
           number = number + 1

❹     # TODO: Create the ZIP file.

       # TODO: Walk the entire folder tree and compress the files in each folder.
       print('Done.')

   backupToZip('C:\\delicious')
Do the basics first: Add the shebang (#!) line, describe what the program does, and import the zipfile and os modules ❶.

Define a backupToZip() function that takes just one parameter, folder. This parameter is a string path to the folder whose contents should be backed up. The function will determine what filename to use for the ZIP file it will create; then the function will create the file, walk the folder folder, and add each of the subfolders and files to the ZIP file. Write TODO comments for these steps in the source code to remind yourself to do them later ❹.

The first part, naming the ZIP file, uses the base name of the absolute path of folder. If the folder being backed up is C:\delicious, the ZIP file’s name should be delicious_N.zip, where N = 1 is the first time you run the program, N = 2 is the second time, and so on.

You can determine what N should be by checking whether delicious_1.zip already exists, then checking whether delicious_2.zip already exists, and so on. Use a variable named number for N ❷, and keep incrementing it inside the loop that calls os.path.exists() to check whether the file exists ❸. The first nonexistent filename found will cause the loop to break, since it will have found the filename of the new zip.

#Step 2: Create the New ZIP File
Next let’s create the ZIP file. Make your program look like the following:


   #! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

   --snip--
       while True:
           zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
           if not os.path.exists(zipFilename):
               break
           number = number + 1
```python
       # Create the ZIP file.
       print('Creating %s...' % (zipFilename))
❶     backupZip = zipfile.ZipFile(zipFilename, 'w')
```
       # TODO: Walk the entire folder tree and compress the files in each folder.
       print('Done.')

   backupToZip('C:\\delicious')
Now that the new ZIP file’s name is stored in the zipFilename variable, you can call zipfile.ZipFile() to actually create the ZIP file ❶. Be sure to pass 'w' as the second argument so that the ZIP file is opened in write mode.

#Step 3: Walk the Directory Tree and Add to the ZIP File
Now you need to use the os.walk() function to do the work of listing every file in the folder and its subfolders. Make your program look like the following:


   #! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

   --snip--
```python
       # Walk the entire folder tree and compress the files in each folder.
❶     for foldername, subfolders, filenames in os.walk(folder):
           print('Adding files in %s...' % (foldername))
           # Add the current folder to the ZIP file.
❷         backupZip.write(foldername)
           # Add all the files in this folder to the ZIP file.
❸         for filename in filenames:
               newBase = os.path.basename(folder) + '_'
               if filename.startswith(newBase) and filename.endswith('.zip'):
                   continue   # don't backup the backup ZIP files
               backupZip.write(os.path.join(foldername, filename))
       backupZip.close()
```
       print('Done.')


   backupToZip('C:\\delicious')
You can use os.walk() in a for loop ❶, and on each iteration it will return the iteration’s current folder name, the subfolders in that folder, and the filenames in that folder.

In the for loop, the folder is added to the ZIP file ❷. The nested for loop can go through each filename in the filenames list ❸. Each of these is added to the ZIP file, except for previously made backup ZIPs.

When you run this program, it will produce output that will look something like this:


Creating delicious_1.zip...
Adding files in C:\delicious...
Adding files in C:\delicious\cats...
Adding files in C:\delicious\waffles...
Adding files in C:\delicious\walnut...
Adding files in C:\delicious\walnut\waffles...
Done.
The second time you run it, it will put all the files in C:\delicious into a ZIP file named delicious_2.zip, and so on.
#Ideas for Similar Programs
You can walk a directory tree and add files to compressed ZIP archives in several other programs. For example, you can write programs that do the following:

Walk a directory tree and archive just files with certain extensions, such as .txt or .py, and nothing else

Walk a directory tree and archive every file except the .txt and .py ones

Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space

Summary
Even if you are an experienced computer user, you probably handle files manually with the mouse and keyboard. Modern file explorers make it easy to work with a few files. But sometimes you’ll need to perform a task that would take hours using your computer’s file explorer.

The os and shutil modules offer functions for copying, moving, renaming, and deleting files. When deleting files, you might want to use the send2trash module to move files to the recycle bin or trash rather than permanently deleting them. And when writing programs that handle files, it’s a good idea to comment out the code that does the actual copy/move/ rename/delete and add a print() call instead so you can run the program and verify exactly what it will do.

Often you will need to perform these operations not only on files in one folder but also on every folder in that folder, every folder in those folders, and so on. The os.walk() function handles this trek across the folders for you so that you can concentrate on what your program needs to do with the files in them.

The zipfile module gives you a way of compressing and extracting files in .zip archives through Python. Combined with the file-handling functions of os and shutil, zipfile makes it easy to package up several files from anywhere on your hard drive. These .zip files are much easier to upload to websites or send as email attachments than many separate files.

Previous chapters of this book have provided source code for you to copy. But when you write your own programs, they probably won’t come out perfectly the first time. The next chapter focuses on some Python modules that will help you analyze and debug your programs so that you can quickly get them working correctly.


