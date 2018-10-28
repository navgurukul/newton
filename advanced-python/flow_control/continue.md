```ngMeta
name: continue
completionMethod: manual
```
# continue Statements
Like break statements, continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. (This is also what happens when the execution reaches the end of the loop.)

Trapped in an Infinite Loop?

If you ever run a program that has a bug causing it to get stuck in an infinite loop, press CTRL-C. This will send a KeyboardInterrupt error to your program and cause it to stop immediately. To try it, create a simple infinite loop in the file editor, and save it as infiniteloop.py.


while True:
    print('Hello world!')
When you run this program, it will print Hello world! to the screen forever, because the while statement’s condition is always True. In IDLE’s interactive shell window, there are only two ways to stop this program: press CTRL-C or select Shell ▸ restart Shell from the menu. CTRL-C is handy if you ever want to terminate your program immediately, even if it’s not stuck in an infinite loop.

Let’s use continue to write a program that asks for a name and password. Enter the following code into a new file editor window and save the program as swordfish.py.
If the user enters any name besides Joe ❶, the continue statement ❷ causes the program execution to jump back to the start of the loop. When it reevaluates the condition, the execution will always enter the loop, since the condition is simply the value True. Once they make it past that if statement, the user is asked for a password ❸. If the password entered is swordfish, then the break statement ❹ is run, and the execution jumps out of the while loop to print Access granted ❺. Otherwise, the execution continues to the end of the while loop, where it then jumps back to the start of the loop. See Figure 2-13 for this program’s flowchart.


Figure 2-13. A flowchart for swordfish.py. The X path will logically never happen because the loop condition is always True.

“Truthy” and “Falsey” Values

There are some values in other data types that conditions will consider equivalent to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True. For example, look at the following program:
If the user enters a blank string for name, then the while statement’s condition will be True ❶, and the program continues to ask for a name. If the value for numOfGuests is not 0 ❷, then the condition is considered to be True, and the program will print a reminder for the user ❸.

You could have typed not name != '' instead of not name, and numOfGuests != 0 instead of numOfGuests, but using the truthy and falsey values can make your code easier to read.

Run this program and give it some input. Until you claim to be Joe, it shouldn’t ask for a password, and once you enter the correct password, it should exit.


Who are you?
I'm fine, thanks. Who are you?
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
Mary
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
swordfish
Access granted.