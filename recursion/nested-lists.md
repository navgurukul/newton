## Nested Lists
Aise sochiye ki aapke paas ek list hai, jismei numbers bhi ho sakte hai, aur lists bhi, aur jo lists uss list mei hai, uske andar bhi numbers ya list ho sakte hai, aur aapko nahi pata ki kab list hai kab numbers, aur kitne levels deep tak aisa hai.

Kya aap aisa code likh sakte hai jo aisi `nested list` ko ek `flat list` mei convert karega, yaani saare elements chahe woh kitne bhi deep ho, woh ek nayi list mei directly accessible honge.

Jaise:

```python
[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] # input
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #output
```

Yeh aapko recursion ka use kar kar, karna hai.

## Hints
- Agar aapke paas andar ki saari lists flat hai, toh kya aap yeh recursion soch paa rahe hai? 

- Yeh check karne ke liye ki element integer hai ya list, aap aisa kar sakte hai:

```python
import types

varA = 10
varB = [12, 15]

type(varA) == types.IntType # True
type(varB) == types.IntType # False

type(varA) == types.ListType # False
type(varB) == types.ListType # True
```

## Solution
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