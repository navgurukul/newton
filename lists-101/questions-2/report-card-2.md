```ngMeta

```

## Report Card - Part II

Iss list ko dekhein:

```python
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
```

Yeh kisi student ke peechle teen saal ke marks hai. Aap ko jitne bhi saal hai, har saal ke average marks print karne hai. Jaise, uppar wali list ka output yeh hona chahiye:

    1 year ka average - 84
    2 year ka average - 80
    3 year ka average - 63


## Edge Cases:
Check your program for following nested lists as well (bina code change kiye chalna chahiye, nahi toh aapne sahi se code nahi likha):

```python
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
```

Aapke code se uppar wali nested list ka solution yeh aana chahiye:

    1 year ka average - 84
    2 year ka average - 81
    3 year ka average - 72


Yeh list bhi bina error ke chalni chahiye, agar aapka program **robust** hai toh:

```python
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
```

Aapke code se uppar wali nested list ka solution yeh aana chahiye:

    1 year ka average - 84
    2 year ka average - 81
    3 year ka average - 72
    4 year ka average - 71

