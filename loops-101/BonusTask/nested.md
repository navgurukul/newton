```ngMeta
name:  Nested While Loop
submission_type: url
```
## `Nested while loop`

`Nested while loop` is defined as a loop witin a loop. In this, first the `inner loop` runs. When the inner loop becomes false, then only the outer loop runs and this process continues `until` the outer loop condition becomes `False`.


#### Example :-

```python
i = 1
j = 5
while i < 4:
    while j < 8:
        print(i, ",", j)
        j = j + 1
    i = i + 1
```
