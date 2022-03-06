```ngMeta
name: Solution
```

## Solution

## Question

Print this pattern.

```
#
##
###
####
#####
######
#######
```



## Solution

The solution to this question is given. This solution is written to give you more clarity on the concept. But, it would be much better if you try to solve it at first by yourself without looking at the solution.

We will understand a very small concept before understanding the solution. Suppose if we write `4*3` then `12` will come as we are multiplying two integers.

Similarly, if we multiply a string with an integer then it will behave differently.

```
>>> 'navgurukul' * 3
'navgurukulnavgurukulnavgurukul'
```

See carefully, here if we write `"navgurukul"*3` then `navgurukul` is printed `3` times. Similarly, if we do `hello * 5`, then `hello` is printed `5` times.

```
>>> 'hello' * 5
'hellohellohellohellohello'
```

Before writing the program we will observe some important things.

1. In this pattern there are `7` lines.
2. the First line has one `#`, the second line has 2 `#`, the third line has 3 `#`.
3. Means the number of `#` increases with the number of lines.

Its solution will be as follows:-

```
i = 1 # start the counter by 1
while i <= 7: #Because our program has 7 lines so the program will run for 7 times.
  print('#'*i)
  i = i + 1
```