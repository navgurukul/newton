sum-of-a-list_key1
sum-of-a-list_key2


sum-of-a-list_key3
- sum-of-a-list_key4
- sum-of-a-list_key5
sum-of-a-list_key6
```python
# sum nahi use kar sakte as the function name, as sum python ka reserved keyword hai
# list nahi use kar sakte as an argument name, as list python ka reserved keyword hai

def sum_list(lis):
    if len(lis)==1:
        return lis[0]
    return lis[0] + sum_list(lis[1:])

print sum_list([1, 4, 7, 10])
```

sum-of-a-list_key7
sum-of-a-list_key8
