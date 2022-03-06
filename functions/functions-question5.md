```ngMeta
name: Question 6
submission_type: url
```
## Question 6

This question is in 3 parts. Submit the three part of code by writing in the same file.

### Question (Part 1)

Create a function named `Calculator` which takes three arguments - `number_x`, `number_y`, `operation`. `number_x` and `number_y` we will take two integers and operation parameter defines the type of mathematical operation to be performed on the two integers. 
For ex:
* If "add" is given in the operation, it will return number_x and number_y by adding it.
* If "subtract" is given in the operation, it will subtract number_x and number_y and return it.
* If "multifly" is given in the operation, it will multifly number_x and number_y and return it.
* If "divide" is given in the operation, it will divide number_x and number_y and return it.

Below are examples of some function calls:

* Calling `calculator(20, 25, "add")` will return 45. 45 we will get by doing 20+25.
* Calling `Calculator(40, 3, "Subtract")` will return 37 on calling. 37 we will get by doing 40-3.
* Calling `Calculator(10, 4, "Multiply")` will return 40. We will get 40 by doing 10*4.
* Calling `calculator(40, 4, "Divide")` will return 10 for the call reason. We will get 10 by doing 40/3.

After writing the function, to do this function call the function and put the value in the variable.

* Add 24 and 20 and put the value in the number_1 variable
* Multiply 50 and 60 and put the value in the number_2 variable
* Divide 80 and 120 and put the value in the number_3 variable
* Subtract 90 and 23 and put the value in the number_4 variable


### Question (Part 2)

Now using `input` take 2 numbers input from the user.


**Note: Not neccesary to create any fuction.**

Call the calculator function 4 times again and again to add, substract, multifly, divide the two numbers and show the result in 4 different variables. 
Those variables would be named as:

* *add_result*  (store the add operation result) 
* *subtract_result* (store the subtract operation result) 
* *multiply_result* (store the multiple operation result)
* *divide_result* (store the divide operation result)

Then print the above four variables.


submit your final code :)

### Question (Part 2)

Write the code of a function named `list_change` which take 2 lists as integer arguments and then multiply the items of those lists which are on the same index number (order) and get them to return a new list.

**You have to use *calculator* function to multiply. Can't multiply normally.**

If we call the function like this:

```python
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
```

Here the value should be *multiple_list* :

```python
[10, 200, 150, 100]
```

10 is obtained by multiplying 5 and 2, 200 by multiplying 10 and 20, 150 by 50 and 3, 100 by 20 and 5.
