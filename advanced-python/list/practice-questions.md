```ngMeta
name: practice-questions
completionMethod: manual
```
# Practice Questions

Q:

1. What is []?

Q:

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

Q:

3. What does spam[int(int('3' * 2) // 11)] evaluate to?

Q:

4. What does spam[-1] evaluate to?

Q:

5. What does spam[:2] evaluate to?

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

Q:

6. What does bacon.index('cat') evaluate to?

Q:

7. What does bacon.append(99) make the list value in bacon look like?

Q:

8. What does bacon.remove('cat') make the list value in bacon look like?

Q:

9. What are the operators for list concatenation and list replication?

Q:

10. What is the difference between the append() and insert() list methods?

Q:

11. What are two ways to remove values from a list?

Q:

12. Name a few ways that list values are similar to string values.

Q:

13. What is the difference between lists and tuples?

Q:

14. How do you type the tuple value that has just the integer value 42 in it?

Q:

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

Q:

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

Q:

17. What is the difference between copy.copy() and copy.deepcopy()?

# Practice Projects
For practice, write programs to do the following tasks.

# Comma Code
Say you have a list value like this:

```python
spam = ['apples', 'bananas', 'tofu', 'cats']
```
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.