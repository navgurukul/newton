```python
def a():
    b() + c()

def b():
    return 3

def c():
    return 7 * b()

print a()
``````python
n = 10
def a(n):
    return n+2

print a(4)
``````python
def sum1(n):
    if (n==0):
        return 0
    return sum1(n-1) + n

print sum1(6)
``````python
def sum2(n):
    if (n==0):
        return 0
    else:
        return sum2(n-1) + n
print sum2(8)
``````python
def fib(n):
    if (n==0):
        return 1
    elif (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print fib(6)
``````python
def fib_series(n):
    if (n==1):
        return [1, 1]
    else:
        series = fib_series(n-1)
        return [series[0] + series[1]] + series

print fib_series(8)
``````python
def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)

print hcf(120, 100)
```

functions-dry-run_key1


@[youtube](https://youtu.be/aUgYYhe-nUc)```python
def is_present_in_list(number_to_search, list_to_search):
    length_of_list = len(list_to_search)

    if length_of_list == 1:
        if number_to_search == list_to_search[0]:
            return True
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

print is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9])
print is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9])

functions-dry-run_key2


functions-dry-run_key3
```

```
```python
def a(l):
    al = len(l)
    i = 0
    while(i<al/2):
        i += 1
        l[i] = l[al-i -1]


example = [3, 9, 1, 2, 7]
a(example)
print example
```

functions-dry-run_key4
```python
def partition(l, s, e):
    pos = s
    i = s
    while(i<e)
        if l[i] < l[e]:
            l[i],l[pos] = l[pos],l[i]
            pos += 1
        i = i+1

    l[pos],l[e] = l[e],l[pos]
    return pos

def so(l, s, e):
    if s < e:
        pos = partition(l, s, e)
        so(l, s, pos - 1)
        so(l, pos + 1, e)

example = [3, 9, 1, 2, 7]
so(example, 0, len(example) - 1)
print example
``````python
def so(l):
    i = 0
    while(i< len(l)-1):
        n = l[i]
        if l[i+1] < n:
            l[i] = l[i+1]
            l[i+1] = n
            so(l)
        i = i + 1    
    return l
 
l = [9, 2, 7, 5]
so(l)
 
print l
```functions-dry-run_key5
