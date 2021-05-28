## split_solution_key1
### split_solution_key2
split_solution_key3

```python
def split(s, delim):
    a = []
    i = 0
    temp_s = ''
    while(i<len(s)):
        if s[i] != delim:
            temp_s += s[i]
        else:
            a.append(temp_s)
            temp_s = ''
        i += 1
    a.append(temp_s)
    return a
```
