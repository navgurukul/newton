```ngMeta
name: aunching-other-programs-from-python
completionMethod: manual
```
# Launching Other Programs from Python
Your Python program can start other programs on your computer with the Popen() function in the built-in subprocess module. (The P in the name of the Popen() function stands for process.) If you have multiple instances of an application open, each of those instances is a separate process of the same program. For example, if you open multiple windows of your web browser at the same time, each of those windows is a different process of the web browser program. See Figure 15-1 for an example of multiple calculator processes open at once.

Every process can have multiple threads. Unlike threads, a process cannot directly read and write another process’s variables. If you think of a multithreaded program as having multiple fingers following source code, then having multiple processes of the same program open is like having a friend with a separate copy of the program’s source code. You are both independently executing the same program.

If you want to start an external program from your Python script, pass the program’s filename to subprocess.Popen(). (On Windows, right-click the application’s Start menu item and select Properties to view the application’s filename. On OS X, CTRL-click the application and select Show Package Contents to find the path to the executable file.) The Popen() function will then immediately return. Keep in mind that the launched program is not run in the same thread as your Python program.

<!-- ![image](assets/000013.jpg) -->

Figure 15-1. Six running processes of the same calculator program

On a Windows computer, enter the following into the interactive shell:

```python
>>> import subprocess
>>> subprocess.Popen('C:\\Windows\\System32\\calc.exe')
```
<subprocess.Popen object at 0x0000000003055A58>
On Ubuntu Linux, you would enter the following:
```python
>>> import subprocess
>>> subprocess.Popen('/usr/bin/gnome-calculator')
```
<subprocess.Popen object at 0x7f2bcf93b20>
On OS X, the process is slightly different. See Opening Files with Default Applications.

The return value is a Popen object, which has two useful methods: poll() and wait().

You can think of the poll() method as asking your friend if she’s finished running the code you gave her. The poll() method will return None if the process is still running at the time poll() is called. If the program has terminated, it will return the process’s integer exit code. An exit code is used to indicate whether the process terminated without errors (an exit code of 0) or whether an error caused the process to terminate (a nonzero exit code—generally 1, but it may vary depending on the program).

The wait() method is like waiting for your friend to finish working on her code before you keep working on yours. The wait() method will block until the launched process has terminated. This is helpful if you want your program to pause until the user finishes with the other program. The return value of wait() is the process’s integer exit code.

On Windows, enter the following into the interactive shell. Note that the wait() call will block until you quit the launched calculator program.

```python
❶ >>> calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
❷ >>> calcProc.poll() == None
```
   True
```python
❸ >>> calcProc.wait()
```
   0
```python
   >>> calcProc.poll()
```
   0
Here we open a calculator process ❶. While it’s still running, we check if poll() returns None ❷. It should, as the process is still running. Then we close the calculator program and call wait() on the terminated process ❸. wait() and poll() now return 0, indicating that the process terminated without errors.