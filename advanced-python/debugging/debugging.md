```ngMeta
name: debugging
completionMethod: manual
```
# Debugging
Now that you know enough to write more complicated programs, you may start finding not-so-simple bugs in them. This chapter covers some tools and techniques for finding the root cause of bugs in your program to help you fix bugs faster and with less effort.

To paraphrase an old joke among programmers, “Writing code accounts for 90 percent of programming. Debugging code accounts for the other 90 percent.”

Your computer will do only what you tell it to do; it won’t read your mind and do what you intended it to do. Even professional programmers create bugs all the time, so don’t feel discouraged if your program has a problem.

Fortunately, there are a few tools and techniques to identify what exactly your code is doing and where it’s going wrong. First, you will look at logging and assertions, two features that can help you detect bugs early. In general, the earlier you catch bugs, the easier they will be to fix.

Second, you will look at how to use the debugger. The debugger is a feature of IDLE that executes a program one instruction at a time, giving you a chance to inspect the values in variables while your code runs, and track how the values change over the course of your program. This is much slower than running the program at full speed, but it is helpful to see the actual values in a program while it runs, rather than deducing what the values might be from the source code.

# Raising Exceptions
Python raises an exception whenever it tries to execute invalid code. In Chapter 3, you read about how to handle Python’s exceptions with try and except statements so that your program can recover from exceptions that you anticipated. But you can also raise your own exceptions in your code. Raising an exception is a way of saying, “Stop running the code in this function and move the program execution to the except statement.”

Exceptions are raised with a raise statement. In code, a raise statement consists of the following:

The raise keyword

A call to the Exception() function

A string with a helpful error message passed to the Exception() function

For example, enter the following into the interactive shell:

```python
>>> raise Exception('This is the error message.')
```
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
If there are no try and except statements covering the raise statement that raised the exception, the program simply crashes and displays the exception’s error message.

Often it’s the code that calls the function, not the function itself, that knows how to handle an exception. So you will commonly see a raise statement inside a function and the try and except statements in the code calling the function. For example, open a new file editor window, enter the following code, and save the program as boxPrint.py:


   def boxPrint(symbol, width, height):
       if len(symbol) != 1:
❶         raise Exception('Symbol must be a single character string.')
       if width <= 2:
❷         raise Exception('Width must be greater than 2.')
       if height <= 2:
❸         raise Exception('Height must be greater than 2.')
       print(symbol * width)
       for i in range(height - 2):
           print(symbol + (' ' * (width - 2)) + symbol)
       print(symbol * width)

   for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
       try:
           boxPrint(sym, w, h)
❹     except Exception as err:
❺         print('An exception happened: ' + str(err))
Here we’ve defined a boxPrint() function that takes a character, a width, and a height, and uses the character to make a little picture of a box with that width and height. This box shape is printed to the screen.

Say we want the character to be a single character, and the width and height to be greater than 2. We add if statements to raise exceptions if these requirements aren’t satisfied. Later, when we call boxPrint() with various arguments, our try/except will handle invalid arguments.

This program uses the except Exception as err form of the except statement ❹. If an Exception object is returned from boxPrint() ❶❷❸, this except statement will store it in a variable named err. The Exception object can then be converted to a string by passing it to str() to produce a user-friendly error message ❺. When you run this boxPrint.py, the output will look like this:


****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
An exception happened: Width must be greater than 2.
An exception happened: Symbol must be a single character string.
Using the try and except statements, you can handle errors more gracefully instead of letting the entire program crash.