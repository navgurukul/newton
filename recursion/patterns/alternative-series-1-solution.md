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
