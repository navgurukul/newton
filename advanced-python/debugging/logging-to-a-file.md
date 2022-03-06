```ngMeta
name: logging-to-a-file
```
# Logging to a File
Instead of displaying the log messages to the screen, you can write them to a text file. The logging.basicConfig() function takes a filename keyword argument, like so:


import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s - %(levelname)s - %(message)s')
The log messages will be saved to myProgramLog.txt. While logging messages are helpful, they can clutter your screen and make it hard to read the program’s output. Writing the logging messages to a file will keep your screen clear and store the messages so you can read them after running the program. You can open this text file in any text editor, such as Notepad or TextEdit.

## IDLE’s Debugger
The debugger is a feature of IDLE that allows you to execute your program one line at a time. The debugger will run a single line of code and then wait for you to tell it to continue. By running your program “under the debugger” like this, you can take as much time as you want to examine the values in the variables at any given point during the program’s lifetime. This is a valuable tool for tracking down bugs.

To enable IDLE’s debugger, click Debug▸Debugger in the interactive shell window. This will bring up the Debug Control window, which looks like Figure 10-1.

When the Debug Control window appears, select all four of the Stack, Locals, Source, and Globals checkboxes so that the window shows the full set of debug information. While the Debug Control window is displayed, any time you run a program from the file editor, the debugger will pause execution before the first instruction and display the following:

The line of code that is about to be executed

A list of all local variables and their values

A list of all global variables and their values

<!-- ![Anoop](assets/000020.jpg)
 -->
The Debug Control window

You’ll notice that in the list of global variables there are several variables you haven’t defined, such as __builtins__, __doc__, __file__, and so on. These are variables that Python automatically sets whenever it runs a program. The meaning of these variables is beyond the scope of this book, and you can comfortably ignore them.

The program will stay paused until you press one of the five buttons in the Debug Control window: Go, Step, Over, Out, or Quit.

# Go
Clicking the Go button will cause the program to execute normally until it terminates or reaches a breakpoint. (Breakpoints are described later in this chapter.) If you are done debugging and want the program to continue normally, click the Go button.

# Step
Clicking the Step button will cause the debugger to execute the next line of code and then pause again. The Debug Control window’s list of global and local variables will be updated if their values change. If the next line of code is a function call, the debugger will “step into” that function and jump to the first line of code of that function.

# Over
Clicking the Over button will execute the next line of code, similar to the Step button. However, if the next line of code is a function call, the Over button will “step over” the code in the function. The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns. For example, if the next line of code is a print() call, you don’t really care about code inside the built-in print() function; you just want the string you pass it printed to the screen. For this reason, using the Over button is more common than the Step button.

# Out
Clicking the Out button will cause the debugger to execute lines of code at full speed until it returns from the current function. If you have stepped into a function call with the Step button and now simply want to keep executing instructions until you get back out, click the Out button to “step out” of the current function call.

# Quit
If you want to stop debugging entirely and not bother to continue executing the rest of the program, click the Quit button. The Quit button will immediately terminate the program. If you want to run your program normally again, select Debug▸Debugger again to disable the debugger.


