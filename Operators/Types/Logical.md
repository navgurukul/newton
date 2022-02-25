```ngMeta
name: Logical Operator 
submission_type: url
```
## LOGICAL OPERATOR (and, or, not) :- 

`Logical operators` are used to combine conditional statements. They are used in any programming language to make decision based on multiple conditions in python, we use logical operators to determine whether a condition is `True` or `False` by taking operand values as base. Let's consider different logical operators that are used in python programming.

(Logical operators help us to take decisions and make sure the required conditions are met to proceed.)


### `and :-` 
This `operator` is used to check that both the conditions it operates on must be true. If `both the conditions are true`, it will `return true`, otherwise (even if 1 condition is false or both conditions are false), the output will be False. 

Example : I want apples and oranges to make a fruit salad. Here, only one of them will not complete my salad, I want both.




#### Example :-

```python
a = True 
b = False 
print(a and b and a)
```

#### Output :-

`False`

#### Example :-

```python
number = int(input("enter the number"))
print(number and 1)
```
Here, the number and 1 are both true so the answer is 1.

If the input is 0 then the output will be 0 because one condition is false.



### `or :-` 
This `operator` is used to check that `one of the conditions it operates on must be true`. If `both the conditions are False`, it will return `False`, otherwise (if 1 condition is false or both conditions are true), the output will be true. 

Example: I want apples or oranges to make a fruit salad. Here, only one of them will be enough to complete my salad.

#### Example :-

```python
a = 4 > 5
a = 899 < 887
print(a or a or 7 < 8) 
``` 
#### Output :-

`True`

#### Example :-
```python
x = "apple"
y = "mango"
print(x or y)
```

#### Output :-

apple


- The `and` and `or` operators will give an output of the value at the moment their answer is determined. 
- For Example, `1 and 2` gives the output as 2 because when checking if both conditions are correct, the output or answer of `and` can be determined when it has checked the second condition.
- Similarly, for `0 and 2` the output is 0 as at the time of checking the first condition, the answer of the `and` operator is determined to be false since the first condition is false.**

- For `or`, similar to `and`,  `1 or 2` will produce an output of 1 as even if the first condition is true, the output to the `or` is determined there. 
- `0 or ""` will give `(empty String)` as the output is not 0 because the output is determined at the second condition.


### `not :-`
 This operator is used to get the opposite of the condition. So it gives the opposite output of whatever is the output of the condition. 


#### Example :-

```python
a = 19
b = 34
c = 56
print(not c > b)
 ```


#### Output :-

`False`
- c is actually greater than b so the condition c > b is true but adding `not` in front of it gives the opposite output, that is, false.
 
#### Example :-

```python
var1 =True
print(not var1)
a =True
b= False
print( a and b or a or not b)
```


#### Output :-

`True`


#### To understand logical operator and circuits watch this video

@[youtube](ZoqMiFKspAA&t=1s)
