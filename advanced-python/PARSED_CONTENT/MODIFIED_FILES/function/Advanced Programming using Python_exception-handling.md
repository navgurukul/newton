```ngMeta
exception-handling_key1
```

exception-handling_key2
exception-handling_key3


exception-handling_key4


```python
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```
exception-handling_key5



exception-handling_key6


exception-handling_key7


exception-handling_key8


```python
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```
exception-handling_key9



exception-handling_key10


```python
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
```
exception-handling_key11



exception-handling_key12
