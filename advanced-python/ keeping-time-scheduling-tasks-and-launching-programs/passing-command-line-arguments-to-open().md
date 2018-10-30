```ngMeta
name: passing-command-line-arguments-to-open()
completionMethod: manual
```
# Passing Command Line Arguments to Popen()
You can pass command line arguments to processes you create with Popen(). To do so, you pass a list as the sole argument to Popen(). The first string in this list will be the executable filename of the program you want to launch; all the subsequent strings will be the command line arguments to pass to the program when it starts. In effect, this list will be the value of sys.argv for the launched program.

Most applications with a graphical user interface (GUI) don’t use command line arguments as extensively as command line–based or terminal-based programs do. But most GUI applications will accept a single argument for a file that the applications will immediately open when they start. For example, if you’re using Windows, create a simple text file called C:\hello.txt and then enter the following into the interactive shell:

```python
>>> subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
```
<subprocess.Popen object at 0x00000000032DCEB8>
This will not only launch the Notepad application but also have it immediately open the C:\hello.txt file.

