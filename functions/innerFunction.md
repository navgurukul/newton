```ngMeta
name: Inner Function
```

#  Python Inner Functions

Ek function jo ki kisi dusre function ke andar likha jaata hai ya define kiya jaata hai use inner function ya nested function kehte hai. Inner functions, outer function ke scope ke variables
Ko access kar sakta hai lekin unn variables ko change nahi kar sakta hai.


**EXAMPLE:-**

```python
def f1():
   s = ‘I Love Navgurukul’
   def f2():
       print(s)
   f2()

f1()
 ```
`Output:- `


```
I Love Navgurukul
 ```

Upar diye gaye example mein, f2() inner function hai aur f1()outer function. s f1()  ka scope variable hai.

    
# Scope of variable in nested function


Aisi jagah jaha hum koi variable find kar sake aur jarurat hone par hum use access bhi kar sake uss jagah ko variable scope kehte hain.
Humne ye padh liya hai ki hum kaise ek function ke andar global variable ko access kar sakte hain, lekin, hum outerFunction ke andar wale variable ko kaise access karenge ? chaliye Example dekhte hain:

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
```
I love India
 ```

```python
def first_function():
    s = 'I love India'
    def second_function():
		s=’ MY NAME IS JACK’
   	 	print(s)	 
    second_function()
    print(s)	
 
first_function()
 ```
`OUTPUT:-`

```
MY NAME IS JACK

I love India
```