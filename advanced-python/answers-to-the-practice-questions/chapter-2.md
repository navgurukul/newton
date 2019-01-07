```ngMeta
name: chapter-2
```
# Chapter 2
True and False, using capital T and F, with the rest of the word in lowercase

and, or, and not

True and True is True.

True and False is False.

False and True is False.

False and False is False.

True or True is True.

True or False is True.

False or True is True.

False or False is False.

not True is False.

not False is True.

False
False
True
False
False
True
==, !=, <, >, <=, and >=.

== is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable.

A condition is an expression used in a flow control statement that evaluates to a Boolean value.

The three blocks are everything inside the if statement and the lines print('bacon') and print('ham').


print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
The code:


if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
Press CTRL-C to stop a program stuck in an infinite loop.

The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.

They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) explicitly tells the loop to start at 0, and range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.

The code:


for i in range(1, 11):
    print(i)
and:


i = 1
while i <= 10:
    print(i)
    i = i + 1
This function can be called with spam.bacon().