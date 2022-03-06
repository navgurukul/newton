```ngMeta
name: Pass by Reference and Functions
submission_type: url
```

Iss program ko run karo aur dekho ki num_list aur num_list_sub_20 ki value same aa rahi. Iss code ko ais chane karo jisse hume num_list ki intial value bhi mil jaye.

```python
def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)
```
