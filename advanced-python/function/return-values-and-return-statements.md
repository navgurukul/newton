```ngMeta
name: return-values-and-return-statements
completionMethod: manual
```
# Return Values and return Statements
When you call the len() function and pass it an argument such as 'Hello', the function call evaluates to the integer value 5, which is the length of the string you passed it. In general, the value that a function call evaluates to is called the return value of the function.

When creating a function using the def statement, you can specify what the return value should be with a return statement. A return statement consists of the following:

The return keyword

The value or expression that the function should return

When an expression is used with a return statement, the return value is what this expression evaluates to. For example, the following program defines a function that returns a different string depending on what number it is passed as an argument. Type this code into the file editor and save it as magic8Ball.py:

```python
❶ import random
❷ def getAnswer(answerNumber):
❸     if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'
```
❹ r = random.randint(1, 9)
❺ fortune = getAnswer(r)
❻ print(fortune)
When this program starts, Python first imports the random module ❶. Then the getAnswer() function is defined ❷. Because the function is being defined (and not called), the execution skips over the code in it. Next, the random.randint() function is called with two arguments, 1 and 9 ❹. It evaluates to a random integer between 1 and 9 (including 1 and 9 themselves), and this value is stored in a variable named r.

The getAnswer() function is called with r as the argument ❺. The program execution moves to the top of the getAnswer() function ❸, and the value r is stored in a parameter named answerNumber. Then, depending on this value in answerNumber, the function returns one of many possible string values. The program execution returns to the line at the bottom of the program that originally called getAnswer() ❺. The returned string is assigned to a variable named fortune, which then gets passed to a print() call ❻ and is printed to the screen.

Note that since you can pass return values as an argument to another function call, you could shorten these three lines:


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
to this single equivalent line:


print(getAnswer(random.randint(1, 9)))
Remember, expressions are composed of values and operators. A function call can be used in an expression because it evaluates to its return value.

# The None Value
In Python there is a value called None, which represents the absence of a value. None is the only value of the NoneType data type. (Other programming languages might call this value null, nil, or undefined.) Just like the Boolean True and False values, None must be typed with a capital N.

This value-without-a-value can be helpful when you need to store something that won’t be confused for a real value in a variable. One place where None is used is as the return value of print(). The print() function displays text on the screen, but it doesn’t need to return anything in the same way len() or input() does. But since all function calls need to evaluate to a return value, print() returns None. To see this in action, enter the following into the interactive shell:

```python
>>> spam = print('Hello!')
```
Hello!
```python
>>> None == spam
```
True
Behind the scenes, Python adds return None to the end of any function definition with no return statement. This is similar to how a while or for loop implicitly ends with a continue statement. Also, if you use a return statement without a value (that is, just the return keyword by itself), then None is returned.