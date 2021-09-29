the-global-statement_key1
the-global-statement_key2


```python
  def spam():
❶    global eggs
❷    eggs = 'spam'

  eggs = 'global'
  spam()
  print(eggs)
```
the-global-statement_key3



the-global-statement_key4


the-global-statement_key5


the-global-statement_key6


the-global-statement_key7


the-global-statement_key8


the-global-statement_key9


the-global-statement_key10


```python
  def spam():
❶  global eggs
    eggs = 'spam' # this is the global

  def bacon():
❷  eggs = 'bacon' # this is a local
  def ham():
❸  print(eggs) # this is the global

  eggs = 42 # this is the global
  spam()
  print(eggs)
```
the-global-statement_key11



the-global-statement_key12
the-global-statement_key13
the-global-statement_key14


the-global-statement_key15


```python
  def spam():
      print(eggs) # ERROR!
❶    eggs = 'spam local'

❷ eggs = 'global'
   spam()
```
the-global-statement_key16



the-global-statement_key17


the-global-statement_key18


the-global-statement_key19


the-global-statement_key20
