```ngMeta
name: Indentation
```

# What is Indentation ?

Please have a look at the code given below. Now think about the output of this code without running.
```python
a = 10
if a * 2 == 20:
print ("Variable a when multiplied by 2 gives 20.")
else:
print ("Variable a when mutiplied by 2 does not give 20.")
```

What answer did you thought ? Please copy paste this code , save this in a file and run this code .You will notice that  this code will not print any output ,but gives error .To  understand about this error we need  to think from the point of view of python . Python will run this program as follows:-

1. In the first line it will put the value 10 in "a" .
2. In the second line python will check that whether multiplying **a** by 2 gives  result equal to 20 or not.
3. Till the third line  python will be able to know that on multiplying **a** 2 by we will definitely get 20.But python gets confused at this place ,it does not understands that whether it should only print  "Variable a when multiplied by 2 gives 20." or it needs to run the code given below also or not . Humans can easily understand this , but the computer gets mad and gives error.

We will write this program correctly as follows,

```python
a = 10
if a * 2 == 20:
    print ( )
else:
    print ("Variable a when mutiplied by 2 does not give 20.")
```

When  python will run this correct code , then its brain will work like this. 

1. In the first line it will put the value 10 in "a" .
2. In the second line python will check that whether multiplying **a** by 2 gives  result equal to 20 or not.
3. In the third line ,python will print "Variable a when multiplied by 2 gives 20."Now you will think that  python prints this line in this code then why it did not print in the  previous example .But , see a little carefully that the third line has started after some space. These spaces are called indent in python.Now ,python  understands that  on multiplying  **a** by  2  we get 20 ,if this condition is true , then we will run the lines which are indented below **if**.
4. In the 4th line  python finds else but it does not run else part because if part already ran. So, how to use if statement , try to  learn about this.

This  spacing in python is called indentation. Whenever there is a problem related to indentation , Python call it as an  Indentation Error This error looks like this:

```python
  File "<ipython-input-5-9eaf99c4383b>", line 3
    print ("a variable ko 2 se multiply kar ke 20 aata hai")
        ^
IndentationError: expected an indented block
```


# One more example

We will take more example and to understand it clearly. First run the code given below. After that read the text given below.
```python
counter = 1
while counter < 10:
	print ("The counter is" + str(counter))
	counter = counter + 1
	print ('--------')
```	

In this program, in the last  3 lines ` (‘print "The counter is" + str(counter)’, ‘counter = counter + 1’, ‘print "--------"’) ` if there is no indentation then python will not be able to understand that after while loop what it has to run?Python will get confused and will give an error. To indent a python  code is very important.If you see the program,you will realize that the code is divided into different parts:

1. In the first part, `counter` variable is defined and we write the line `while counter < 10` .
2. In the second part ,we have written that code which will run after for loop again and again till the for loop is running. 
The different parts of code are called code blocks and  in python to indent these blocks we use tab. 
To understand this , save the given code in a new file and see what output comes and how that output is different from the output of the code given above .After this discuss about what happened?
```python
counter = 1
while counter < 10:
	print ("The counter is" + str(counter))
	counter = counter + 1
print ('--------')
```

**Note: Whenever you write the code, then your editor should indent the code ,but if it does not do that ,then you can use the Tab key for indenting.**

**Note: You can also use  Space key for indentation. Space key  is difficult to use, as many error occur due to its use ,just because of this many error occur ,that is why many   Developers(Software Engineer) use Tab so that minor errors do not occur.**

# Multiple Levels of Indentation

In a given indented code block there can be  another indented code block. Study this code and understand and tell how the output come?Try to run this code and see if you thought correctly about the output or not.If not then use your brain to think about it more.

```python
counter = 1
while counter < 10:
	if counter % 2 == 0:
		print ("Counter is an even number.")
	print ("The counter is" + str(counter))
	counter = counter + 1
print ('--------')
```

Please see here that in this code , 2 levels of indented code blocks exist.  

1. After the first level `if counter % 2 == 0’ is present.`
2. In the second level `print ("Counter is an even number.")` is present.

Here, python will run if under while loop  and`print ("Counter is an even number.")`only when inside the loop `counter`value  is an even number.
