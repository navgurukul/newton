```ngMeta
name: getting-the-traceback-as-a-string
```
# Getting the Traceback as a String
When Python encounters an error, it produces a treasure trove of error information called the traceback. The traceback includes the error message, the line number of the line that caused the error, and the sequence of the function calls that led to the error. This sequence of calls is called the call stack.

Open a new file editor window in IDLE, enter the following program, and save it as errorExample.py:


def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()
When you run errorExample.py, the output will look like this:


Traceback (most recent call last):
  File "errorExample.py", line 7, in <module>
    spam()
  File "errorExample.py", line 2, in spam
    bacon()
  File "errorExample.py", line 5, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.
From the traceback, you can see that the error happened on line 5, in the bacon() function. This particular call to bacon() came from line 2, in the spam() function, which in turn was called on line 7. In programs where functions can be called from multiple places, the call stack can help you determine which call led to the error.

The traceback is displayed by Python whenever a raised exception goes unhandled. But you can also obtain it as a string by calling traceback.format_exc(). This function is useful if you want the information from an exception’s traceback but also want an except statement to gracefully handle the exception. You will need to import Python’s traceback module before calling this function.

For example, instead of crashing your program right when an exception occurs, you can write the traceback information to a log file and keep your program running. You can look at the log file later, when you’re ready to debug your program. Enter the following into the interactive shell:

```python
>>> import traceback
>>> try:
         raise Exception('This is the error message.')
except:
         errorFile = open('errorInfo.txt', 'w')
         errorFile.write(traceback.format_exc())
         errorFile.close()
         print('The traceback info was written to errorInfo.txt.')
```

116
The traceback info was written to errorInfo.txt.
The 116 is the return value from the write() method, since 116 characters were written to the file. The traceback text was written to errorInfo.txt.


Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
Exception: This is the error message.
