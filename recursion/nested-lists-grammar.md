```ngMeta
submissionType: url
```
## Using Grammar to create Nested Lists

**Yeh thoda advanced concept hai. Iss par aap 4-5 ghante lagane ke baad bhi nahi samajh paa rahe, toh aap isse skip kar kar aage badh sakte hai**

Jaise English mei `Grammar` hoti hai, aise hi hamare code ki bhi grammar hoti hai. Issi grammar ko use kar kar `compiler` samajhta hai, hamare code ka kya matlab hai, aur woh matlab samajh kar, machine yaai computer samjhata hai. Jis `language` mei `compiler` `machine` ko woh code samjhata hai, usse `machine code` kehte hai.

Nested Lists ko grammar ko tarah se samajhte hai.

1. NESTED_LIST = [ INTEGER ]
2. NESTED_LIST = [ NESTED_LIST, INTEGER ]
3. NESTED_LIST = [ INTEGER, NESTED_LIST ]
4. NESTED_LIST = NESTED_LIST + NESTED_LIST

Dariye mat, yeh bahut simple se rules hai. Yeh rules kehte hai ki, right side mei jo bhi `grammar rules` diye gaye hai woh rules ko use kar kar aap ek nayi `nested list` bana sakte hai.

Jaise,

`[5]` ek `nested list` hai using Rule 1
`[[5], 2]` ek `nested list` hai using Rule 2
`[3, [[5], 2]]` ek `nested list` hai using Rule 3
`[5, 6, 7]` ek `nested list` hai using Rule 4 (kyuki yeh `[5]`, `[6]`, `[7]` jo teen nested lists hai unko jod kar banayi jaa sakti hai)

Aap dhyaan se dekhenge toh aap kisi bhi nested list ko inn rules mei break kar sakte hai. Ek example ke liye:

```python
[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] => [1] + [2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 4 and Rule 1 (for [1])
[2,     [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 3
[3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] => [3] + [4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 4
[4,             [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 3
and so on ...
```

Humein inn rules ko use kar kar ek recursion ka program likhna hai, jo ek random `nested list` generate karta hai.

## Hints
- Aap ke paas chaar rules hai, aap chaar rules mei se koi bhi rule randomly use kar kar ek `nested list` generate kar sakte ho
- Har rule ke liye aapko batana padega aapki nayi list kaise hogi
- Aap ek generateRandomNumber naam ka function use kar sakte hai, `INTEGER` generate karne ke liye, aur
- Aap ek generateRandomNestedList naam ka function use kar sakte hai `NESTED_LIST` generate karne ke liye, yeh function recursive hoga

## Solution

```python
import random

rules = [ "[INTEGER]", "[NESTED_LIST, INTEGER]", "[INTEGER, NESTED_LIST]", "NESTED_LIST + NESTED_LIST"]

def generateRandomNumber():
    return random.randrange(1, 20)

def generateRandomNestedList():
    random_rule = random.randrange(4)
    if random_rule == 0:
        return [generateRandomNumber()]

    elif random_rule == 1:
        return [generateRandomNestedList(), generateRandomNumber()]

    elif random_rule == 2:
        return [generateRandomNumber(), generateRandomNestedList()]

    elif random_rule == 3:
        return generateRandomNestedList() + generateRandomNestedList()

print generateRandomNestedList()
```

## Aage
Agar aap ko thoda aur samajhna ka mann hai, toh aap nested_list of INTEGER and STRINGS mix ke rules likh kar, usko generate karne ka cocde likh sakte hai.

## Bahut Aage
Agar aapko yeh exercise interesting lagi, aur aap yeh samajh paa rahe hai, toh aap Shakuntala Devi ka code samajh sakte hai. Woh issi logic ko use kar kar likha gaya hai.

Code [yaha](https://github.com/navgurukul/shakuntala-devi) par available hai.
