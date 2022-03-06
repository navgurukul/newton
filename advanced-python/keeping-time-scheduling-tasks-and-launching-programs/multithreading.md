```ngMeta
name: multithreading
```
# Multithreading
To introduce the concept of multithreading, let’s look at an example situation. Say you want to schedule some code to run after a delay or at a specific time. You could add code like the following at the start of your program:

```python
import time, datetime

startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Halloween 2029')
```

--snip--
This code designates a start time of October 31, 2029, and keeps calling time.sleep(1) until the start time arrives. Your program cannot do anything while waiting for the loop of time.sleep() calls to finish; it just sits around until Halloween 2029. This is because Python programs by default have a single thread of execution.

To understand what a thread of execution is, remember the Chapter 2 discussion of flow control, when you imagined the execution of a program as placing your finger on a line of code in your program and moving to the next line or wherever it was sent by a flow control statement. A single-threaded program has only one finger. But a multithreaded program has multiple fingers. Each finger still moves to the next line of code as defined by the flow control statements, but the fingers can be at different places in the program, executing different lines of code at the same time. (All of the programs in this book so far have been single threaded.)

Rather than having all of your code wait until the time.sleep() function finishes, you can execute the delayed or scheduled code in a separate thread using Python’s threading module. The separate thread will pause for the time.sleep calls. Meanwhile, your program can do other work in the original thread.

To make a separate thread, you first need to make a Thread object by calling the threading.Thread() function. Enter the following code in a new file and save it as threadDemo.py:

```python
   import threading, time
   print('Start of program.')

❶ def takeANap():
       time.sleep(5)
       print('Wake up!')

❷ threadObj = threading.Thread(target=takeANap)
❸ threadObj.start()

   print('End of program.')
```

At ❶, we define a function that we want to use in a new thread. To create a Thread object, we call threading.Thread() and pass it the keyword argument target=takeANap ❷. This means the function we want to call in the new thread is takeANap(). Notice that the keyword argument is target=takeANap, not target=takeANap(). This is because you want to pass the takeANap() function itself as the argument, not call takeANap() and pass its return value.

After we store the Thread object created by threading.Thread() in threadObj, we call threadObj.start() ❸ to create the new thread and start executing the target function in the new thread. When this program is run, the output will look like this:


Start of program.
End of program.
Wake up!
This can be a bit confusing. If print('End of program.') is the last line of the program, you might think that it should be the last thing printed. The reason Wake up! comes after it is that when threadObj.start() is called, the target function for threadObj is run in a new thread of execution. Think of it as a second finger appearing at the start of the takeANap() function. The main thread continues to print('End of program.'). Meanwhile, the new thread that has been executing the time.sleep(5) call, pauses for 5 seconds. After it wakes from its 5-second nap, it prints 'Wake up!' and then returns from the takeANap() function. Chronologically, 'Wake up!' is the last thing printed by the program.

Normally a program terminates when the last line of code in the file has run (or the sys.exit() function is called). But threadDemo.py has two threads. The first is the original thread that began at the start of the program and ends after print('End of program.'). The second thread is created when threadObj.start() is called, begins at the start of the takeANap() function, and ends after takeANap() returns.

A Python program will not terminate until all its threads have terminated. When you ran threadDemo.py, even though the original thread had terminated, the second thread was still executing the time.sleep(5) call.

