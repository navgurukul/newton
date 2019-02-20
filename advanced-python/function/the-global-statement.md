```ngMeta
name: the-global-statement
```
# The global Statement
If you need to modify a global variable from within a function, use the global statement. If you have a line such as global eggs at the top of a function, it tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.” For example, type the following code into the file editor and save it as sameName2.py:

```python
  def spam():
❶    global eggs
❷    eggs = 'spam'

  eggs = 'global'
  spam()
  print(eggs)
```
When you run this program, the final print() call will output this:


spam
Because eggs is declared global at the top of spam() ❶, when eggs is set to 'spam' ❷, this assignment is done to the globally scoped eggs. No local eggs variable is created.

There are four rules to tell whether a variable is in a local scope or global scope:

If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

If there is a global statement for that variable in a function, it is a global variable.

Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

But if the variable is not used in an assignment statement, it is a global variable.

To get a better feel for these rules, here’s an example program. Type the following code into the file editor and save it as sameName3.py:

```python
  def spam():
❶  global eggs
    eggs = 'spam' # this is the global

  def bacon():
❷  eggs = 'bacon' # this is a local
  def ham():
❸  print(eggs) # this is the global

  eggs = 42 # this is the global
  spam()
  print(eggs)
```
In the spam() function, eggs is the global eggs variable, because there’s a global statement for eggs at the beginning of the function ❶. In bacon(), eggs is a local variable, because there’s an assignment statement for it in that function ❷. In ham() ❸, eggs is the global variable, because there is no assignment statement or global statement for it in that function. If you run sameName3.py, the output will look like this:


spam
In a function, a variable will either always be global or always be local. There’s no way that the code in a function can use a local variable named eggs and then later in that same function use the global eggs variable.
# Note
If you ever want to modify the value stored in a global variable from in a function, you must use a global statement on that variable.

If you try to use a local variable in a function before you assign a value to it, as in the following program, Python will give you an error. To see this, type the following into the file editor and save it as sameName4.py:

```python
  def spam():
      print(eggs) # ERROR!
❶    eggs = 'spam local'

❷ eggs = 'global'
   spam()
```
If you run the previous program, it produces an error message.


Traceback (most recent call last):
  File "C:/test3784.py", line 6, in <module>
    spam()
  File "C:/test3784.py", line 2, in spam
    print(eggs) # ERROR!
UnboundLocalError: local variable 'eggs' referenced before assignment
This error happens because Python sees that there is an assignment statement for eggs in the spam() function ❶ and therefore considers eggs to be local. But because print(eggs) is executed before eggs is assigned anything, the local variable eggs doesn’t exist. Python will not fall back to using the global eggs variable ❷.

Functions as “Black Boxes”

Often, all you need to know about a function are its inputs (the parameters) and output value; you don’t always have to burden yourself with how the function’s code actually works. When you think about functions in this high-level way, it’s common to say that you’re treating the function as a “black box.”

This idea is fundamental to modern programming. Later chapters in this book will show you several modules with functions that were written by other people. While you can take a peek at the source code if you’re curious, you don’t need to know how these functions work in order to use them. And because writing functions without global variables is encouraged, you usually don’t have to worry about the function’s code interacting with the rest of your program.

