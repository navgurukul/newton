```ngMeta
name: Permanently Deleting Files and Folders
completionMethod: manual
```
# Permanently Deleting Files and Folders
You can delete a single file or a single empty folder with functions in the os module, whereas to delete a folder and all of its contents, you use the shutil module.

Calling os.unlink(path) will delete the file at path.

Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.

Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

Be careful when using these functions in your programs! It’s often a good idea to first run your program with these calls commented out and with print() calls added to show the files that would be deleted. Here is a Python program that was intended to delete files that have the .txt file extension but has a typo (highlighted in bold) that causes it to delete .rxt files instead:


import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
If you had any important files ending with .rxt, they would have been accidentally, permanently deleted. Instead, you should have first run the program like this:


import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
Now the os.unlink() call is commented, so Python ignores it. Instead, you will print the filename of the file that would have been deleted. Running this version of the program first will show you that you’ve accidentally told the program to delete .rxt files instead of .txt files.

Once you are certain the program works as intended, delete the print(filename) line and uncomment the os.unlink(filename) line. Then run the program again to actually delete the files.