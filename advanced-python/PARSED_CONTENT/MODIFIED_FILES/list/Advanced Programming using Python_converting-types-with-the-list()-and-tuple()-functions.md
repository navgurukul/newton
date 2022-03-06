converting-types-with-the-list()-and-tuple()-functions_key1
converting-types-with-the-list()-and-tuple()-functions_key2


```python
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```
converting-types-with-the-list()-and-tuple()-functions_key3


converting-types-with-the-list()-and-tuple()-functions_key4
converting-types-with-the-list()-and-tuple()-functions_key5


```python
>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42
```
converting-types-with-the-list()-and-tuple()-functions_key6


converting-types-with-the-list()-and-tuple()-functions_key7


```python
❶ >>> spam = [0, 1, 2, 3, 4, 5]
❷ >>> cheese = spam
❸ >>> cheese[1] = 'Hello!'
   >>> spam
   [0, 'Hello!', 2, 3, 4, 5]
   >>> cheese
   [0, 'Hello!', 2, 3, 4, 5]
```
converting-types-with-the-list()-and-tuple()-functions_key8


converting-types-with-the-list()-and-tuple()-functions_key9


converting-types-with-the-list()-and-tuple()-functions_key10


![image](assets/000081.jpg)
converting-types-with-the-list()-and-tuple()-functions_key11


converting-types-with-the-list()-and-tuple()-functions_key12


![image](assets/000082.jpg)
converting-types-with-the-list()-and-tuple()-functions_key13


converting-types-with-the-list()-and-tuple()-functions_key14


![image](assets/000071.jpg)
converting-types-with-the-list()-and-tuple()-functions_key15


converting-types-with-the-list()-and-tuple()-functions_key16


converting-types-with-the-list()-and-tuple()-functions_key17


converting-types-with-the-list()-and-tuple()-functions_key18
converting-types-with-the-list()-and-tuple()-functions_key19


```python
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
```
converting-types-with-the-list()-and-tuple()-functions_key20



converting-types-with-the-list()-and-tuple()-functions_key21


converting-types-with-the-list()-and-tuple()-functions_key22
