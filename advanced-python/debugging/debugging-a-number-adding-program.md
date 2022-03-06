```ngMeta
name: debugging-a-number-adding-program
```
# Debugging a Number Adding Program
Open a new file editor window and enter the following code:


print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)
Save it as buggyAddingProgram.py and run it first without the debugger enabled. The program will output something like this:


Enter the first number to add:
5
Enter the second number to add:
3
Enter the third number to add:
42
The sum is 5342
The program hasn’t crashed, but the sum is obviously wrong. Let’s enable the Debug Control window and run it again, this time under the debugger.

When you press F5 or select Run▸Run Module (with Debug▸Debugger enabled and all four checkboxes on the Debug Control window checked), the program starts in a paused state on line 1. The debugger will always pause on the line of code it is about to execute. The Debug Control window will look like Figure 10-2.

<!-- ![Anoop](assets/000063.jpg)
 -->
 The Debug Control window when the program first starts under the debugger

Click the Over button once to execute the first print() call. You should use Over instead of Step here, since you don’t want to step into the code for the print() function. The Debug Control window will update to line 2, and line 2 in the file editor window will be highlighted, as shown in Figure 10-3. This shows you where the program execution currently is.

<!-- ![Anoop](assets/000068.jpg)
 -->
The Debug Control window after clicking Over

Click Over again to execute the input() function call, and the buttons in the Debug Control window will disable themselves while IDLE waits for you to type something for the input() call into the interactive shell window. Enter 5 and press Return. The Debug Control window buttons will be reenabled.

Keep clicking Over, entering 3 and 42 as the next two numbers, until the debugger is on line 7, the final print() call in the program. The Debug Control window should look like Figure 10-4. You can see in the Globals section that the first, second, and third variables are set to string values '5', '3', and '42' instead of integer values 5, 3, and 42. When the last line is executed, these strings are concatenated instead of added together, causing the bug.

<!-- ![Anoop](assets/000000.jpg)
 -->
Figure 10-4. The Debug Control window on the last line. The variables are set to strings, causing the bug.

Stepping through the program with the debugger is helpful but can also be slow. Often you’ll want the program to run normally until it reaches a certain line of code. You can configure the debugger to do this with breakpoints.


