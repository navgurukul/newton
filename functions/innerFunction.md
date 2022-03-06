```ngMeta
name: Inner Function
```

#  Python Inner Functions

A function which is written or defined inside another function is called inner function or nested function. In inner functions, we can access the scope of variable of the outer function but we can't change those variables.

**EXAMPLE:-**

```python
def f1():
   s = "I Love Navgurukul"
   def f2():
       print(s)
   f2()

f1()
 ```
**Output :-**


I Love Navgurukul


In the above example, f2() is a inner function and f1() is outer function. s  is a scope of vaiable f1() 

    
# Scope of variable in nested function


Such a place where we can find a variable and we can also access it when needed, that place is called variable scope.
We have read how we can access global variables inside a function, but, How do we access the variable inside the outer function? let's see the example:

**Example :-**

```python
def first_function():
    s = 'I love India'
    def second_function():
        print(s)	 
    second_function()
first_function()
 ```

`OUTPUT:- `

I love India


```python
def first_function():
    s = 'I love India'
    def second_function():
		s = "MY NAME IS JACK"
   	 	print(s)	 
    second_function()
    print(s)	
 
first_function()
 ```
`OUTPUT:-`

MY NAME IS JACK

I love India
