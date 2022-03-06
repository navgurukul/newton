```ngMeta
name: python-introduction
```
# Conventions

This cource is not designed as a reference manual; it’s a guide for beginners. The coding style sometimes goes against best practices (for example, some programs use global variables), but that’s a trade-off to make the code simpler to learn. This book is made for people to write throwaway code, so there’s not much time spent on style and elegance. Sophisticated programming concepts—like object-oriented programming, list comprehensions, and generators—aren’t covered because of the complexity they add. Veteran programmers may point out ways the code in this book could be changed to improve efficiency, but this book is mostly concerned with getting programs to work with the least amount of effort.

# What Is Programming?

Television shows and films often show programmers furiously typing cryptic streams of 1s and 0s on glowing screens, but modern programming isn’t that mysterious. Programming is simply the act of entering instructions for the computer to perform. These instructions might crunch some numbers, modify text, look up information in files, or communicate with other computers over the Internet.

All programs use basic instructions as building blocks. Here are a few of the most common ones, in English:

1. Do this; then do that.

2. If this condition is true, perform this action; otherwise, do that action.

3. Do this action that number of times.

4. Keep doing that until this condition is true.

You can combine these building blocks to implement more intricate decisions, too. For example, here are the programming instructions, called the source code, for a simple program written in the Python programming language. Starting at the top, the Python software runs each line of code (some lines are run only if a certain condition is true or else Python runs some other line) until it reaches the bottom.

```python
❶ passwordFile = open('SecretPasswordFile.txt')
❷ secretPassword = passwordFile.read()
❸ print('Enter your password.')
typedPassword = input()
❹ if typedPassword == secretPassword:
❺   	 print('Access granted')
❻	if typedPassword == '12345':
❼	print('That password is one that an idiot puts on their luggage.')
else:
❽ 	print('Access denied')
```

You might not know anything about programming, but you could probably make a reasonable guess at what the previous code does just by reading it. First, the file SecretPasswordFile.txt is opened ❶, and the secret password in it is read ❷. Then, the user is prompted to input a password (from the keyboard) ❸. These two passwords are compared ❹, and if they’re the same, the program prints Access granted to the screen ❺. Next, the program checks to see whether the password is 12345 ❻ and hints that this choice might not be the best for a password ❼. If the passwords are not the same, the program prints Access denied to the screen ❽.

