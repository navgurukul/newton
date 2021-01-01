```ngMeta
name: Sum Of A List
submission_type: url
```
## Sum of a List
Agar aapko sum karna ho list ke elements ka recursion use kar kar, toh aap kaise karoge?

## Hint
- Ek list ke elements ka sum dekhne ke liye, aap pehle element ko baaki bachi hui list ke sum se jod kar dekh sakte hai
- Base case kya hoga?

## Solution
```python
# sum nahi use kar sakte as the function name, as sum python ka reserved keyword hai
# list nahi use kar sakte as an argument name, as list python ka reserved keyword hai

def sum_list(lis):
    if len(lis)==1:
        return lis[0]
    return lis[0] + sum_list(lis[1:])

print sum_list([1, 4, 7, 10])
```

## Aage
Kya aap aise hi ek length naam ka function bana sakte hai?
