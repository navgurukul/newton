```ngMeta
name: Iterating two lists
```

## How to iterate on two lists together?

Let's say you have two lists of the same length. How will you iterate through both the lists together ?

```python
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]

print(len(students))
print(len(marks))
```

See if both the lists have same length as `6`. Below we have written a code on how to iterate through these lists.

```python
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
counter = 0
while counter < length:
	print(students[counter] + str(marks[counter]))
	counter+=1
```

You will notice here that elements of both the lists will be printed.

This lesson has only this much to read :D