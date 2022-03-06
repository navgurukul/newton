```ngMeta
name: what-is-python
```
# What Is Python??

Python refers to the Python programming language (with syntax rules for writing what is considered valid Python code) and the Python interpreter software that reads source code (written in the Python language) and performs its instructions. The Python interpreter is free to download from http://python.org/, and there are versions for Linux, OS X, and Windows.

The name Python comes from the surreal British comedy group Monty Python, not from the snake. Python programmers are affectionately called Pythonistas, and both Monty Python and serpentine references usually pepper Python tutorials and documentation.

# Programmers Don’t Need to Know Much Math

The most common anxiety I hear about learning to program is that people think it requires a lot of math. Actually, most programming doesn’t require math beyond basic arithmetic. In fact, being good at programming isn’t that different from being good at solving Sudoku puzzles.

To solve a Sudoku puzzle, the numbers 1 through 9 must be filled in for each row, each column, and each 3×3 interior square of the full 9×9 board. You find a solution by applying deduction and logic from the starting numbers. For example, since 5 appears in the top left of the Sudoku puzzle shown in Figure 1, it cannot appear elsewhere in the top row, in the leftmost column, or in the top-left 3×3 square. Solving one row, column, or square at a time will provide more number clues for the rest of the puzzle.


Just because Sudoku involves numbers doesn’t mean you have to be good at math to figure out the solution. The same is true of programming. Like solving a Sudoku puzzle, writing programs involves breaking down a problem into individual, detailed steps. Similarly, when debugging programs (that is, finding and fixing errors), you’ll patiently observe what the program is doing and find the cause of the bugs. And like all skills, the more you program, the better you’ll become.


# Programming Is a Creative Activity

Programming is a creative task, somewhat like constructing a castle out of LEGO bricks. You start with a basic idea of what you want your castle to look like and inventory your available blocks. Then you start building. Once you’ve finished building your program, you can pretty up your code just like you would your castle.

The difference between programming and other creative activities is that when programming, you have all the raw materials you need in your computer; you don’t need to buy any additional canvas, paint, film, yarn, LEGO bricks, or electronic components. When your program is written, it can easily be shared online with the entire world. And though you’ll make mistakes when programming, the activity is still a lot of fun.

# Asking Smart Programming Questions

If you can’t find the answer by searching online, try asking people in a web forum such as Stack Overlow (http://stackoverflow.com/) or the “learn programming” subreddit at http://reddit.com/r/learnprogramming/. But keep in mind there are smart ways to ask programming questions that help others help you. Be sure to read the Frequently Asked Questions sections these websites have about the proper way to post questions.

## When asking programming questions, remember to do the following:

1. Explain what you are trying to do, not just what you did. This lets your helper know if you are on the wrong track.

2. Specify the point at which the error happens. Does it occur at the very start of the program or only after you do a certain action?

3. Copy and paste the entire error message and your code to <span><a href="http://pastebin.com/">http://pastebin.com/</a></span> or <span><a href="http://gist.github.com/.">http://gist.github.com/.</a></span>

4. These websites make it easy to share large amounts of code with people over the Web, without the risk of losing any text formatting. You can then put the URL of the posted code in your email or forum post. For example, here some pieces of code I’ve posted:<span><a href=" http://pastebin.com/SzP2DbFx/"> http://pastebin.com/SzP2DbFx/</a></span> and <span><a href="https://gist.github.com/asweigart/6912168/.">https://gist.github.com/asweigart/6912168/.</a></span>

5. Explain what you’ve already tried to do to solve your problem. This tells people you’ve already put in some work to figure things out on your own.

6. List the version of Python you’re using. (There are some key differences between version 2 Python interpreters and version 3 Python interpreters.) Also, say which operating system and version you’re running.

7. If the error came up after you made a change to your code, explain exactly what you changed.

8. Say whether you’re able to reproduce the error every time you run the program or whether it happens only after you perform certain actions. Explain what those actions are, if so.

Always follow good online etiquette as well. For example, don’t post your questions in all caps or make unreasonable demands of the people trying to help you.

# How to Find Help

Solving programming problems on your own is easier than you might think. If you’re not convinced, then let’s cause an error on purpose: Enter '42' + 3 into the interactive shell. You don’t need to know what this instruction means right now, but the result should look like this:

```python
  >>> '42' + 3
❶ Traceback (most recent call last):
    File "<pyshell#0>", line 1, in <module>
      '42' + 3
❷ """TypeError: Can't convert 'int' object to str "implicitly"""
  >>>
  ```
The error message ❷ appeared here because Python couldn’t understand your instruction. The traceback part ❶ of the error message shows the specific instruction and line number that Python had trouble with. If you’re not sure what to make of a particular error message, search online for the exact error message. Enter “TypeError: Can’t convert ‘int’ object to str implicitly” (including the quotes) into your favorite search engine, and you should see tons of links explaining what the error message means and what causes it, as shown in Figure 2.


Figure 2. The Google results for an error message can be very helpful.

You’ll often find that someone else had the same question as you and that some other helpful person has already answered it. No one person can know everything about programming, so an everyday part of any software developer’s job is looking up answers to technical questions.





