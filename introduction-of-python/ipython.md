# Now we will learn about iPython 

Here we will learn about, what is ipython  and why do we use it?


When you write   `python` on the Terminal , then   *python shell* opens on the Terminal. You write your python code  on the *python shell* to run it.
iPython also does the same work but it provides some extra features.Some of those features we will study below:

## Difference between python and iPython
### First with iPython 
First on the Terminal write `ipython` and press *Enter* .
Now ,write  `cd Downloads` in it and press*Enter*.
Then write `ls` and press *Enter* .
You will be able to see all the **folder and files** that you kept under Downloads folder .
Now to come outside the iPython shell write `quit` linside the shell and press **Enter** .


### Now we will do the same thing with python 

Write  `ipython` on the Terminal and press  **Enter**

Now write `cd Downloads` and press  **Enter**.

```python
>>> cd Downloads
  File "<stdin>", line 1
    cd Downloads
               ^
SyntaxError: invalid syntax
>>> 
```

You will be able to see something like this on the Terminal?
Which means you cannot go to the **Downloads** folder  with the help of  **python shell**.

For this you need to come out of the **python shell** and for that you need to type `quit` on the  **python shell**.

Now after coming outside type `cd Downloads` and then type  `ls` you will be able to see whatever is present in  Downloads .

You cannot change your **folder** by using normal **python shell** .For that you need to come out of the  **python shell**.But you can easily change the **folder** inside these python shell so that you don't need to come out of the **iPython shell** .

And when you will type in **python shell**.
```python
>>> if True:
... 
```
Then note that the cursor (**|**) comes without any space after this `...` .
But if you will type it in **iPython shell** then it will show like this.

```python
In [1]: if True:
   ...:     |
```
Then you will see that the cursor(**|**) comes after some spaces.
We call this as **Indentation** . When you will write the code for the first time **50% error** will be there because of lack of **Indentation** .
Hence ,iPython makes the life of an engineer very easy by providing extra features.

When iPython opens you can write  code in it.If you are copy pasting the code from somewhere then press `Ctrl + C` to copy paste and open iPython and type `%paste` for pasting the code.


## Very Important Rules
- Run each and every example on iPython shell.If you don't do this you will make a fool of yourself.
- To copy-paste and run the code will not help you in understanding the code.You have to run each and every code by yourself.
- Words written in UPPER CASE or **bold letters** are very important . Learn them ,you will come across them many times. 
- During the course You need to answer some questions at times. To answer those questions you can always upload a file.

## Some Code Samples

In this section some code samples are given. To get comfortable with iPython ,you can run them on ipython.

### Example 1

```python
print ("It will print this.")
print ("Cool Stuff "*10)
```

### Example 2

```python
time = input("Is it morning or evening? (morning/evening) ")
if time == "morning":
    print ("Let's go for a run!")
elif time == "evening":
    print ("Let's go out for a coffee.")
else:
    print ("I did not understand what input you put?")
```
