Fibonacci series yeh hoti hai: 

**0, 1, 1, 2, 3, 5, 8, 13, 21, 34**

Iss series ka `pehla_number 0` hai aur `dusra_number` 1 hai. Aur uske baad har number `peechle do` numbers ka `sum` hota hai

Jaise,
`teesra number` = `pehla_number` + `dusra_number`
`1 = 0 + 1`
`chautha_number` = `dusra_number` + `teesra_number`
`2 = 1 + 1`

Aap isse recursion ka use kar kar - ek function banaye `fib` jo `number` parameter lekar uske corresponding `fibonacci number` return karta ho.

## Hint
Yeh ek aisi recursion hai jismei current value - ussi function ki last do values par depend karta hai.

## Solution
```python
def fib(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)
```

## Aage
Aap apni understanding expand karne ke liye yeh video dekh sakte hai.

@(youtube)[koFsRrJgioA]
