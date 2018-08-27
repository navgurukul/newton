```ngMeta
name: KBC Part 3
completionMethod: peer
```

**Iss exercise ko karne ke liye aapko apni `KBC Part 2` waali file ki copy bana ke edit karni padegi.**

*Yaad rakho ki jahan bhi aap faso, pehle paper pe flowchart banane ki koshish karo.*

Yeh questions alag alag parts mein divided hai. Saare parts ko ek hi file mein code likh kar submit karna hai.

## Part 1

Apni `questions_list` pe iterate kar ke saare questions aur unki corresponding options print karo. Options print karne ke liye aapko `first_options`, `second_options`, `third_options`, `fourth_options` lists ka use karna padega. 

Example: Maan lo aapka question *What is the capital of India?* hai aur uski options hain, *Delhi*, *Mumbai*, *Jaipur*, *Chandigarh* toh aapko har question ke liye kuch aisa print karna hai:

```
What is the capital of India?

- Delhi
- Mumbai
- Jaipur
- Chandigarh
```

## Part 2

Upar `Part 1` waale code ko aise modify karo ki aap har question ke liye `raw_input` use kar ke user se uska answer input lein. User option ka number daalega answer mein. Jaise upar waale question mein `Delhi` sahi javab hai toh user `0` daalega. Agar `Mumbai` hota toh `1` daalta, `Jaipur` hota 

## Part 3

Ab ek `answers_list` naam ka empty list banao aur jab bhi user answer daale to user ke answer ko iss `answers_list` mein append kar de.

## Part 4

Iterate karte hue jab bhi aap question print karte ho, toh saath saath question ki length bhi print karo `len` function ka use kar ke. Jaise agar question *What is the capital of India* hai, toh aapko har question aise print karna hai:

```
What is the capital of India? - 29

- Delhi
- Mumbai
- Jaipur
- Chandigarh
```


Dekho question ke baad 29 print kiya hua, kyunki uss text ki length 29 hai.

Inn saare parts ka code ek hi file mein likh ke submit karein.