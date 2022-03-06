```ngMeta
name: copying-and-pasting-strings-with-the-pyperclip-mo
```
# Copying and Pasting Strings with the pyperclip Module
The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard. Sending the output of your program to the clipboard will make it easy to paste it to an email, word processor, or some other software.

Pyperclip does not come with Python. To install it, follow the directions for installing third-party modules in Appendix A. After installing the pyperclip module, enter the following into the interactive shell:

```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()
'Hello world!'
```
Of course, if something outside of your program changes the clipboard contents, the paste() function will return it. For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:

```python
>>> pyperclip.paste()
```
'For example, if I copied this sentence to the clipboard and then called
paste(), it would look like this:'
Running Python Scripts Outside of IDLE

So far, you’ve been running your Python scripts using the interactive shell and file editor in IDLE. However, you won’t want to go through the inconvenience of opening IDLE and the Python script each time you want to run a script. Fortunately, there are shortcuts you can set up to make running Python scripts easier. The steps are slightly different for Windows, OS X, and Linux, but each is described in Appendix B. Turn to Appendix B to learn how to run your Python scripts conveniently and be able to pass command line arguments to them. (You will not be able to pass command line arguments to your programs using IDLE.)

# Project: Password Locker
You probably have accounts on many different websites. It’s a bad habit to use the same password for each of them because if any of those sites has a security breach, the hackers will learn the password to all of your other accounts. It’s best to use password manager software on your computer that uses one master password to unlock the password manager. Then you can copy any account password to the clipboard and paste it into the website’s Password field.

The password manager program you’ll create in this example isn’t secure, but it offers a basic demonstration of how such programs work.

# The Chapter Projects

This is the first “chapter project” of the book. From here on, each chapter will have projects that demonstrate the concepts covered in the chapter. The projects are written in a style that takes you from a blank file editor window to a full, working program. Just like with the interactive shell examples, don’t only read the project sections—follow along on your computer!

# Step 1: Program Design and Data Structures
You want to be able to run this program with a command line argument that is the account’s name—for instance, email or blog. That account’s password will be copied to the clipboard so that the user can paste it into a Password field. This way, the user can have long, complicated passwords without having to memorize them.

Open a new file editor window and save the program as pw.py. You need to start the program with a #! (shebang) line (see Appendix B) and should also write a comment that briefly describes the program. Since you want to associate each account’s name with its password, you can store these as strings in a dictionary. The dictionary will be the data structure that organizes your account and password data. Make your program look like the following:


#! python3
# pw.py - An insecure password locker program.
```python
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
```
# Step 2: Handle Command Line Arguments
The command line arguments will be stored in the variable sys.argv. (See Appendix B for more information on how to use command line arguments in your programs.) The first item in the sys.argv list should always be a string containing the program’s filename ('pw.py'), and the second item should be the first command line argument. For this program, this argument is the name of the account whose password you want. Since the command line argument is mandatory, you display a usage message to the user if they forget to add it (that is, if the sys.argv list has fewer than two values in it). Make your program look like the following:


#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
```python
import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name
```
# Step 3: Copy the Right Password
Now that the account name is stored as a string in the variable account, you need to see whether it exists in the PASSWORDS dictionary as a key. If so, you want to copy the key’s value to the clipboard using pyperclip.copy(). (Since you’re using the pyperclip module, you need to import it.) Note that you don’t actually need the account variable; you could just use sys.argv[1] everywhere account is used in this program. But a variable named account is much more readable than something cryptic like sys.argv[1].

Make your program look like the following:


#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
```python
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
```
This new code looks in the PASSWORDS dictionary for the account name. If the account name is a key in the dictionary, we get the value corresponding to that key, copy it to the clipboard, and print a message saying that we copied the value. Otherwise, we print a message saying there’s no account with that name.

That’s the complete script. Using the instructions in Appendix B for launching command line programs easily, you now have a fast way to copy your account passwords to the clipboard. You will have to modify the PASSWORDS dictionary value in the source whenever you want to update the program with a new password.

Of course, you probably don’t want to keep all your passwords in one place where anyone could easily copy them. But you can modify this program and use it to quickly copy regular text to the clipboard. Say you are sending out several emails that have many of the same stock paragraphs in common. You could put each paragraph as a value in the PASSWORDS dictionary (you’d probably want to rename the dictionary at this point), and then you would have a way to quickly select and copy one of many standard pieces of text to the clipboard.

On Windows, you can create a batch file to run this program with the WIN-R Run window. (For more about batch files, see Appendix B.) Type the following into the file editor and save the file as pw.bat in the C:\Windows folder:


@py.exe C:\Python34\pw.py %*
@pause
With this batch file created, running the password-safe program on Windows is just a matter of pressing WIN-R and typing pw <account name>.

