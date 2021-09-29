list-like-types:-strings-and-tuples_key1
list-like-types:-strings-and-tuples_key2


```python
>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
        print('* * * ' + i + ' * * *')

* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
```
list-like-types:-strings-and-tuples_key3


```python
>>> name = 'Zophie a cat'
>>> name[7] = 'the'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
```
list-like-types:-strings-and-tuples_key4


```python
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'
```
list-like-types:-strings-and-tuples_key5


list-like-types:-strings-and-tuples_key6


```python
>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
>>> eggs
[4, 5, 6]
```
list-like-types:-strings-and-tuples_key7


list-like-types:-strings-and-tuples_key8


```python
>>> eggs = [1, 2, 3]
>>> del eggs[2]
>>> del eggs[1]
>>> del eggs[0]
>>> eggs.append(4)
>>> eggs.append(5)
>>> eggs.append(6)
>>> eggs
[4, 5, 6]
```
![image](aseets/000076.jpg)
list-like-types:-strings-and-tuples_key9


list-like-types:-strings-and-tuples_key10


![image](aseets/000078.jpg)
list-like-types:-strings-and-tuples_key11

 
list-like-types:-strings-and-tuples_key12


list-like-types:-strings-and-tuples_key13


list-like-types:-strings-and-tuples_key14
