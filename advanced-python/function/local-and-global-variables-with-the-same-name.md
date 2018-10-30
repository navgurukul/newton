```ngMeta
name: local-and-global-variables-with-the-same-name
completionMethod: manual
```
# Local and Global Variables with the Same Name
To simplify your life, avoid using local variables that have the same name as a global variable or another local variable. But technically, it’s perfectly legal to do so in Python. To see what happens, type the following code into the file editor and save it as sameName.py:

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
When you run this program, it outputs the following:


bacon local
spam local
bacon local
global
There are actually three different variables in this program, but confusingly they are all named eggs. The variables are as follows:

❶ A variable named eggs that exists in a local scope when spam() is called.

❷ A variable named eggs that exists in a local scope when bacon() is called.

❸ A variable named eggs that exists in the global scope.

Since these three separate variables all have the same name, it can be confusing to keep track of which one is being used at any given time. This is why you should avoid using the same variable name in different scopes.