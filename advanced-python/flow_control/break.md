```ngMeta
name: break
```
# break Statements
There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains the break keyword.

Pretty simple, right? Here’s a program that does the same thing as the previous program, but it uses a break statement to escape the loop. Enter the following code, and save the file as yourName2.py:

```python
while True:                         # (1)
    print('Please type your name.')
    name = input()                  # (2)
    if name == 'your name':         # (3)
        break                       # (4)
print('Thank you!')                 # (5)
```
The first line ❶ creates an infinite loop; it is a while loop whose condition is always True. (The expression True, after all, always evaluates down to the value True.) The program execution will always enter the loop and will exit it only when a break statement is executed. (An infinite loop that never exits is a common programming bug.)

Just like before, this program asks the user to type your name ❷. Now, however, while the execution is still inside the while loop, an if statement gets executed ❸ to check whether name is equal to your name. If this condition is True, the break statement is run ❹, and the execution moves out of the loop to print('Thank you!') ❺. Otherwise, the if statement’s clause with the break statement is skipped, which puts the execution at the end of the while loop. At this point, the program execution jumps back to the start of the while statement ❶ to recheck the condition. Since this condition is merely the True Boolean value, the execution enters the loop to ask the user to type your name again. See Figure 2-12 for the flowchart of this program.

Run yourName2.py, and enter the same text you entered for yourName.py. The rewritten program should respond in the same way as the original.


Figure 2-12. The flowchart for the yourName2.py program with an infinite loop. Note that the X path will logically never happen because the loop condition is always True.