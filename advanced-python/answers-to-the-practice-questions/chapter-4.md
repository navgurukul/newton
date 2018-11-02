```ngMeta
name: chapter-4
completionMethod: manual
```
# Chapter 4
The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.

spam[2] = 'hello' (Notice that the third value in a list is at index 2 because the first index is 0.)

'd' (Note that '3' * 2 is the string '33', which is passed to int() before being divided by 11. This eventually evaluates to 3. Expressions can be used wherever values are used.)

'd' (Negative indexes count from the end.)

['a', 'b']

1

[3.14, 'cat', 11, 'cat', True, 99]

[3.14, 11, 'cat', True]

The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)
While append() will add values only to the end of a list, insert() can add them anywhere in the list.
The del statement and the remove() list method are two ways to remove values from a list.
Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.
Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists use the square brackets, [ and ].
(42,) (The trailing comma is mandatory.)
The tuple() and list() functions, respectively
They contain references to list values.
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.