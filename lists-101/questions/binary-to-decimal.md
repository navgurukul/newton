```ngMeta
submission_type: url
```

## Binary to Decimal

In this program, if we are given any number in **binary form**, then we will learn to convert that number in **decimal form**.

![binary](../assets/binary.jpg)

Please see this diagram.

```python
binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
```

To convert this number in `decimal form`:-

```python
# last element ko 2^0 yaani 1 se
# second last element ko 2^1 yaani 2 se
# third last element ko 2^2 yaani 4 se
# fourth last element ko 2^3 yaani 8 se
# ...
# ...
# 
# multiply kar kar
# add karna hai
```

After doing the above steps, you will get **155** as an answer.

## `Edge Case`
```python
binary_number = [1, 0, 0, 2, 1]
```

What will be the output of this program? If your progrsm is **robust** then it will give invalid output, otherwise it will throw an error.

```python
binary_number = [1, 0, 0, "1", 1]
```

If your program is **robust** :

    - then it will give invalid output, or
    - it will consider "1" as 1 ki and solve the question.

But, if it will not be **robust**, then it will throw error.