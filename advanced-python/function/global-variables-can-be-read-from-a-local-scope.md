```ngMeta
name: global-variables-can-be-read-from-a-local-scope
```
# Global Variables Can Be Read from a Local Scope
Consider the following program:


def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
Since there is no parameter named eggs or any code that assigns eggs a value in the spam() function, when eggs is used in spam(), Python considers it a reference to the global variable eggs. This is why 42 is printed when the previous program is run.