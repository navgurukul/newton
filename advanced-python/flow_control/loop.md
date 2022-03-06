```ngMeta
name: loop
```
# for Loops and the range() Function
The while loop keeps looping while its condition is True (which is the reason for its name), but what if you want to execute a block of code only a certain number of times? You can do this with a for loop statement and the range() function.

In code, a for statement looks something like for i in range(5): and always includes the following:

The for keyword

A variable name

The in keyword

A call to the range() method with up to three integers passed to it

A colon

Starting on the next line, an indented block of code (called the for clause)

Let’s create a new program called fiveTimes.py to help you see a for loop in action.
The code in the for loop’s clause is run five times. The first time it is run, the variable i is set to 0. The print() call in the clause will print Jimmy Five Times (0). After Python finishes an iteration through all the code inside the for loop’s clause, the execution goes back to the top of the loop, and the for statement increments i by one. This is why range(5) results in five iterations through the clause, with i being set to 0, then 1, then 2, then 3, and then 4. The variable i will go up to, but will not include, the integer passed to range(). Figure 2-14 shows a flowchart for the fiveTimes.py program.



When you run this program, it should print Jimmy Five Times followed by the value of i five times before leaving the for loop.


My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)
Note
You can use break and continue statements inside for loops as well. The continue statement will continue to the next value of the for loop’s counter, as if the program execution had reached the end of the loop and returned to the start. In fact, you can use continue and break statements only inside while and for loops. If you try to use these statements elsewhere, Python will give you an error.

As another for loop example, consider this story about the mathematician Karl Friedrich Gauss. When Gauss was a boy, a teacher wanted to give the class some busywork. The teacher told them to add up all the numbers from 0 to 100. Young Gauss came up with a clever trick to figure out the answer in a few seconds, but you can write a Python program with a for loop to do this calculation for you.
The result should be 5,050. When the program first starts, the total variable is set to 0 ❶. The for loop ❷ then executes total = total + num ❸ 100 times. By the time the loop has finished all of its 100 iterations, every integer from 0 to 100 will have been added to total. At this point, total is printed to the screen ❹. Even on the slowest computers, this program takes less than a second to complete.

(Young Gauss figured out that there were 50 pairs of numbers that added up to 101: 1 + 100, 2 + 99, 3 + 98, 4 + 97, and so on, until 50 + 51. Since 50 × 101 is 5,050, the sum of all the numbers from 0 to 100 is 5,050. Clever kid!)

# An Equivalent while Loop
You can actually use a while loop to do the same thing as a for loop; for loops are just more concise. Let’s rewrite fiveTimes.py to use a while loop equivalent of a for loop.
If you run this program, the output should look the same as the fiveTimes.py program, which uses a for loop.

# The Starting, Stopping, and Stepping Arguments to range()
Some functions can be called with multiple arguments separated by a comma, and range() is one of them. This lets you change the integer passed to range() to follow any sequence of integers, including starting at a number other than zero.

The first argument will be where the for loop’s variable starts, and the second argument will be up to, but not including, the number to stop at.


12
13
14
15
The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.

So calling range(0, 10, 2) will count from zero to eight by intervals of two.


0
2
4
6
8
The range() function is flexible in the sequence of numbers it produces for for loops. For example (I never apologize for my puns), you can even use a negative number for the step argument to make the for loop count down instead of up.
Running a for loop to print i with range(5, -1, -1) should print from five down to zero.


5
4
3
2
1
0

