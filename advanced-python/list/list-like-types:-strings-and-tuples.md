```ngMeta
name:  list-like-types:-strings-and-tuples
completionMethod: manual
```
# List-like Types: Strings and Tuples
Lists aren’t the only data types that represent ordered sequences of values. For example, strings and lists are actually similar, if you consider a string to be a “list” of single text characters. Many of the things you can do with lists can also be done with strings: indexing; slicing; and using them with for loops, with len(), and with the in and not in operators. To see this, enter the following into the interactive shell:

```python
>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
        print('* * * ' + i + ' * * *')

* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
```
Mutable and Immutable Data Types
But lists and strings are different in an important way. A list value is a mutable data type: It can have values added, removed, or changed. However, a string is immutable: It cannot be changed. Trying to reassign a single character in a string results in a TypeError error, as you can see by entering the following into the interactive shell:

```python
>>> name = 'Zophie a cat'
>>> name[7] = 'the'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
```
The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string. Enter the following into the interactive shell:

```python
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'
```
We used [0:7] and [8:12] to refer to the characters that we don’t wish to replace. Notice that the original 'Zophie a cat' string is not modified because strings are immutable.

Although a list value is mutable, the second line in the following code does not modify the list eggs:

```python
>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
>>> eggs
[4, 5, 6]
```
The list value in eggs isn’t being changed here; rather, an entirely new and different list value ([4, 5, 6]) is overwriting the old list value ([1, 2, 3]). This is depicted in Figure 4-2.

If you wanted to actually modify the original list in eggs to contain [4, 5, 6], you would have to do something like this:

```python
>>> eggs = [1, 2, 3]
>>> del eggs[2]
>>> del eggs[1]
>>> del eggs[0]
>>> eggs.append(4)
>>> eggs.append(5)
>>> eggs.append(6)
>>> eggs
[4, 5, 6]
```
<!-- ![image](aseets/000076.jpg)
 -->
 When eggs = [4, 5, 6] is executed, the contents of eggs are replaced with a new list value.

In the first example, the list value that eggs ends up with is the same list value it started with. It’s just that this list has been changed, rather than overwritten. Figure 4-3 depicts the seven changes made by the first seven lines in the previous interactive shell example.

<!-- ![image](aseets/000078.jpg)
 -->
 
 The del statement and the append() method modify the same list value in place.

Changing a value of a mutable data type (like what the del statement and append() method do in the previous example) changes the value in place, since the variable’s value is not replaced with a new list value.

Mutable versus immutable types may seem like a meaningless distinction, but Passing References will explain the different behavior when calling functions with mutable arguments versus immutable arguments. But first, let’s find out about the tuple data type, which is an immutable form of the list data type.
