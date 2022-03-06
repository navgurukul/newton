```ngMeta
name: task-scheduler-launchd-and-cron
```
# Task Scheduler, launchd, and cron
If you are computer savvy, you may know about Task Scheduler on Windows, launchd on OS X, or the cron scheduler on Linux. These well-documented and reliable tools all allow you to schedule applications to launch at specific times. If you’d like to learn more about them, you can find links to tutorials at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>.

Using your operating system’s built-in scheduler saves you from writing your own clock-checking code to schedule your programs. However, use the time.sleep() function if you just need your program to pause briefly. Or instead of using the operating system’s scheduler, your code can loop until a certain date and time, calling time.sleep(1) each time through the loop.

# Opening Websites with Python
The webbrowser.open() function can launch a web browser from your program to a specific website, rather than opening the browser application with subprocess.Popen(). See Project: mapit.py with the webbrowser Module for more details.

# Running Other Python Scripts
You can launch a Python script from Python just like any other application. You just have to pass the python.exe executable to Popen() and the filename of the .py script you want to run as its argument. For example, the following would run the hello.py script from Chapter 1:

```python
>>> subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])
```
<subprocess.Popen object at 0x000000000331CF28>
Pass Popen() a list containing a string of the Python executable’s path and a string of the script’s filename. If the script you’re launching needs command line arguments, add them to the list after the script’s filename. The location of the Python executable on Windows is C:\python34\python.exe. On OS X, it is /Library/Frameworks/Python.framework/Versions/3.3/bin/python3. On Linux, it is /usr/bin/python3.

Unlike importing the Python program as a module, when your Python program launches another Python program, the two are run in separate processes and will not be able to share each other’s variables.