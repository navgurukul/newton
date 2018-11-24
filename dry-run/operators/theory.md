```ngMeta
name: Operators Precedence
completionMethod: manual
```

## Understanding "Precedence" in Operators

<!-- TODO Aap iss video ko dekhein. -->

```python
a = 100
a = a*2
a = a/4
a = a + 3 * a
a = a - a / 4
```

Iska solution verify ya samajhne k liye aap yeh video dekh sakte ho.

@[youtube](https://www.youtube.com/watch?v=dwCIg0WjliI)

Aap ko es picture se yhe concept aur acha se samaz aa jaye ga.
![PEMDAS](assets/pemdas.png)

"PRECEDENCE" ka matlab hota hai - importance. Ki kaun sa **Operator** kitna important hai. Jaise School mei humne BODMAS padha hoga. BODMAS padh kar humne seekha tha ki kaise ek **`expression/statement`** mei agar *multiple operators* ho toh, kaunsa operator choose karte hai.

Aise hi Programming languages mei apne rule hote hai. Alag alag programming languages mei alag alag rules bhi ho sakte hai. Pehle - Hum Python ke liye yeh rules dekhte aur samajhte hai.

Iss exercise ko dry run karne ke liye, aapko operators ka order samajhna hoga. Jab bahut saare operators hote hai toh yeh order hota hai python mei importance ka.

1. Brackets `(), [], {}`
   - () - () round brackets mei jo likha hota hai woh sabse pehle execute hota hai. Yeh **functions** aur **expressions** mei use hote hai, jo aage describe kiye jayenge.
   - [] - Yeh **List** mei use karenge (aage explain kiya jayega)
   - {} - Yeh **Dictionaries** mei use karenge (aage explain kiya jayega)

2. Exponentiation - ** - jaise 2\*\*3 = 8 ya 3\*\*2 = 9
    Yaani `exponentiation` neeche diye gaye sab operators se jyada important hai. Computer pehle isko execute karega, neeche wale operators ko execute karne se pehle.

3. `*, /, %`
    Multiplication, Division or Remainder operator teeno ka same weight hai. Yaani jab computer teeno ko same importance deta hai. Jaise 
    left se right mei jaate hue, in teeno mei se pehle koi bhi operator dikhega, computer ussi operator ko use karega.
    
    Jab ki, agar yeh operator neeche diye hue operators ke baad bhi aayega, toh bhi inko jyada weight/preference/maanyta milegi, jiske vajah se pehle yeh operators execute, and phir neeche wale.

4. `+, -`
    Addition, Subtraction - inn dono ka same weight hai

5. `in, not in, is, is not, <, <=, >, >=, <>, !=, ==`
    - `<, <=, >, >=, <>, !=, ==` : comparison operators
    - `in`, `not in` : yeh operator yeh check karne ke liye kaam aate hai ki koi element list mei hai ya nahi. jaise 3 in [1,2,3] dekhta hai, ki `3 element`, `[1,2,3]` list mei hai ya nahi

6. not

7. and

8. or

Yeh operators hum aage aur details mei samjhenge. Tension mat lena. Dheere dheere aap inke saath kaafi aaram feel karne lagenge.

<!-- Add a video here-->

**Yeh Dhyaan Rakhein ki jo operators same line mei hai, unka same weight hia. Jab hum left se right mei jayenge, toh same weight se yeh evaluate hoga. Eg.**

1. 15 / 3 * 4 = 12 (Pehle 15 ko 3 se divide karenge, phir jo answer hai **5**, usko 4 se multiply karenge.)
2. 9 * 2 / 4 = 4 (Pehle 9 ko 2 se divide karenge, phir jo answer hai **18**, usko 4 se divide karenge - aur jo quotient aayega woh output hoga.)

*Yeh Understanding ke saath ab hum kuch questions ka dry karenge. Aur apna answer laptop par code chala kar verify karein.*
