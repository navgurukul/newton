```ngMeta
name: Variables - Operators Precedence
completionMethod: manual
```

Iss exercise ko dry run karne ke liye, aapko operators ka order samajhna hoga. Jab bahut saare operators hote hai toh yeh order hota hai python mei importance ka.

1. Brackets (), [], {}
   - () - () round brackets mei jo likha hota hai woh sabse pehle execute hota hai. Yeh **functions** aur **expressions** mei use hote hai, jo aage describe kiye jayenge.
   - [] - Yeh **List** mei use karenge (aage explain kiya jayega)
   - {} - Yeh **Dictionaries** mei use karenge (aage explain kiya jayega)
2. Exponentiation - ** - jaise 2\*\*3 = 8 ya 3\*\*2 = 9
3. \*, /, %
    Multiplication, Division or Remainder operator teeno ka same weight hai
4. +, \-
    Addition, Subtraction - inn dono ka same weight hai
5. in, not in, is, is not, <, <=, >, >=, <>, !=, ==
    - <, <=, >, >=, <>, !=, == : comparison operators
    - in, not in : operators to test ki koi element list mei hai ya nahi
6. not
7. and
8. or

Yeh operators hum aage aur details mei samjhenge. Tension mat lena. Dheere dheere aap inke saath kaafi aaram feel karne lagenge.

<!-- Add a video here-->

**Yeh Dhyaan Rakhein ki jo operators same line mei hai, unka same weight hia. Jab hum left se right mei jayenge, toh same weight se yeh evaluate hoga. Eg.**

1. 15 / 3 * 4 = 12 (Pehle 15 ko 3 se divide karenge, phir jo answer hai **5**, usko 4 se multiply karenge.)
2. 9 * 2 / 4 = 4 (Pehle 9 ko 2 se divide karenge, phir jo answer hai **18**, usko 4 se divide karenge - aur jo quotient aayega woh output hoga.)

*Yeh Understanding ke saath inn ka dry karein. Aur apna answer laptop par code chala kar verify karein.*

```python
a = 100
a = a*2
a = a/4
a = a + 3 * a
a = a - a / 4
```

```python
a = (4 + 5) / 3
a = a * 8 / 4
a = a / 2 * 10
a = a + 2 * 10
a = a + 2 * 10 - 5
```

```python
a = (4 + 5) / 3
b = a * 8 / 4 - 10
a = b / 2 * 10
a = a + 2 * 10
a = b + 2 * 10 - 5
```

```python
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print "Value of (a + b) * c / d is ",  e

e = ((a + b) * c) / d
print "Value of ((a + b) * c) / d is ",  e

e = (a + b) * (c / d)
print "Value of (a + b) * (c / d) is ",  e

e = a + (b * c) / d
print "Value of a + (b * c) / d is ",  e
```