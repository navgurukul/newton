module_key1
module_key2


module_key3


1. module_key4
2. module_key5
3. module_key6
module_key7


module_key8
```python
import random
for i in range(5):
    print(random.randint(1, 10))
```
module_key9



module_key10


module_key11



module_key12


module_key13
    An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star; for example, from random import *.
    With this form of import statement, calls to functions in random will not need the random. prefix. However, using the full name makes for more readable code, so it is better to use the normal form of the import statement.


module_key14
module_key15


module_key16


```python
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```

module_key17
