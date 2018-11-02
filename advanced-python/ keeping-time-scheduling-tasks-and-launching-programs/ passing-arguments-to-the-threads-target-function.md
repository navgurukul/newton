```ngMeta
name:  passing-arguments-to-the-threads-target-function
completionMethod: manual
```
# Passing Arguments to the Thread’s Target Function
If the target function you want to run in the new thread takes arguments, you can pass the target function’s arguments to threading.Thread(). For example, say you wanted to run this print() call in its own thread:

```python
>>> print('Cats', 'Dogs', 'Frogs', sep=' & ')
```
Cats & Dogs & Frogs
This print() call has three regular arguments, 'Cats', 'Dogs', and 'Frogs', and one keyword argument, sep=' & '. The regular arguments can be passed as a list to the args keyword argument in threading.Thread(). The keyword argument can be specified as a dictionary to the kwargs keyword argument in threading.Thread().

Enter the following into the interactive shell:

```python
>>> import threading
>>> threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
kwargs={'sep': ' & '})
>>> threadObj.start()
```
Cats & Dogs & Frogs
To make sure the arguments 'Cats', 'Dogs', and 'Frogs' get passed to print() in the new thread, we pass args=['Cats', 'Dogs', 'Frogs'] to threading.Thread(). To make sure the keyword argument sep=' & ' gets passed to print() in the new thread, we pass kwargs={'sep': '& '} to threading.Thread().

The threadObj.start() call will create a new thread to call the print() function, and it will pass 'Cats', 'Dogs', and 'Frogs' as arguments and ' & ' for the sep keyword argument.

This is an incorrect way to create the new thread that calls print():


threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
What this ends up doing is calling the print() function and passing its return value (print()’s return value is always None) as the target keyword argument. It doesn’t pass the print() function itself. When passing arguments to a function in a new thread, use the threading.Thread() function’s args and kwargs keyword arguments.
# Concurrency Issues
You can easily create several new threads and have them all running at the same time. But multiple threads can also cause problems called concurrency issues. These issues happen when threads read and write variables at the same time, causing the threads to trip over each other. Concurrency issues can be hard to reproduce consistently, making them hard to debug.

Multithreaded programming is its own wide subject and beyond the scope of this book. What you have to keep in mind is this: To avoid concurrency issues, never let multiple threads read or write the same variables. When you create a new Thread object, make sure its target function uses only local variables in that function. This will avoid hard-to-debug concurrency issues in your programs.

# Note
A beginner’s tutorial on multithreaded programming is available at <span><a href=" http://nostarch.com/automatestuff/."> http://nostarch.com/automatestuff/.</a></span>