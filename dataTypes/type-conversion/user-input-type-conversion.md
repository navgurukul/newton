```ngMeta
name: type conversion
submission_type: url
```

## Introduction

In this section, we want to take input from user using python. Then we'll also explore doing `type conversions` with that input.

In the future, very often we will have to take some input from our users. To take an input in Python, we use `input`.

#### Example 1 :-

```python
user_input = input("Kuch input daaliye ")
print (user_input)
```
When it runs, python will stop and a cursor will appear. Here you have to put some inputs. Press `Enter` after you have made your input. Now, when you `print user_input`, whatever value you had to enter will be in the form of a `string` in the `user_input` variable.


#### Example 2 :-

Let us understand this in more detail by taking an example of another input.

```python
number1 = input("Enter a number ")
```

Look here that we have put a `string` inside the brackets of `raw_input`. The value of this `string` is `"Enter a number"`. Whatever `string` we put inside the inner brackets, that `string` is printed by Python before asking for input. It gives some hint to the user as to what to input. Like in the example above, python will print `"Enter a number"` before asking for input. And when the user presses `enter` after typing in a number (input), variable `number1` will have that value.  
  
If we do print `number1` in the `python shell`, then whatever value we have entered, will be printed.

## `Type Conversion of User Inputs`
  
Whenever we take user input from `input` to a variable it is in the `string` type. Meaning, whatever the user puts in, `raw_input` makes it a `string`.
```python
number2 = input("Enter a number ")
print (type(number2))
```
Here the data type of `number2` will be `string`. Whenever we take the value of a variable as input from `input`, that value is in the form of a `string`. If the user has to input a number, it will also be in the form of a `string`.


Like if here we entered 25 then `number2` would contain "25". Any value that has `quotes` in front of it is a `string`. To convert it to `  INTEGER` we have to use `int()`.

```python
number3 = int(number2)
print (type(number3))
```

#### Now you know how to take user input in python. Do you know how computer take user input from user if don't know you can watch this video

@[youtube](xnyFYiK2rSY)

## One more `type conversion and raw_input` example.

Below is a final example to understand all these things better. This example prints two numbers by taking the input and multiplying them.

```python
number_x = input("Pehla number daaliye ")
number_y = input("Dusra number daaliye")
number_x = int(number_x) # user_input se hume number_x string type mein mila
number_y = int(number_y) # user_input se hume number_y string type mein mila
print (number_x * number_y) # number_x aur number_y ka multiple kar ke result print hoga
```

Here it is important to understand that we convert `number_x` and `number_y` to integer before multiplying because with `input` we get input always in the form of a `string`.

### Fun Activity : 

*Run this example without converting `number_x` and `number_y` to `int` and see what error occurs. Google this error and try to solve it. Talk to your friends around you, too. For this, you will have to remove the lines with `number_x = int(number_x)` and `number_y = int(number_y)`.*