```ngMeta
submissionType: url
```
## Factorial
Factorial ek maths ka function hota hai, jiska kaafi jagah use hota hai, specially probability yaani chance calculate karne ke liye.

Factorial ko hum exclamation mark operator se dikhate hai. Jaise,

`7!`, `9!`, etc.

```python
7! => 7 * 6 * 5 * 4 * 3 * 2 * 1
```
Kisi bhi number ka factorial 1 se le kar uss number tak ke beech ke saare numbers ka product hota hai. Kya aap factorial function recursion ka use kar kar likh sakte hai?

## Hint
- Agar aapko `7!` factorial nikalna hai, aur aapke paas `6!` factorial given hai, toh aap kaise nikaloge? Agar aap yeh sahi se soch paa rahe hai, phir program likhna asaan ho jayega.

- Base case kya hoga?

## Solution
```python
def factorial(number):
    if number==1:
        return 1
    return number * factorial(number - 1)

print factorial(5)
```

## Aage
Yeh function aap bina recursion ke bhi likh sakte hai. Kya aap bina recursion ke bhi likh kar implemment kar sakte hai?
