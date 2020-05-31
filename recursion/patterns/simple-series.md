```ngMeta
submission_type: url
```

## Pattern
1, 4, 7, 10, 13, 16 ...

## Hint
- Kisi bhi element ko nikalne ke liye, aapko peechle element mei 3 add karna hai.
- Base Case ka dhyaan rakhein

## Solution
```python
def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3
```


