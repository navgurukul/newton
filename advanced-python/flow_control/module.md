```ngMeta
name: module
```
# Importing Modules

All Python programs can call a basic set of functions called built-in functions, including the print(), input(), and len() functions you’ve seen before. Python also comes with a set of modules called the standard library. Each module is a Python program that contains a related group of functions that can be embedded in your programs. For example, the math module has mathematics-related functions, the random module has random number–related functions, and so on.

Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:

1. The import keyword

2. The name of the module

3. Optionally, more module names, as long as they are separated by commas

Once you import a module, you can use all the cool functions of that module. Let’s give it a try with the random module, which will give us access to the random.randint() function.

Enter this code into the file editor, and save it as printRandom.py:
```python
import random
for i in range(5):
    print(random.randint(1, 10))
```
When you run this program, the output will look something like this:


4
1
8
4
1
The random.randint() function call evaluates to a random integer value between the two integers that you pass it. Since randint() is in the random module, you must first type random. in front of the function name to tell Python to look for this function inside the random module.

Here’s an example of an import statement that imports four different modules:


import random, sys, os, math
Now we can use any of the functions in these four modules. We’ll learn more about them later in the book.

# from import Statements

	An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star; for example, from random import *.
	With this form of import statement, calls to functions in random will not need the random. prefix. However, using the full name makes for more readable code, so it is better to use the normal form of the import statement.


# Ending a Program Early with sys.exit()

The last flow control concept to cover is how to terminate the program. This always happens if the program execution reaches the bottom of the instructions. However, you can cause the program to terminate, or exit, by calling the sys.exit() function. Since this function is in the sys module, you have to import sys before your program can use it.

Open a new file editor window and enter the following code, saving it as exitExample.py:

```python
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```

Run this program in IDLE. This program has an infinite loop with no break statement inside. The only way this program will end is if the user enters exit, causing sys.exit() to be called. When response is equal to exit, the program ends. Since the response variable is set by the input() function, the user must enter exit in order to stop the program.
