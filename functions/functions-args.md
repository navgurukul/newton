```ngMeta
name: Function Arguments
```

## What are function arguments?

Some of the functions we've coded so far using by simple print statements. We can also write functions that take some data and do something with that data. Run this code.

```python
numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
print (max(numbers_list))
```

**Output :-**
`10`

Here we give `numbers_list` to the `max` function and it gives us the largest value out of it.

**max** function, is one of the pre-define function, where no need to defined the def max() to write the code of block because the creator of Python has already done this work for us.

Similarly, the len function also takes a list and gives us the count of items in the list.

We use the len( ) function to find the length of an array or sequence. It is also the python pre-define function.


`Example :-`

```python

a=[1,2,3,4,5,6]
print(len(a))
 ```

**Output :-**
6

Try the code below and see what is happening.

```python
def say_hello(name):
    print("Hello ", name)
    print("How are you?")
say_hello("Aatif")
 ```
**Output :-**

Hello , Aatif
How are you?

Here we have defined the function in the same way as in the previous example. Notice that the after `def say_hello` in the function brackets we write `name` and the bellow of that we write the `name` variable with the  print command. Here the name is called * parameter * whose value we can give at the time of calling the function.While calling the function in the last line, we have written `"Atif"` inside the brackets. The parameters we assign values ​​while calling a function are called arguments.

In this example we learn:

* Defined a function named `say_hello` which takes a parameter named `name` and prints something using that

* Then we called the function and at the time of calling the function, we gave an argument whose value was "Atif"

* When this function call then which we have given string "Atif" argument. Here its value goes to the name parameter and this value

* `name`  is passed to the parameter, so he can pass it inside the function to a variable named 'name'. We have written the print command by  using variable name.

**Note: This is a tricky concept, if you do not understand it very well, then you will definitely understand by reading it once and looking at other examples. ;-)**

## Multiple Function Arguments

We have written the code with only one function argument. Now let's write the code with a few more function arguments.


```python
def add_numbers(number1, number2):
    print("I will add two numbers.")
    print(number1 + number2)
add_numbers(120, 50)
num_x = 134
name = "Rinki"
add_numbers(num_x, name)
 ```

**Output :-**

I will add two numbers.
170
I will add two numbers.

TypeError: unsupported operand type(s) for +: 'int' and 'str'


Here we have defined a function named `add_numbers`. But see that in bracket we have written 2 parameters. To take more than one argument, put a comma after the arguments. We have given two integer parameters while calling the function by writing add_numbers(120, 50). Here the sequence/order of parameters is important. In this function call it would have been

* The value of `120` goes to *first parameter* `number1`Which is inside the function named variable number1
* The value of `50` goes to *second parameter* `number2` which is inside the function named variable number2
* Later we have defined two variables, `num_x` and `num_y` and then called add_numbers by giving num_x and num_y arguments.
*  The value of `num_x` is  `134` goes to the first parameter `number1` and the value of `num_y` is `Rinki` goes to the second parameter `number2` .

Let's see another example for better understanding.


As you saw that **output** shows the  **TypeError** why it is coming because of integer and string cann't be concatinate. We have store **integer** in the num1 and in the name store the **string**



```python
def say_hello_language(name, language):
    if language == "hindi":
        print("Namaste ", name)
        print("Aap kaise ho?")
    elif language == "punjabi":
        print("Sat sri akaal ", name)
        print("Tuhada ki haal hai?")
    else:
        print("Hello ", name)
        print("How are you?")
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")
 ```
**Output :-**


Sat sri akaal  Rishabh
Tuhada ki haal hai?
Hello  Armaan
How are you?
Hello  Abhishek
How are you?
Namaste  Kavay
Aap kaise ho?


This function takes two parameters, `name` and `language`and works like this:

* If `language` is  `"hindi"`, then should be print something in Hindi.
* If `language` is `"punjabi"`, then should be print something in Punjabi.
* If `"hindi"` or `"punjabi"`, you have given any langauge other than this, it will print in English.

To do this we defined a function that takes two arguments,  `name` and `language`.When we call `say_hello_language("rishabh", "punjabi")` see what happens:

* The string value "Rishabh" goes the first parameter which is `name` and the second parameter, `language` goes for "punjabi".

* Then our program uses if-elif-else to see what is the value of the language and print it to the correct language accordingly

* This happenes in the every function calls.


## One more example

Try to think about the output by reading it before running. Then run it to see if you thought the correct output or not.

```python
def say_hello_people(name_x, name_y, name_z, name_a):
    print("Namaste ", name_x) # In hindi
    print("Alah hafiz ", name_y) # In urdu 
    print("Bonjour ", name_z) # In french 
    print("Hello ", name_a) # In english 
say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")
 ```
**Output :-**


Namaste  Imitiyaz
Alah hafiz  Rishabh
Bonjour  Rahul
Hello  Vidya
Namaste  Steve
Alah hafiz  Saswata
Bonjour  Shakrundin
Hello  Rajeev


See in this function that, it takes 4 arguments, `name_x`, `name_y`, `name_z`, `name_a`. In the first line of `def`, we have written the names of 4 parameters with commas (`,`). The order in which we have written the parameters while calling the function, in the def line, In the same sequence/ order, the values ​​of the arguments go to the parameters.

The values ​​of the parameters in `say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")` are as follows:

* The value of `"Imtiyaz"` is passed to the first parameter `name_x`
* The value of `"Rishabh"`is passed to the first parameter `name_y`
* The value of `"Rahul"` is passed to the first parameter `name_z`
* The value of `"Vidya"` is passed to the first parameter `name_a`

## Python Arbitrary Arguments 

Arbitrary Arguments we use when do not know how many numbers we have of arguments are to be given in the function. We use ( * ) before parameters to define functions with arbitrary arguments as shown below.


`Example:-`

```python
def icecream(*flavours):
 for flavour in flavours:
  print("i love"+flavour)

icecream("chocolate", "butterscotch","vanilla","strawberry")
 ```

**Output :-**


i love chocolate
i love butterscotch
i love vanilla
i love strawberry 


## Default parameter value  

Here by default parameter value, we mean that we assign a value to a parameter while defining the function so that if we call the function without any argument, it will take the default value.


`Example :-`

```python
def attendance(name,status="absent"):
	print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh")
 ```

**Output :-**

kartik is present today
sonu is absent today
vishal is present today
Umesh is absent today
