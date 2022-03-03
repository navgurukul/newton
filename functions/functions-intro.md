```ngMeta
name: Functions
```

# Basics of Functions

Function is a code of block that only runs when it is called.
In the function we pass the data which we call parameter. Function returns data.
By using functions, we can write some code once and use it many times. This makes our work very easy.

Christopher Wesson Bosh who is an American former professional basketball player and actively learning how to code along with helping others to learn programming once said, "I began to notice that the world around me was spinning on an axis powered by varying patterns of 1s and 0s. We’d be fools to ignore the power of mastering the designing and coding of those patterns." Let's hear his explanation about functions in the following video.

@[youtube](8T5acEwfJbw)

```python
print("NavGurukul")

def say_hello():
    print("Hello!")
    print("How are you?")

say_hello()
print("Python is awesome")
say_hello()
print("Hello…")
say_hello()
```

Run the code, it's output will be something like this.:


NavGurukul
Hello!
How are you?
Python is awesome
Hello!
How are you?
Hello…
Hello!
How are you?


Note that wherever `say_hello()` is written in the code, there the lines `Hello!` and `How are you?` are printed. This happened because in the second line we used the function `def say_hello()`. Now whenever this function is called, the code inside it will run. In this way we can use the same code again and again.

## Introduction to Functions

By using functions, we can write some code once and make it do the same thing again and again. You have already used too many functions. Read this code:  

```python
names_list = ["Fiza", "Shivam", "Imtiyaz", "Deepanshu", "Rahman"]
print(len(names_list))
```

`Ouput:-`

`5`

Here by using `len(names_list)` we know how many items are in the list.  Now we can count the items of any list by using `len` in our code. Here `len` is the fuction. Without functions, we would have to write code again and again to get the count of the items in the list. To understand this better, we will write its code ourselves in the next example.


We will write a function. Try this code first, and then read below to understand about it.

```python
def definition_say_hello():
    print("NavGurukul")
    print("In Navgurukul, we have to take responsibility for our learning.")

definition_say_hello()

print("In Navgurukul we treat all the people in the same way.")

definition_say_hello()
```
**Output :-**


NavGurukul

In Navgurukul, we have to take responsibility for our learning.

In Navgurukul we treat all the people in the same way.

NavGurukul

In Navgurukul, we have to take responsibility for our learning.


Another example to understand functions. Think of the output by reading this code. After trying this example, read carefully.

1. By using `def` in the beginning, we are telling python that we have written a function name `definition_say_hello`
![](assets/function_defn_inst_1.png)
2. The code of this function (two lines to print) is written under `def definition_say_hello()`by giving some indent (space). With these spaces, Python understands that this is the code of the function.
![](assets/function_defn_inst_2.png)
3. Then in the next line, `definition_say_hello()` we have called the function which runs the code inside the function. we can say  **FUNCTION CALL** 
![](assets/function_defn_inst_3.png)
4. After this using print statement we print one string.
![](assets/function_defn_inst_4.png)
5. Finally we called  the function again by writing`definition_say_hello()`. One more time the function runs the code inside once. With this the code inside the function - i.e. - *2 print* command runs.
![](assets/function_defn_inst_5.png)


```python
def function_say_bye():
    print("It was fun meeting with you. ")
    print("Bye bye")
function_say_bye()
function_say_bye()
print("Python is used a lot.")
function_say_bye()
function_say_bye()
 ```
**Output :-**


It was fun meeting  withyou. 
Bye bye
It was fun meeting with you. 
Bye bye
PPython is used a lot.
It was fun meeting with you.
Bye bye
It was fun meeting with you.
Bye bye

1. We create functions in python by using the `def` keyword. After `def` the name of the function, `function_say_bye` is written. After the name we put two brackets `(` `)`.
2. The brackets are followed by a colon `:`. The python semicolon understands that the code of the function is starting.
3. See that the entire function's code is written with an indent (space). Python understand that this is the code inside the function.
4. The code after print `print ("Bye bye")` is written without space. Python understand that the code of block function has finished.
5. Functions are also named according to the naming rules of variables.
Once memorize the naming rules of variables.

## Understand the Function Call 

Write the code below and see if any output is coming from it. If the output is not come then why is it not coming?

```python
def definition_hello_again():
    print("Again Hello :)")
    print("How are you?")
 ```

Now add this line to your code and see if any output comes.

```python
def definition_hello_again():
    print("Again Hello :)")
    print("How are you?")
definition_hello_again()
 ```

**Output :-**

Again Hello :)
How are you?


In Python, just writing the function does not run the code of the function. Here first we told python the code of the function by using the def keyword. It is called **"FUNCTION DEFINITION"**.

Then we later called the function by writing `definition_hello_again()` and the written code try to run. It is called as **"FUNCTION CALL"**. In  **"FUNCTION CALL"** we put 2 brackets `(` `)` after the name of the function. This tells Python that the code inside the function has to run.


@[youtube](https://www.youtube.com/watch?v=WkC7ktXM_8k)

@[youtube](https://youtu.be/AJJpGImQWLc)
