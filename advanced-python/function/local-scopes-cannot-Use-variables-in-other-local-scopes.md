```ngMeta
name: local-scopes-cannot-Use-variables-in-other-local-scopes
completionMethod: manual
```
# Local Scopes Cannot Use Variables in Other Local Scopes
A new local scope is created whenever a function is called, including when a function is called from another function. Consider this program:


  def spam():
❶    eggs = 99
❷    bacon()
❸    print(eggs)

  def bacon():
      ham = 101
❹    eggs = 0

❺ spam()
When the program starts, the spam() function is called ❺, and a local scope is created. The local variable eggs ❶ is set to 99. Then the bacon() function is called ❷, and a second local scope is created. Multiple local scopes can exist at the same time. In this new local scope, the local variable ham is set to 101, and a local variable eggs—which is different from the one in spam()’s local scope—is also created ❹ and set to 0.

When bacon() returns, the local scope for that call is destroyed. The program execution continues in the spam() function to print the value of eggs ❸, and since the local scope for the call to spam() still exists here, the eggs variable is set to 99. This is what the program prints.

The upshot is that local variables in one function are completely separate from the local variables in another function.