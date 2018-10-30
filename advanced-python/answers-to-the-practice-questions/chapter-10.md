```ngMeta
name: chapter-10
completionMethod: manual
```
# Chapter 10
assert spam >= 10, 'The spam variable is less than 10.'

assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!' or assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'

assert False, 'This assertion always triggers.'

To be able to call logging.debug(), you must have these two lines at the start of your program:


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s -  %(message)s')
To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of your program:


import logging
>>> logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')
DEBUG, INFO, WARNING, ERROR, and CRITICAL

logging.disable(logging.CRITICAL)

You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.

The Step button will move the debugger into a function call. The Over button will quickly execute the function call without stepping into it. The Out button will quickly execute the rest of the code until it steps out of the function it currently is in.

After you click Go, the debugger will stop when it has reached the end of the program or a line with a breakpoint.

A breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.

To set a breakpoint in IDLE, right-click the line and select Set Breakpoint from the context menu.