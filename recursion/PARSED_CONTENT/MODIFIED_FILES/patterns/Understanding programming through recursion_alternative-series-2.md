alternative-series-2_key1
alternative-series-2_key2


alternative-series-2_key3
- alternative-series-2_key4
- alternative-series-2_key5
alternative-series-2_key6
```python
def pattern(number):
    if number == 1:
        return 10
    elif number % 2 == 0:
        return pattern(number - 1) + 1
    else:
        return pattern(number - 1) * 10
```
