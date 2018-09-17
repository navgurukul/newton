```ngMeta
name: Functions - Dry Run
completionMethod: manual
```

<!--
Functions ka dry run aise kiya jaata hai. 
Issi tareeke se aap ko saare programs ka dry run karna hai. 
-->

```python
def a():
    b() + c()

def b():
    return 3

def c():
    return 7 * b()

print a()
```

```python
n = 10
def a(n):
    return n+2

print a(4)
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
def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)

print hcf(120, 100)
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

Jab Hum ek list ko as an argument pass karte hai, toh woh list copy ho kar nahi jaati, balki bas uska ek `reference` jaata hai. Iska matlab, jub hum uss function mei jaha par woh list bheji hai, ussmei jo hamari main item thi, wohi modify karte hai.

Jaise iss program mei, jab hum `a(example)` call karenge, toh jo `def a` mei changes honge, woh example variable ke andar ho jayenge. Jba hum `example` ko `print` karenge, toh `example` updated hoga.

```python
def a(l):
    al = len(l)
    for ( i in range()/2 ):
        l[i] = a[al-i]


example = [3,45,1,2,34]
a(example)
print example 
```

Yeh question karte waqt, aap uppar wale example ka dhyaan rakhiye.
```python
def partition(lst, start, end):
    pos = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos]
    return pos

def quick_sort_recursive(lst, start, end):
    if start < end:
        pos = partition(lst, start, end)
        quick_sort_recursive(lst, start, pos - 1)
        quick_sort_recursive(lst, pos + 1, end)

example = [3,45,1,2,34]
quick_sort_recursive(example, 0, len(example) - 1)
print example
```