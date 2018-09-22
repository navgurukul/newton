
```ngMeta
name: Lists Two
completionMethod: manual
```

Yeh `program` kya karte hai, inhe acche se samjhe aur inke dry run kare.

<!-- todo: explain list of list -->
```python
list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['hello', 'world', 'Namaste']]
print len(list)

```

<!-- todo: explain how does one colon work -->

```python
list = ['a', 'b', 'c', 'd', 'e']
print list[4:]
print list[10:]
print list[1:]
print list[1:4]
```

<!-- todo: explain this example - introduce this concept and then give examples to solidify -->
```python
list = [1,2]*3
print list
```

index ka matlab ki kaunsi jagah pe aayega, so isme `a = ['hello', 2]`  hello ka index **0** hai

<!-- todo: introduce range properly -->
```python
list1 = range(100, 110) #statement 1
print "index of element 105 is : ", list1.index(105) 
```

