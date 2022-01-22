```ngMeta
name:  Question 4
submission_type: url
```
## Question 4

What will be the output of the code given below?


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

