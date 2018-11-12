```ngMeta
name: opening-files-with-default-applications
completionMethod: manual
```
# Opening Files with Default Applications
Double-clicking a .txt file on your computer will automatically launch the application associated with the .txt file extension. Your computer will have several of these file extension associations set up already. Python can also open files this way with Popen().

Each operating system has a program that performs the equivalent of double-clicking a document file to open it. On Windows, this is the start program. On OS X, this is the open program. On Ubuntu Linux, this is the see program. Enter the following into the interactive shell, passing 'start', 'open', or 'see' to Popen() depending on your system:

```python
>>> fileObj = open('hello.txt', 'w')
>>> fileObj.write('Hello world!')
```
12
```python
>>> fileObj.close()
>>> import subprocess
>>> subprocess.Popen(['start', 'hello.txt'], shell=True)
```
Here we write Hello world! to a new hello.txt file. Then we call Popen(), passing it a list containing the program name (in this example, 'start' for Windows) and the filename. We also pass the shell=True keyword argument, which is needed only on Windows. The operating system knows all of the file associations and can figure out that it should launch, say, Notepad.exe to handle the hello.txt file.

On OS X, the open program is used for opening both document files and programs. Enter the following into the interactive shell if you have a Mac:

```python
>>> subprocess.Popen(['open', '/Applications/Calculator.app/'])
<subprocess.Popen object at 0x10202ff98>
```
The Calculator app should open.

# The UNIX Philosophy

Programs well designed to be launched by other programs become more powerful than their code alone. The Unix philosophy is a set of software design principles established by the programmers of the Unix operating system (on which the modern Linux and OS X are built). It says that it’s better to write small, limited-purpose programs that can interoperate, rather than large, feature-rich applications. The smaller programs are easier to understand, and by being interoperable, they can be the building blocks of much more powerful applications.

Smartphone apps follow this approach as well. If your restaurant app needs to display directions to a café, the developers didn’t reinvent the wheel by writing their own map code. The restaurant app simply launches a map app while passing it the café’s address, just as your Python code would call a function and pass it arguments.

The Python programs you’ve been writing in this book mostly fit the Unix philosophy, especially in one important way: They use command line arguments rather than input() function calls. If all the information your program needs can be supplied up front, it is preferable to have this information passed as command line arguments rather than waiting for the user to type it in. This way, the command line arguments can be entered by a human user or supplied by another program. This interoperable approach will make your programs reusable as part of another program.

The sole exception is that you don’t want passwords passed as command line arguments, since the command line may record them as part of its command history feature. Instead, your program should call the input() function when it needs you to enter a password.

You can read more about Unix philosophy at <span><a href=" https://en.wikipedia.org/wiki/Unix_philosophy/."> https://en.wikipedia.org/wiki/Unix_philosophy/.</a></span>