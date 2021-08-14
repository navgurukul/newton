simple-series_key1
simple-series_key2


simple-series_key3
- simple-series_key4
- simple-series_key5
simple-series_key6
```python
def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3
```