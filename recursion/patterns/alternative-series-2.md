```ngMeta
submissionType: url
```
## Pattern
10, 11, 110, 111, 1110, 1111, 11110, 11111, 111110, 111111 ...

## Hint
- Kisi bhi element ko nikalne ke liye
    - nth element (n-1)th element ka 10 times hai agar n odd hai
    - nth element (n-1)th element mei 1 jod kar milta hai agar n even hai toh
- Base Case ka dhyaan rakhein - jab 1st element nikalna ho

## Solution
```python
def pattern(number):
    if number == 1:
        return 10
    elif number % 2 == 0:
        return pattern(number - 1) + 1
    else:
        return pattern(number - 1) * 10
```
