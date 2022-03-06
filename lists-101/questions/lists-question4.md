```ngMeta
name: Palindrome or not?
submission_type: url
```

A `palindrome` is a word, sentence, verse, or even a number that reads the same backward or forward. Like NITIN. Read Nitin either from left or right, it will be same. Similarly MOM is also a `palindrome`.

Write a code that checks whether a list is a palindrome or not. And print “Haan! palindrome hai” if its a `pallindrome` and “nahi! palindrome nahi hai” if its not a palindrome.

For the time being you can use the list given below for writing the code.

```python
name=[ 'n', 'i', 't', 'i', 'n' ]
```

Now, change your list, and test it with different values and then finally upload the correct code.

You can test for these values.

nayan => true
naina => false
anamana => true
ainaania => true
ainabnia => false

## Hints
When the `index is i`, then what will be at index `length - i -1`.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]

| i     | places[i] | length - i| places[length - i] |
|-------|:---------:|:---------:|-------------------:|
|0      | "delhi"   |4          | "kerala"           |   
|1      | "gujrat"  |3          | "punjab"           |   
|2      |"rajasthan"|2          | "rajasthan"        |   
|3      | "punjab"  |1          | "gujrat"           |   
|4      | "kerala"  |0          | "delhi"            |