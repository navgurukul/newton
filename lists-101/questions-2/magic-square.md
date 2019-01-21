```ngMeta
submissionType: url
```

## Is Magic Square?
Magic Square woh square hota hai jismei - har row ka, har column ka, and dono diagonals ka sum same hota hai.

Aapko yeh program likhna hai - jo ek nested list leta hai, aur dekhta hai ki woh magic square hai ya nahi?

E.g. Yeh magic square hai, kyuki
```python
magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
```
Rows
8 + 3 + 4 = 15
1 + 5 + 9 = 15
6 + 7 + 2 = 15

Columns
8 + 1 + 6 = 15
3 + 5 + 7 = 15
4 + 9 + 2 = 15

Diagonals
8 + 5 + 2 = 15
4 + 5 + 6 = 15


    Iss square ko visualise karne ke liye, isse ek square ki tarah dekhein. Har row mei same number of elements honge. Jitne elements ek row mei hai, utne hi columns iss square mei honge.

Yeh magic square nahi hai, kyuki:
```python
magic_square = [
    [5, 3, 7],
    [1, 8, 9],
    [6, 4, 2]
]
```
Rows
5 + 3 + 7 = 15
1 + 8 + 9 = 18

Kyuki second row ka sum 15 nahi hai, isliye yeh magic square nahi hai.

## Edge Case 1
Kya aapka likha program sirf 3x3 square ke liye chalta hai, ya kisi bhi size ke square ke liye chal jaata hai?

Isse kisi bhi square size ke liye likhe, jisse ki user koi bhi square size likhei toh aapka program sahi output de.

## Edge Case 2
```python
magic_square = [
    [8, 3, 4, 0],
    [1, 5, 9],
    [6, 7, 2]
]
```
Iss `nested list` ke liye aapka kya answer hoga - `True` ya `False`. Aapka answer kya hona chahiye.

**Hint** - Agar di hui `nested list` ek `square` nahi hai, toh aapko pehle hi `False` return karna chahiye.