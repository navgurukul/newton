## Solution
```python
def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3
```
