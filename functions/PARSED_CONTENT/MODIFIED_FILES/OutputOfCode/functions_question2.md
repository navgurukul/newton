```ngMeta
question2_key1
```
## question2_key2
question2_key3


```python
def primeorNot(num):     
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")

    else:
           print(num,"is not a prime number")
primeorNot(406)
```
