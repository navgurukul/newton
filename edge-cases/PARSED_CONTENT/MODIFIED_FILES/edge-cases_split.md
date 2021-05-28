## split_key1
### split_key2
split_key3

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
    return a
```
split_key4### split_key5
- split_key6
- split_key7
split_key8


