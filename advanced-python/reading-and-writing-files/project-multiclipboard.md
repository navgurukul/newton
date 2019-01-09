```ngMeta
name: project-multiclipboard
```
# Project: Multiclipboard
Say you have the boring task of filling out many forms in a web page or software with several text fields. The clipboard saves you from typing the same text over and over again. But only one thing can be on the clipboard at a time. If you have several different pieces of text that you need to copy and paste, you have to keep highlighting and copying the same few things over and over again.

You can write a Python program to keep track of multiple pieces of text. This “multiclipboard” will be named mcb.pyw (since “mcb” is shorter to type than “multiclipboard”). The .pyw extension means that Python won’t show a Terminal window when it runs this program. (See Appendix B for more details.)

The program will save each piece of clipboard text under a keyword. For example, when you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam. This text can later be loaded to the clipboard again by running py mcb.pyw spam. And if the user forgets what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard.

Here’s what the program does:

The command line argument for the keyword is checked.

If the argument is save, then the clipboard contents are saved to the keyword.

If the argument is list, then all the keywords are copied to the clipboard.

Otherwise, the text for the keyword is copied to the clipboard.

This means the code will need to do the following:

Read the command line arguments from sys.argv.

Read and write to the clipboard.

Save and load to a shelf file.

If you use Windows, you can easily run this script from the Run... window by creating a batch file named mcb.bat with the following content:


@pyw.exe C:\Python34\mcb.pyw %*
# Step 1: Comments and Shelf Setup
Let’s start by making a skeleton script with some comments and basic setup. Make your code look like the following:


   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
❶ # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

❷ import shelve, pyperclip, sys

❸ mcbShelf = shelve.open('mcb')

   # TODO: Save clipboard content.

   # TODO: List keywords and load content.
```python
   mcbShelf.close()
```
It’s common practice to put general usage information in comments at the top of the file ❶. If you ever forget how to run your script, you can always look at these comments for a reminder. Then you import your modules ❷. Copying and pasting will require the pyperclip module, and reading the command line arguments will require the sys module. The shelve module will also come in handy: Whenever the user wants to save a new piece of clipboard text, you’ll save it to a shelf file. Then, when the user wants to paste the text back to their clipboard, you’ll open the shelf file and load it back into your program. The shelf file will be named with the prefix mcb ❸.

# Step 2: Save Clipboard Content with a Keyword
The program does different things depending on whether the user wants to save text to a keyword, load text into the clipboard, or list all the existing keywords. Let’s deal with that first case. Make your code look like the following:


   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --snip--
```python
   # Save clipboard content.

❶ if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
❷         mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
```
❸    # TODO: List keywords and load content.

   mcbShelf.close()
If the first command line argument (which will always be at index 1 of the sys.argv list) is 'save' ❶, the second command line argument is the keyword for the current content of the clipboard. The keyword will be used as the key for mcbShelf, and the value will be the text currently on the clipboard ❷.

If there is only one command line argument, you will assume it is either 'list' or a keyword to load content onto the clipboard. You will implement that code later. For now, just put a TODO comment there ❸.

# Step 3: List Keywords and Load a Keyword’s Content
Finally, let’s implement the two remaining cases: The user wants to load clipboard text in from a keyword, or they want a list of all available keywords. Make your code look like the following:


   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --snip--

   # Save clipboard content.
   if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
           mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
```python
       # List keywords and load content.
❶     if sys.argv[1].lower() == 'list':
❷         pyperclip.copy(str(list(mcbShelf.keys())))
       elif sys.argv[1] in mcbShelf:
❸         pyperclip.copy(mcbShelf[sys.argv[1]])
```
   mcbShelf.close()
If there is only one command line argument, first let’s check whether it’s 'list' ❶. If so, a string representation of the list of shelf keys will be copied to the clipboard ❷. The user can paste this list into an open text editor to read it.

Otherwise, you can assume the command line argument is a keyword. If this keyword exists in the mcbShelf shelf as a key, you can load the value onto the clipboard ❸.

And that’s it! Launching this program has different steps depending on what operating system your computer uses. See Appendix B for details for your operating system.

Recall the password locker program you created in Chapter 6 that stored the passwords in a dictionary. Updating the passwords required changing the source code of the program. This isn’t ideal because average users don’t feel comfortable changing source code to update their software. Also, every time you modify the source code to a program, you run the risk of accidentally introducing new bugs. By storing the data for a program in a different place than the code, you can make your programs easier for others to use and more resistant to bugs.

# Summary
Files are organized into folders (also called directories), and a path describes the location of a file. Every program running on your computer has a current working directory, which allows you to specify file paths relative to the current location instead of always typing the full (or absolute) path. The os.path module has many functions for manipulating file paths.

Your programs can also directly interact with the contents of text files. The open() function can open these files to read in their contents as one large string (with the read() method) or as a list of strings (with the readlines() method). The open() function can open files in write or append mode to create new text files or add to existing text files, respectively.

In previous chapters, you used the clipboard as a way of getting large amounts of text into a program, rather than typing it all in. Now you can have your programs read files directly from the hard drive, which is a big improvement, since files are much less volatile than the clipboard.

In the next chapter, you will learn how to handle the files themselves, by copying them, deleting them, renaming them, moving them, and more.