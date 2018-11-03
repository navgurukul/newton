```ngMeta
name: using-for-loops-with-lists
completionMethod: manual
```
# Using for Loops with Lists
In Chapter 2, you learned about using for loops to execute a block of code a certain number of times. Technically, a for loop repeats the code block once for each value in a list or list-like value. For example, if you ran this code:

```python
for i in range(4):
    print(i)
```
the output of this program would be as follows:


0
1
2
3
This is because the return value from range(4) is a list-like value that Python considers similar to [0, 1, 2, 3]. The following program has the same output as the previous one:

```python
for i in [0, 1, 2, 3]:
    print(i)
What the previous for loop actually does is loop through its clause with the variable i set to a successive value in the [0, 1, 2, 3] list in each iteration.
```

# Note
In this book, I use the term list-like to refer to data types that are technically named sequences. You don’t need to know the technical definitions of this term, though.

A common Python technique is to use range(len(someList)) with a for loop to iterate over the indexes of a list. For example, enter the following into the interactive shell:

```python
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
```
Using range(len(supplies)) in the previously shown for loop is handy because the code in the loop can access the index (as the variable i) and the value at that index (as supplies[i]). Best of all, range(len(supplies)) will iterate through all the indexes of supplies, no matter how many items it contains.