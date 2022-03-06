```ngMeta
submission_type: url
```
## Pattern
1, 4, 8, 11, 22, 25, 50, 53, 106 ...

## Hint
- Kisi bhi element ko nikalne ke liye
    - nth element (n-1)th element ka double hai agar n odd hai
    - nth element (n-1)th element mei 3 jod kar milta hai agar n even hai toh
- Base Case ka dhyaan rakhein - jab 1st element nikalna ho

## Solution
```python
def pattern(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        return pattern(number - 1) + 3
    else:
        return pattern(number - 1) * 2
```





