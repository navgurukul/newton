```ngMeta
name: More about Booleans
```

## Introduction

Till now we have learned that booleans are a special data type. Similar to how `integer` and `float` store numbers and `string` can store anything, `boolean` can only store two values - `True` or `False`. 

We can use the `type` function in Python to find out the data type of any value.

```python
number1 = 124
type(number1) # yeh int karega. `int` ka matlab integer hota hai.

number2 = 123.4
type(number2) # float

string1 = "NavGurukul"
type(string1) # str

x = True
type(x) # bool. iska matlab boolean hota hai
type(4 < 5) # socho iska javab bool kyun aata hai?
```

### `If Conditions & Booleans`

Using programming, we instruct the computer to perform different actions under different conditions. For example:-

1. When you are in an elevator and press the button for the 1st floor, the elevator stops when it reaches the 1st floor. Similarly, if you press 2nd floor, the elevator will stop at 2nd floor.
2. When you send a message on Whatsapp, two `grey ticks` are shown when the message is not yet read by the receiver. As soon as the receiver reads the message, the `grey ticks` turn blue.

In the previous sections, we have learned to use `if statements` to specify such conditions. `If statements` use `boolean` values. Remember, we made use of `comparison operators` inside `if statements`:-

1. `<`
2. `<=`
3. `>`
4. `>=`
5. `>`
6. `!=`

These `comparison operators` raise a certain question. For example,

```python
number1 = 45
number2 = 56
if number2 > number1:
	print("Bada hai number2")
else:
	print("Number 2 bada nahi hai")
```

In the above example, `>` operator raises the question - **Is number2 greater than number1?** Notice carefully, there are only two possible answers to this question:-

1. Yes / True
2. No / False

When the answer is "Yes", the output of `>` is `True`. When the answer is "No", the output is `False`. Depending on this `True or False` value, the `if statement` executes the code. If the output was True, then the code inside the `if statement` will run, otherwise the code inside the else statement will run.

Try to run the following code:

```python
if True:
	print("Only I will run")
else:
	print("I will never run")
```

In the above example, `Only I will run` will be printed all the time. This is because we have specified `True` after `if`. This means that the condition to run the code inside if statement is always `True`, so it will get executed every time.

### Note:
 Try to write similar code using if-elif-else and discuss with your friends.