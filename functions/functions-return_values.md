```ngMeta
name: Return Values
submission_type: url
```

# How to return a value from a function?

We used some functions which returned some values, that is, returned some data.we've written functions that don't return anything.

Write a simple addition function that returns the data.

```python
def add_numbers(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum

sum1 = add_numbers(20, 40)
print(sum1)
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print(sum2)
print(sum3)
number_a = add_numbers(20, 40) / add_numbers(5, 1)
print(number_a)
```
**Output**

60
583
1246
10.0

* Here we have defined the function in the same way as we have been defining the functions till now. But in the last line in the function you will see something new.
* In the last line, we have used the `return` statement to tell the function that it will return the value of `number_sum`
* Since this function is returning the value of `number_sum`, we can easily store this value in a variable.
* Like we have put the value of the sum of `20` and `40` in the `sum1` variable, which is 60.
* We have returned a value from the function by using `return` in the last line of **function definition**. We call this the return statement. 'Return' means to give back.
* Functions that return some value, we can do very interesting things with those functions, Have a look in the line `number_a = add_numbers(20,40) / add_numbers(5,1)`. Here we have called two add_numbers in one statement and then the result of both of them (60 of the first and 6 of the second) is divided by these functions, which returns something, We can do that in such a statement. We have done in the division line.


We write the same function without the return value.




```python
def add_numbers_print(number_x, number_y):
    number_sum = number_x + number_y
    print (number_sum)
sum4 = add_numbers_print(4, 5)
print(sum4)
print(type(sum4))
```
**Output :-**

9
None
<class 'NoneType'>

We have written the code of the above function here, but did not use the return statement. Because of this, this function will not return anything to us because this function does not return anything, We cannot put the sum of our numbers in another variable like we did in the previous example.

Here if you will see the value of `sum4`' then it will show `None`. `None` means nothing. Simply numbers that do not return a value return "nothing". `None` is a data type in python. In the line containing `print (type(number4))` you will see that it will show the type of sum4 as None type. It means that there is nothing in it.

Read the code below and think what will happen.Now run the code and see if you thought right

```python
number_b = add_numbers_print(5, 4) / add_numbers_print(2, 1)
```
**Output :-** 

TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'


Here we have tried to simply divide the values ​​of a function that does not return any value. We just read that the functions which do not return, return None (meaning nothing). When we divide None by None here, Python gets freaked out and doesn't know what to do. Because of this the error returns. Python tells us the same in error:


**`unsupported operand type(s) for /: 'NoneType' and 'NoneType'`**

This means that Python is not dividing the value of NoneType by the value of NoneType itself and an error has occurred.

## Understandng function execution with a return statement

Before running this example, read its code and think about what this function will return and what it will print when we give 2 integer arguments to it.

```python
def add_numbers_more(number_x, number_y):
    number_sum = number_x + number_y
    print("Hello from NavGurukul ;)")
    return number_sum
    number_sum = number_x + number_x
    print("Will i reach here?")
    return number_sum

sum6 = add_numbers_more(100, 20)
```
**Output :-**

Hello from NavGurukul ;)



* Here this function will print "Hello from Navgurukul ;)" and return the value of 120. It will return the value of 120 using the line "return number_sum".

* The value `sum6` will become 120.

* Whatever code you have written below the first `return number_sum` line, none of that code will work. This won't work because python receives a return statement while the function is running, So Python returns the value using that return statement and then none of the code below runs.

In a little more depth, Understand execution of function in Python. Try to understand without running this code first. Then run it once and see.

```python
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"

    print("Will I be able to print? :-(")

mon_menu = menu("monday")
print(mon_menu)
tues_menu = menu("tuesday")
print(tues_menu)
fri_menu = menu("friday")
print(fri_menu)
```
**Output :-**


Butter Chicken
Mutton Chaap
Chole Bhature


* Our 'menu' function returns the value of the menu item of that day based on the 'day' argument.

* Here mon_menu will have the value of "Butter Chicken" because our if-elif-else statement here sees that the day is given as "Monday" then return the "Butter-Chicken". As soon as python sees the return statement, it returns "butter chicken" and the function stops running. Because of this the last print command does not run. Because even before that print command, the return statement always causes the function to stop running.

* Similarly when the value of day is "tuesday" then the return statement with return "Mutton Chaap" is executed

* And when both "Monday" and "Tuesday" are not there, the return statement with "Chole Bhature" gets executed.

* **But the return statement is executed from inside if-elif-else, Our program never reaches the last if statement and it is never printed.**

Now we will write the same function in such a way that the last print command is also run. and `Will I be able to print? :-("` print the line :

```python
def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print("Will I be able to print? :-(")
    return food
    print("But I'm not sure will print? :'(")
print(menu("monday"))
```
**Output :-**

Will I be able to print? :-(
Butter Chicken


Here we have not used return statement in if-elif-else directly. We took the variable name `food` and stored value which we want into. Now when if-elif-else is run, our program proceeds to the print statement below it. Because python has not yet received a return statement, the print command runs. After printing it returns the value of *food* variable from the return statement but the last one which is the print statement will not get printed. Because the return statement is run before that print statement and because of that python does not reach the required print statement

