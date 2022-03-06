```ngMeta
name: local-variables-cannot-be-used-in-the-global-scope
```
# Local Variables Cannot Be Used in the Global Scope
Consider this program, which will cause an error when you run it:

```python
def spam():
    eggs = 31337
spam()
print(eggs)
```
If you run this program, the output will look like this:

```python
Traceback (most recent call last):
  File "C:/test3784.py", line 4, in <module>
    print(eggs)
NameError: name 'eggs' is not defined
```
The error happens because the eggs variable exists only in the local scope created when spam() is called. Once the program execution returns from spam, that local scope is destroyed, and there is no longer a variable named eggs. So when your program tries to run print(eggs), Python gives you an error saying that eggs is not defined. This makes sense if you think about it; when the program execution is in the global scope, no local scopes exist, so there can’t be any local variables. This is why only global variables can be used in the global scope.