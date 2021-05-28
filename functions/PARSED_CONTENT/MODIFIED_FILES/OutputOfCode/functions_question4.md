```ngMeta
question4_key1
```
## question4_key2
question4_key3


```python
def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number/=10
    return sum

print(sumofdigits(123))

```
