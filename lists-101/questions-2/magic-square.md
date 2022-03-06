```ngMeta
name: magic-square
submission_type: url
```

## Is Magic Square?
`Magic Square` is that kind of square in which sum of each row, sum of each column and sum of both the diagonals is equal.   


You have to write this program that takes a `nested list` as input and checks whether it is a `magic square` or not? 

 This is a `magic square` because, 
```python
magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
```


# Rows
8 + 3 + 4 = 15
1 + 5 + 9 = 15
6 + 7 + 2 = 15

# Columns
8 + 1 + 6 = 15
3 + 5 + 7 = 15
4 + 9 + 2 = 15

# Diagonals
8 + 5 + 2 = 15
4 + 5 + 6 = 15


To visualize this sqaure, see it like a square. All the rows have same number of elements. Number of elements in row should be equal to number of elements in a column.

This is not a magic square :
```python
magic_square = [
    [5, 3, 7],
    [1, 8, 9],
    [6, 4, 2]
]
```


Rows
5 + 3 + 7 = 15
1 + 8 + 9 = 18

Because the sum of elements of the second row is not 15 nahi hai, therefore this is not a magic square.

### `Edge Case 1`

Pls see that the program that you wrote works for only 3x3 square or it works for any size of square.

Write this program for square of any size, square of any size so that if a user enters square of any size, your program should give the correct output.



### `Edge Case 2`
```python
magic_square = [
    [8, 3, 4, 0],
    [1, 5, 9],
    [6, 7, 2]
]
```
For this `nested list`, what will be your answer - `True` or `False`. 

#### Hint :

If the given `nested list` is not a `square`, then return `False`, on the first go.

