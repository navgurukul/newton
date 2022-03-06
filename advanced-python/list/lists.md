```ngMeta
name: lists
```
# Lists
One more topic you’ll need to understand before you can begin writing programs in earnest is the list data type and its cousin, the tuple. Lists and tuples can contain multiple values, which makes it easier to write programs that handle large amounts of data. And since lists themselves can contain other lists, you can use them to arrange data into hierarchical structures.

In this chapter, I’ll discuss the basics of lists. I’ll also teach you about methods, which are functions that are tied to values of a certain data type. Then I’ll briefly cover the list-like tuple and string data types and how they compare to list values. In the next chapter, I’ll introduce you to the dictionary data type.

The List Data Type
A list is a value that contains multiple values in an ordered sequence. The term list value refers to the list itself (which is a value that can be stored in a variable or passed to a function like any other value), not the values inside the list value. A list value looks like this: ['cat', 'bat', 'rat', 'elephant']. Just as string values are typed with quote characters to mark where the string begins and ends, a list begins with an opening square bracket and ends with a closing square bracket, []. Values inside the list are also called items. Items are separated with commas (that is, they are comma-delimited). For example, enter the following into the interactive shell:

```python
   >>> [1, 2, 3]
   [1, 2, 3]
   >>> ['cat', 'bat', 'rat', 'elephant']
   ['cat', 'bat', 'rat', 'elephant']
   >>> ['hello', 3.1415, True, None, 42]
   ['hello', 3.1415, True, None, 42]
❶ >>> spam = ['cat', 'bat', 'rat', 'elephant']
   >>> spam
   ['cat', 'bat', 'rat', 'elephant']
```
The spam variable ❶ is still assigned only one value: the list value. But the list value itself contains other values. The value [] is an empty list that contains no values, similar to '', the empty string.

