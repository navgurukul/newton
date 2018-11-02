```ngMeta
name: function-introduction
completionMethod: manual
```
You’re already familiar with the print(), input(), and len() functions from the previous chapters. Python provides several builtin functions like these, but you can also write your own functions. A function is like a mini-program within a program.

To better understand how functions work, let’s create one. Type this program into the file editor and save it as helloFunc.py:

```python
❶ def hello():
❷     print('Howdy!')
       print('Howdy!!!')
       print('Hello there.')
❸ hello()
   hello()
   hello()
```
The first line is a def statement ❶, which defines a function named hello(). The code in the block that follows the def statement ❷ is the body of the function. This code is executed when the function is called, not when the function is first defined.

The hello() lines after the function ❸ are function calls. In code, a function call is just the function’s name followed by parentheses, possibly with some number of arguments in between the parentheses. When the program execution reaches these calls, it will jump to the top line in the function and begin executing the code there. When it reaches the end of the function, the execution returns to the line that called the function and continues moving through the code as before.

Since this program calls hello() three times, the code in the hello() function is executed three times. When you run this program, the output looks like this:


Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!

Hello there.
A major purpose of functions is to group code that gets executed multiple times. Without a function defined, you would have to copy and paste this code each time, and the program would look like this:

```python
print('Howdy!')
print('Howdy!!!')
print('Hello there.')
print('Howdy!')
print('Howdy!!!')
print('Hello there.')
print('Howdy!')
print('Howdy!!!')
print('Hello there.')
```
In general, you always want to avoid duplicating code, because if you ever decide to update the code—if, for example, you find a bug you need to fix—you’ll have to remember to change the code everywhere you copied it.

As you get more programming experience, you’ll often find yourself deduplicating code, which means getting rid of duplicated or copy-and-pasted code. Deduplication makes your programs shorter, easier to read, and easier to update.






