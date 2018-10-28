```ngMeta
name: flow-control
completionMethod: manual
```
# Elements of Flow Control
Conditions
The Boolean expressions you’ve seen so far could all be considered conditions, which are the same thing as expressions; condition is just a more specific name in the context of flow control statements. Conditions always evaluate down to a Boolean value, True or False. A flow control statement decides what to do based on whether its condition is True or False, and almost every flow control statement uses a condition.

# Blocks of Code
Lines of Python code can be grouped together in blocks. You can tell when a block begins and ends from the indentation of the lines of code. There are three rules for blocks.

1. Blocks begin when the indentation increases.

2. Blocks can contain other blocks.

3. Blocks end when the indentation decreases to zero or to a containing block’s indentation.

Blocks are easier to understand by looking at some indented code, so let’s find the blocks in part of a small game program, shown here:
```python
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
```
The first block of code ❶ starts at the line print('Hello Mary') and contains all the lines after it. Inside this block is another block ❷, which has only a single line in it: print('Access Granted.'). The third block ❸ is also one line long: print('Wrong password.').

# Program Execution
In the previous chapter’s hello.py program, Python started executing instructions at the top of the program going down, one after another. The program execution (or simply, execution) is a term for the current instruction being executed. If you print the source code on paper and put your finger on each line as it is executed, you can think of your finger as the program execution.

Not all programs execute by simply going straight down, however. If you use your finger to trace through a program with flow control statements, you’ll likely find yourself jumping around the source code based on conditions, and you’ll probably skip entire clauses.

