```ngMeta
name: Question 9
completionMethod: peer
```

Harshad numbers aise number hote hain jo apni digits ke sum se dhang se divide hote hain. Dhang se divide hone ka matlab ki remainder 0 aata hai. Jaise 42 ek Harshad number hai kyunki 4 + 2 = 6 aur 42 ko 6 se vidie kar ke remainder aata hai

Aise hi 18, 21 aur 24 bhi harshad number hai kyunki 1 + 8 = 9 aur 18 ko 9 se divide kar ke remainder 0 hai. Aise hi 1, 2, 3, 4, 5, 6, 7, 8, 9 saare harshad number hain kyunki inki digits ka sum khud yeh number hain aur yeh apne aap se divide ho jate hain.

Ek number ke digits nikalne ka code yeh hai:

```python
x = 42
x_digits = list(str(x))
```

Yahan humne list function mein x ko string mein type cast kar ke de diya. Toh ab yeh har 42 ke alag alag number se list bana dega. `x_digits` mein ["4", "2"] list hogi. Iss list mein saare digits string ki form mein hogi, aap unko firse integer mein convert kar sakte ho


Ek function likho `is_harshad_number` jo ek number parameter ki tarah le aur fir agar woh number harshad number hai toh ek `boolean` (`True` agar harshad number hai, `False` agar nahi hai toh) return kare.

Fir iss function ka use kar ke 1 se 1000 ke beech mein saare harshad number print karo.