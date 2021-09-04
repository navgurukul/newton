## What can we do with Lists?

In this exercise, we will try to understand how do we use `LISTS`. Just as we saw that a `list` contains a collection of values. So we need to find a way, that how can we access these values.

```python
names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
print names_list[1]
```

What happened when we wrote `nameslist[1]`? Did "shivam" got printed? 

Here, `[1]` is called `INDEX`. To access any item of a list, we use the INDEX of that item. Let us see what is the index of all the items in the given list.

`["annu", "shivam", "deepa", "pooja", "rupa"]`

1. `annu` has `index` 0
2. `shivam` has `index` 1
3. `deepa` has `index` 2
4. `pooja` has `index` 3
5. `rupa` has `index` 4

If you see carefully, then you will notice that the INDEX of that ITEM is one less than its position. The counting of the INDEX starts from 0, not from 1.

|["annu",  | "shivam",  | "deepa",  | "pooja",   | "rupa"] |
|----------|:----------:|:---------:|:----------:|--------:|
| 0        | 	1       | 2         | 3          | 4       |

```python
names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]

print names_list[0] # se "annu" print hoga

print names_list[4] # se "rupa" print hoga

print names_list[5]
```

Does the last line gives you error ? 

> list index out of range

Simply means - whatever `INDEX` you have given, that INDEX is out of range of the given `indices` of list. (indices - plural of index).

#### Question
What is the maximum INDEX that we can put? 

#### Answer
1 less than the length of the INDEX. If we will put more value than the range of the index, then `index out of range` error will come.

Try to google this error and understand about it. This error will not leave you ;), its better that you understand it now only.

### Changing List Items

In the same way we can update/change the ITEMS in a given LIST.

```python
names_list[0] = "abhishek"
print names_list
```

Did you notice anything? The ITEM present at 0 INDEX has now been changed to "abhishek". Similarly, run this code now.
```python
names_list[3]="rishabh"
print names_list
```

The ITEM that was present at  INDEX 3 has now changed to "rishabh". Keep in mind that INDEX is 1 less than the position of the item. Similarly, if you write something as given below :


```python
names_list[5]="dhruv"
```
So, you will get a list index out of range error, because at the 5th index no item exists. 

### Length of List and Adding values of the List
If we want to see the length of the list then we use the `len ()` (length function).

```python
names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
print len(names_list)
```
If we want to add one new value to a list then we will use `append` function. By using the `append()`, we can add an element at the end of the list.


```python
print names_list
names_list.append("dhruv")
print "length of the list is ", len(names_list)
print names_list
```
Here, you can see that previously the list length was `5` but after using the `append()`, the length of the list became `6`. When you printed `names_list` then the value `dhruv` was added in the last.


Let's append once again.

```python
names_list.append("alok")
print "length of the list is ", len(names_list)
print names_list
```

In this way, you can add as many elements as you want.

### Removing Elements from a List
Just as we can add elements to the list, similarly we can remove elements from the list we can use the `pop()`. To remove the last element from the list we can use the `pop` function.

```python
names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
names_list.pop()
print "length of the list is ", len(names_list)
print names_list
```

Try to print it and see if the last element is removed or not. Let's try to one more element from the list.

```python
names_list.pop()
print "length of the list is ", len(names_list)
print names_list
```
You can use `pop` function with an argument also on a given list. That means you can also add `index` to the `pop function`, which will remove the desired element of the given index from the list. 

#### Example :-

```python
print "length of the list is ", len(names_list), names_list
names_list.pop(2)
print "length of the list is ", len(names_list), names_list
names_list.pop(2)
print "length of the list is ", len(names_list), names_list
```

### Check if Element exists in List
We can do a lot of interesting operations on the list. One of the important operations of lists is to check whether a particular element is present in the given ITEM LIST or not.

#### Example:-

```python
"shivam" in names_list
```
Its result will come as `True` because "shivam" element exists in `names_list`.


```python
"imtiyaz" in names_list
```

Its result will come as `False` because "imtiyaz" element does not exist in the `names_list`.

As this is a `Boolean value`, it will return (True/False), we can also use it with the `if statement`.

#### Example :-

```python
if "shivam" in names_list:
    print "Shivam ka naam `names_list` mei hai"
else:
    print "Shivam ka naam `names_list` mei nahi hai."
```

*Do you still remember what all we studied in the last Boolean lesson?*