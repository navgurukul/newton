```ngMeta
name: Conversion
```

  
**Note : Remember to run all the code examples and see them. Only by trying them will you be able to learn.**

# `What is Type Conversion`?

In the previous sections, we understood that there are different types of data types in Python. Some of the types we have read about are :

1.`Integer`
2.`Float`
3.`String`

Some examples are given below. Read them carefully.

```python
# integer
age = 27
total_apples = 100

# float
weight = 10.5
area = 120.56

# string
day = "Wednesday"
name = "Mahatma Gandhi"
a = "Y"
```
  
We can convert our data from one `type` to another `data type` in python. This will come in very handy in the future because we will often have data in one type and we will have to convert to another type. In Python we can do these `type conversions` -

1.`Float to String`
2.`Float to Integer`
3.`Integer to String`
4.`Integer to Float`
5.`String to Float`
6.`String to Integer`


# `String to Integer & String to Float`
Now let us see how to convert to `Integer`. `Type cast 12` to Python `Integer` and store 12.

```python
var_a = '12'
var_b = int(var_a)
print (type(var_a))
print (type(var_b))
print (var_a + var_a)
print (var_b + var_b)
```

Python does not know how to extract `integers` from `12houses`.
```python
var_a = '12houses'
var_b = int(var_a)
print (type(var_a))
print (type(var_b))
```

Python tries to convert `String` to `Integer` but throws an error if it is even a bit confusing. Ex :- Python cannot convert `12.2`, and `12houses` to integer but can do the same for `12`.

Python does not know how to extract integers from `12`
```python
var_a = '12.2'
var_b = int(var_a)
print (type(var_a))
print (type(var_b))
```

# `Float to Integer & Float to String`

Converts any `float` to Python `integer` by removing its decimal part.

```python
var_a = 12.2
var_b = int(var_a)
print (type(var_a))
print (type(var_b))
print (var_b)
```

Now we will learn to `typecast` in `FLOAT`. This is similar to `typecasting` to `Integer`. See it yourself.

```python
var_a = '12'
var_b = float(var_a)
print (type(var_a))
print (type(var_b))
print (var_a + var_a)
print (var_b + var_b)
```

```python
var_a = '12.2'
var_b = float(var_a)
print (type(var_a))
print (type(var_b))
```

Python does not know how to extract `Float` from `12houses`.

```python
var_a = '12houses'
var_b = float(var_a)
print (type(var_a))
print (type(var_b))
```

# `Integer to Float & Integer to String`

  
Python simply adds the decimal point when we convert `INTEGER` to `FLOAT`.
```python
var_a = 12
var_b = float(var_a)
print (type(var_a))
print (type(var_b))
print (var_b)
```

Look carefully here that Python adds `.0` to the last.  Try converting a `Float` 12.2 to `Integer` in Python. Try and understand what is happening.