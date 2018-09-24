```ngMeta
name: Exercises on Range
completionMethod: manual
```

<!-- fixme: wrong example -->
<!-- ```python
my_string = 'Hello world'
for i in range(len(my_string)):
    my_string[i].upper()
print (my_string)
``` -->

<!-- TODO: Put this as an edge case -->

<!-- ```python
my_string = 'hello world'
for i in range(len(my_string)):
    print (my_string)
    my_string = 'ng' -->

<!-- todo: introduce range properly -->
```python
list1 = range(100, 110)
```

```python
for i in range(5): #loop1
    for j in range(10): #loop2
        if (j > 3): 
            break 
        else:
            print "*", 
    print ''
```
Iss program ka `output` likh kar, iss program ko bina `break` statement ke likhiye.
Apne likhe hue naye program ka bhi `dry run` karein.

```python
for a in range(6):
    for b in range(6):
        if (a == b):
            break
        print '*',
    print ''
```
Iss program ka `output` likh kar, iss program ko bina `break` statement ke likhiye.
Apne likhe hue naye program ka bhi `dry run` karein.

```python
def a(l):
    al = len(l)
    for ( i in range()/2 ):
        l[i] = a[al-i]


example = [3, 9, 1, 2, 7]
a(example)
print example
```

Yeh question karte waqt, aap uppar wale example ka dhyaan rakhiye.
```python
def partition(l, s, e):
    pos = s
    for i in range(s, e):
        if l[i] < l[e]:
            l[i],l[pos] = l[pos],l[i]
            pos += 1

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
```

```python
def so(l):
    for i in range(len(l)-1):
        n = l[i]
        if l[i+1] < n:
            l[i] = l[i+1]
            l[i+1] = n
            so(l)
    return l
 
l = [9, 2, 7, 5]
so(l)
 
print l
```