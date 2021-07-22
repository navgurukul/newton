```ngMeta
name:  Question 4

```
## Question 4

Niche diye gye code snippet ki output kya hoga?


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

