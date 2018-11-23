```ngMeta
name: rounding-numbers
completionMethod: manual
```
# Rounding Numbers
When working with times, you’ll often encounter float values with many digits after the decimal. To make these values easier to work with, you can shorten them with Python’s built-in round() function, which rounds a float to the precision you specify. Just pass in the number you want to round, plus an optional second argument representing how many digits after the decimal point you want to round it to. If you omit the second argument, round() rounds your number to the nearest whole integer. Enter the following into the interactive shell:

```python
>>> import time
>>> now = time.time()
>>> now
```
1425064108.017826
```python
>>> round(now, 2)
```
1425064108.02
```python
>>> round(now, 4)
```
1425064108.0178
```python
>>> round(now)
```

1425064108
After importing time and storing time.time() in now, we call round(now, 2) to round now to two digits after the decimal, round(now, 4) to round to four digits after the decimal, and round(now) to round to the nearest integer.

