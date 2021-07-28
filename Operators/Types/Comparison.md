```ngMeta
name: Comparison Operators
submission_type: url
```
### Comparison operators:- 

We use `comparison operators` to compare 2 values. Their answer or result is always of the boolean data type.


| OPERATORS |           NAME            |  EXAMPLE |
| :-------- | :-----------------------: | -------: |
| `==`        |           Equal           | `10 == 10` |
| `!=`        |         Not Equal         | `10 != 13` |
| `>`         |       Greater than        |    `2 < 5` |
| `<`         |         Less than         |    `2 < 5` |
| `>=`        | Greater than or  equal to |   `2 <= 5` |
| `<=`        |   Less than or equal to   |   `2 <= 5` |


#### 1. **Equal(==):-** To check whether 2 values are equal, the `==` operator is used. (Since we know `=` is used for assignment so for equality it is `==`)

`Example 1 :-`

```python
a=5
b=5
print(a==b)
```

`Output :-`

`true`


`Example 2 :-`

```python
a=6
b=9
print(a==b)
```


`Output`

`false`

#### 2. **Not Equal (!=) :-** The `!=` operator is used to check if 2 values are unequal or not equal .


`Example 1 :-`

```python
x=10
y=13
print(x!=y)
```
`Output :-`

`true`

This means that x=10 and y=13 are not equal.


`Example 2 :-`

```python
a=32
b=32
print(a!=b)
```
`Output :-`

`false`

In the above example, both the values are equal, meaning the answer to the question "Are the 2 values unequal?" is false.

#### 3. **Greater than (>) :-** It is the same as in mathematics, it checks whether the value on the left is greater than the value on the right. If yes then the output is true otherwise it is false.


`Example1 :-`

```python
a=6
b=4
print(a>b) 
 ```

`Output :-`

`true`

This means a=6 is greater than b=4 and so the output is seen to be true.

`Example2 :-`

```python
x=7
y=9
print(x>y)
 ```

`Output :-`

`false`

In this example we are saying that the value of x is greater than y, which is wrong hence the output is false.


#### 4. **Less than (<):-** It is the same as in mathematics, it checks whether the value on the left is less than the value on the right. If yes then the output is true otherwise it is false.

`Example 1:-`

```python
x=6
y=9
print(x<y)
 ```
`Output :-`

`true`

In this example, x is smaller than y so the output is true.


`Example 2 :-`

```python
a=13
b=10
print(a<b)
 ```
`Output :-`

`false`

In this example, a is greater than b so the output is false.


#### 5. **Greater than or  equal to (>=) :-** It is the same as in mathematics, it checks whether the value on the left is greater than or equal to the value on the right. If yes then the output is true otherwise it is false.

`Example 1:-`

```python
a=23
b=15
print(a>=b) 
 ```
`Output :-`

`true`

Here, a is greater than b so the output is true.

`Example 2 :-`

```python
a=12
b=35
print(a>=b)
 ```
`Output :-`

false

Here since a is not greater than b and a is also not equal to b, the output is false.

#### 6. **Less than or equal to (<=) :-**

It is the same as in mathematics, it checks whether the value on the left is lesser than or equal to the value on the right. If yes then the output is true otherwise it is false.

`Example 1:-`

```python
x=6
y=9
print(x<=y)
 ```
`Output :-`

`true`

In the example above, x=6 is smaller than y=9 and thus, the output is true.

`Example 2 :-`

```python
x=8
y=6
print(x<=y)
 ```
`Output :-`

`false`

Here, x is neither less than y, nor equal to y, hence the output is false.
