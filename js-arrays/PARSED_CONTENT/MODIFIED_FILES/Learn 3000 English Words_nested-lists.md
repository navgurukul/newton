nested-lists_key1
nested-lists_key2


nested-lists_key3


nested-lists_key4


```python
[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] # input
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #output
```

nested-lists_key5


nested-lists_key6
- nested-lists_key7
- nested-lists_key8
```python
import types

varA = 10
varB = [12, 15]

type(varA) == types.IntType # True
type(varB) == types.IntType # False

type(varA) == types.ListType # False
type(varB) == types.ListType # True

```

nested-lists_key9
```python
import types

def nested_to_flat(lis):
    flat_list = []
    index = 0

    while (index < len(lis)):

        element = lis[index]

        if type(element) != types.IntType:
            flat_list = flat_list + nested_to_flat(element)
        else:
            flat_list.append(element)

        index += 1

    return flat_list
```