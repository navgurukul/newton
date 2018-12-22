## Calculate

```python
def operate(num1, operator, num2):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2
```

Yeh ek simple sa function hai, jo do numbers leta hai, operator leta hai, aur unn numbers par woh operation kar kar return kar deta hai.

Maan lo user aap ko yeh input deta hai:

'3 + 5 - 2 * 4 / 2 + 8 - 10 * 9 / 3'

Aap ko ek function banana hai jo iss string ko evaluate karega, left se right ke order mei. Yaani agar sabhi operators ki same precedence (yaani importance) hoti, toh hum left se right chalte aur ek ek kar kar result calculate kar lete.

Jaise:
'3 + 5 - 2 * 4 / 2 + 8 - 10 * 9 / 3'
'8 - 2 * 4 / 2 + 8 - 10 * 9 / 3'
'6 * 4 / 2 + 8 - 10 * 9 / 3'
'24 / 2 + 8 - 10 * 9 / 3'
'12 + 8 - 10 * 9 / 3'
'20 - 10 * 9 / 3'
'10 * 9 / 3'
'90 / 3'
'30'
30 is the answer.
Agar aap dhyaan se sochenge toh yeh bhi ek recursion hai.

## Hint
- Kya yaha par aap `split` function use kar sakte hai?
  
- Base case kya hoga?
  
- What's the problem? Kya aap uss problem ko choti problem mei break kar sakte ho?
Yaani aap ke paas agar ek badi string hai, toh kis chotti string ka agar aapke paas answer hota toh, aapki problem bahut easily solve ho jaati.
  
## Solution
'3 + 5 - 2 * 4 / 2 + 8 - 10 * 9 / 3'
ko pehle split karein:
['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9', '/', '3']

Ab yeh dekhein:
[num1]
[num1, operator, num2]
`base cases` hai. Kyuki agar in dono mei se koi bhi input hoga, toh aapko answer bahut easily find kar sakte hai, `operate` function use kar kar.

`['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9']` - Agar aapke paas iska answer hai toh, maan lo, woh answer value hai. Toh aapke question ka answer
`[value, '/', '3']` hai. Yaani list ke last ke do elements skip kar kar, jo remaining hui list hai uska answer ka use kar kar, aap apne question ko solve kar sakte ho.

```python
def operate(num1, operator, num2):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2

def solve(question_list):
    if len(question_list)==1:
        return int(question_list[0])
    elif len(question_list)==3:
        return operate(int(question_list[0]), question_list[1], int(question_list[2]))
    else:
        return operate(solve(question_list[:-2]), question_list[-2], int(question_list[-1])) 

solve(['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9', '/', '3'])
```

## Aage
Yeh function aap bina recursion ke bhi likh sakte hai. Kya aap bina recursion ke bhi likh kar implemment kar sakte hai?