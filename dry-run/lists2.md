
```ngMeta
name: Lists
completionMethod: manual
```

Yeh `program` kya karte hai, inhe acche se samjhe aur inke dry run kare.


```python
list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['hello', 'world', 'Namaste']]
print len(list)

```


Yeh `program` kya karte hai, list mai sai kaise elemenets fecth kar sakte hai.

```python
list = ['python', 'learning', '@', 'ng']
 
print list[::]          
print list[0:6:2]       
print list[ :6: ]       
print list[ :6:2]      
print list[ ::3]       
print list[ ::-2]     
```



```python
list = ['a', 'b', 'c', 'd', 'e']
print list[10:]
print list[1:]
```


```python
list = [1,2]*3
print list
print list[1:7]

list = ['a', 'b', 'c']*-3
print list
```

index ka mtlb ki kaunsi jagah pe aayega, so isme `a = [1, 2]` 1 **0** index per hai

```python
list1 = range(100, 110) #statement 1
print "index of element 105 is : ", list1.index(105) 
```

