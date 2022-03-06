```ngMeta
name: flow_state
```
# Flow Control Statements

Now, let’s explore the most important piece of flow control: the statements themselves. The statements represent the diamonds you saw in the flowchart in Figure 2-1, and they are the actual decisions your programs will make.

# if Statements
The most common type of flow control statement is the if statement. An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. The clause is skipped if the condition is False.

In plain English, an if statement could be read as, “If this condition is true, execute the code in the clause.” In Python, an if statement consists of the following:

1. The if keyword

2. A condition (that is, an expression that evaluates to True or False)

3. A colon

4. Starting on the next line, an indented block of code (called the if clause)

For example, let’s say you have some code that checks to see whether someone’s name is Alice. (Pretend name was assigned some value earlier.)

```python
if name == 'Alice':
    print('Hi, Alice.')
```
All flow control statements end with a colon and are followed by a new block of code (the clause). This if statement’s clause is the block with print('Hi, Alice.'). Figure 2-3 shows what a flowchart of this code would look like.

Figure 2-3. The flowchart for an if statement

# else Statements
An if clause can optionally be followed by an else statement. The else clause is executed only when the if statement’s condition is False. In plain English, an else statement could be read as, “If this condition is true, execute this code. Or else, execute that code.” An else statement doesn’t have a condition, and in code, an else statement always consists of the following:

1. The else keyword

2. A colon

3. Starting on the next line, an indented block of code (called the else clause)

Returning to the Alice example, let’s look at some code that uses an else statement to offer a different greeting if the person’s name isn’t Alice.
```python
name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')
```
Figure 2-4 shows what a flowchart of this code would look like.

Figure 2-4. The flowchart for an else statement

# elif Statements
While only one of the if or else clauses will execute, you may have a case where you want one of many possible clauses to execute. The elif statement is an “else if” statement that always follows an if or another elif statement. It provides another condition that is checked only if all of the previous conditions were False. In code, an elif statement always consists of the following:

The elif keyword

1. A condition (that is, an expression that evaluates to True or False)

2. A colon

3. Starting on the next line, an indented block of code (called the elif clause)

Let’s add an elif to the name checker to see this statement in action.
```python
name = 'Bob'
age = 5
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
```
This time, you check the person’s age, and the program will tell them something different if they’re younger than 12. You can see the flowchart for this in Figure 2-5.

Figure 2-5. The flowchart for an elif statement

The elif clause executes if age < 12 is True and name == 'Alice' is False. However, if both of the conditions are False, then both of the clauses are skipped. It is not guaranteed that at least one of the clauses will be executed. When there is a chain of elif statements, only one or none of the clauses will be executed. Once one of the statements’ conditions is found to be True, the rest of the elif clauses are automatically skipped. For example, open a new file editor window and enter the following code, saving it as 

```python
name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
```
Here I’ve added two more elif statements to make the name checker greet a person with different answers based on age. Figure 2-6 shows the flowchart for this.

