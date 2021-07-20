# Definitions

### Binary Numbers

Binary numbers are known as machine language or low level language ,binary numbers are made of 0 and 1 which humans cannot understand but computers can.


### Interpreter 

It checks the code line by line and the line at which error is present, interpreter  stops the code at that line and shows the name of error.
Interpreter  converts high level language to low level language with the help of which the computer is able to run the code.

**Interpreter is used for Python and Ruby programming languages.**

**Example :-**

```python
a = megha
print (a)
 ```
`Output `
`file "<string>",line 1, in <module>`

In  this example you saw that I have taken a variable named **a** and assigned/given  a string value to it but I forgot to put " "(quote).So, python was not able to identify the type of value I gave to the variable **a**.Therefore, the interpreter stopped the code at the line that contained error, and displayed the error.

### Compiler

Compiler is a software that scans the complete code in one go and if the code contains any error  ,then it shows the error at the end of the code.
Whereas the interpreter, stops the code at the line that contains error.

**Compiler is used in C and C++ programming languages.**
 
Note- To study Compiler and Interpreter in detail please click this link.  [Compiler and Interpreter](https://www.youtube.com/watch?v=e4ax90XmUBc&t=156s) 

### Case Sensitive 

Case sensitive means that the text that we have typed should be exactly same as we type it anywhere in the code.

**Example :-**

```python
var = 5
print(Var)
 ```
`Output`

`Var is not defined`

For example ,in the above example ,we have assigned a  variable named **var** and while printing we typed **Var** ,so an error was displayed because in python var and Var are different. In python small letters and capital letters are considered different.

Note- You can click this link to study  case sensitive in detail . [Case Sensitive](https://youtu.be/mNxDbLBBzno) 


### Error /  Bugs

When we make any mistake while writing the code ,that mistake is called error/bug.
**Examples :-**

```python
num=5
print(num
 ```
`Output`

`SyntaxError: unexpected EOF while parsing`

```python
num=5
print "a"
 ```
`Output`

`SyntaxError: invalid syntax`


In this example you saw that while printing I forgot to put parenthesis so it showed us a syntax error which means our code has some mistake/error.

### Debugs

Debug means to solve bug/error in the given code or removing the error from the code and writing the correct code which is as per the syntax.

**Examples**

```python
num=5
print(num)
 ```
`Output`

`5`

```python
num=2
Print (num)
 ```
`Output`

`2`

As you saw in the bug example   there was a bug present in the second code so we debugged that code.

### Source code

Source code is that code which humans can easily understand .
**Example** 
```python
name="python"
print(name)
 ```
`Output`

`python`

In this example you saw that we have taken a variable named as **name** and we have stored python in it.Ypu can easily read and understand this code .This code is called source code/main code.


![Types of brackets](https://www.grammar-monster.com/glossary/pics/types_of_brackets.png)
