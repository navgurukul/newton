```ngMeta
name: Functions - Dry Run
completionMethod: manual
```

```python
def sum1(n):
    if (n==0):
        return 0
    return sum1(n-1) + n

print sum1(6)
```

```python
def sum2(n):
    if (n==0):
        return 0
    else:
        return sum2(n-1) + n
print sum2(8)
```

```python
def fib(n):
    if (n==0):
        return 1
    elif (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print fib(6)
```

```python
def fib_series(n):
    if (n==1):
        return [1, 1]
    else:
        series = fib_series(n-1)
        return [series[0] + series[1]] + series

print fib_series(8)
```

```python
def is_present_in_list(number_to_search, list_to_search):
    length_of_list = len(list_to_search)

    if length_of_list == 1:
        if number_to_search == list_to_search[0]:
            return False
        else:
            return False
    
    if length_of_list == 2:
        if number_to_search == list_to_search[0] or number_to_search == list_to_search[1]:
            return True
        else:
            return False
            

    first_half_of_list = list_to_search[:length_of_list/2]
    second_half_of_list = list_to_search[length_of_list/2:]

    return is_present_in_list(number_to_search, first_half_of_list) or is_present_in_list(number_to_search, second_half_of_list)

print is_present_in_list(35, [23, 43, 87, 98, 35, 64, 18, 10, 80])
print is_present_in_list(36, [23, 43, 87, 98, 35, 64, 18, 10, 80])
```