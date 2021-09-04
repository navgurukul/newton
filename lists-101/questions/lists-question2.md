```ngMeta
name: Reverse Order
submission_type: url
```

Write a code that the reverses the order of the items means in opposite order.

```python
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
```

Your code output should be here :

```
kerela
punjab
rajasthan
gujrat
delhi
```

## Hints 
When `index i` is there, then what will be at index `length - i -1`.

`places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]`

| i     | places[i] | length - i| places[length - i] |
|-------|:---------:|:---------:|-------------------:|
|0      | "delhi"   |4          | "kerala"           |   
|1      | "gujrat"  |3          | "punjab"           |   
|2      |"rajasthan"|2          | "rajasthan"        |   
|3      | "punjab"  |1          | "gujrat"           |   
|4      | "kerala"  |0          | "delhi"            |   