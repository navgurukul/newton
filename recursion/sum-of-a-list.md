## Sum of a List
Agar aapko sum karna ho list ke elements ka recursion use kar kar, toh aap kaise karoge?

## Hint
- Ek list ke elements ka sum dekhne ke liye, aap pehle element ko baaki bachi hui list ke sum se jod kar dekh sakte hai
- Base case kya hoga?

## Solution
```python

# list nahi use kar sakte as a keyword, as list python ka reserved keyword hai
def sum(lis):
    if len(lis)==1:
        return lis[0]
    return lis[0] + sum(lis[1:])

print sum([1, 4, 7, 10])
```