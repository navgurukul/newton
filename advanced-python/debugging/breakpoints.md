```ngMeta
name: breakpoints
completionMethod: manual
```
# Breakpoints
A breakpoint can be set on a specific line of code and forces the debugger to pause whenever the program execution reaches that line. Open a new file editor window and enter the following program, which simulates flipping a coin 1,000 times. Save it as coinFlip.py.


   import random
   heads = 0
   for i in range(1, 1001):
❶     if random.randint(0, 1) == 1:
           heads = heads + 1
       if i == 500:
❷         print('Halfway done!')
   print('Heads came up ' + str(heads) + ' times.')
The random.randint(0, 1) call ❶ will return 0 half of the time and 1 the other half of the time. This can be used to simulate a 50/50 coin flip where 1 represents heads. When you run this program without the debugger, it quickly outputs something like the following:


Halfway done!
Heads came up 490 times.
If you ran this program under the debugger, you would have to click the Over button thousands of times before the program terminated. If you were interested in the value of heads at the halfway point of the program’s execution, when 500 of 1000 coin flips have been completed, you could instead just set a breakpoint on the line print('Halfway done!') ❷. To set a breakpoint, right-click the line in the file editor and select Set Breakpoint, as shown in Figure 10-5.

<!-- ![Anoop](assets/000001.jpg)
 -->
 Setting a breakpoint

You don’t want to set a breakpoint on the if statement line, since the if statement is executed on every single iteration through the loop. By setting the breakpoint on the code in the if statement, the debugger breaks only when the execution enters the if clause.

The line with the breakpoint will be highlighted in yellow in the file editor. When you run the program under the debugger, it will start in a paused state at the first line, as usual. But if you click Go, the program will run at full speed until it reaches the line with the breakpoint set on it. You can then click Go, Over, Step, or Out to continue as normal.

If you want to remove a breakpoint, right-click the line in the file editor and select Clear Breakpoint from the menu. The yellow highlighting will go away, and the debugger will not break on that line in the future.

# Summary
Assertions, exceptions, logging, and the debugger are all valuable tools to find and prevent bugs in your program. Assertions with the Python assert statement are a good way to implement “sanity checks” that give you an early warning when a necessary condition doesn’t hold true. Assertions are only for errors that the program shouldn’t try to recover from and should fail fast. Otherwise, you should raise an exception.

An exception can be caught and handled by the try and except statements. The logging module is a good way to look into your code while it’s running and is much more convenient to use than the print() function because of its different logging levels and ability to log to a text file.

The debugger lets you step through your program one line at a time. Alternatively, you can run your program at normal speed and have the debugger pause execution whenever it reaches a line with a breakpoint set. Using the debugger, you can see the state of any variable’s value at any point during the program’s lifetime.

These debugging tools and techniques will help you write programs that work. Accidentally introducing bugs into your code is a fact of life, no matter how many years of coding experience you have.

