```ngMeta
submissionType: url
```

# Count Occurences

**Occurences** - occur shabd se bana hai, jiska matlab hota hai, ki kitni baar aata hai.

**Sample List**
```python
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
```

**Output:**
```python
[["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]

a - 6 times
n - 3 times
t - 2 times
x - 2 times
u - 1 times
g - 1 times
```

Humei `char_list` mei jo bhi characters hai, unki `occurences` count karni hai, aur ek nested list mei save karni hai, phir uss nested list ko use kar kar jo output hai, woh print karna hai.

## Edge Case
```python
char_list = []
```

**Solution**
```python
[]
```