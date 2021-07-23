```ngMeta
name: Reverse Order

```

Code likho jo neeche di gayi lists ke items ko reverse order yaani ki ulta print kare.

```python
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
```

Aapke code ka outut yeh hona chaiye:

```
kerela
punjab
rajasthan
gujrat
delhi
```

## Hints
Jab `index i` hai, tab `length - i -1` index par kya hoga.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]

| i     | places[i] | length - i| places[length - i] |
|-------|:---------:|:---------:|-------------------:|
|0      | "delhi"   |4          | "kerala"           |   
|1      | "gujrat"  |3          | "punjab"           |   
|2      |"rajasthan"|2          | "rajasthan"        |   
|3      | "punjab"  |1          | "gujrat"           |   
|4      | "kerala"  |0          | "delhi"            |   