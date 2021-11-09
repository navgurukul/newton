local-and-global-variables-with-the-same-name_key1
local-and-global-variables-with-the-same-name_key2


```python
   def spam():
❶     eggs = 'spam local'
       print(eggs) # prints 'spam local'
   def bacon():

❷     eggs = 'bacon local'
       print(eggs) # prints 'bacon local'
       spam()
       print(eggs) # prints 'bacon local'

❸ eggs = 'global'
   bacon()
   print(eggs) # prints 'global'
```
local-and-global-variables-with-the-same-name_key3



local-and-global-variables-with-the-same-name_key4


local-and-global-variables-with-the-same-name_key5


local-and-global-variables-with-the-same-name_key6


local-and-global-variables-with-the-same-name_key7


local-and-global-variables-with-the-same-name_key8
