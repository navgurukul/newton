```ngMeta
name: Palindrome or not?

```

Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai. Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai. Aise hi MOM bhi ek palindrome hai.

Code likho jo check kare ki kya list palindrome hai ya nahi. Aur print karo “Haan! palindrome hai” agar hai. Aur “nahi! Palindrome nahi hai” agar nahi hai.

Abhi ke liye iss list ko use kar ke code likh sakte ho:

```python
name=[ 'n', 'i', 't', 'i', 'n' ]
```

Apni list ko change kar ke alag alag values ke saath test out karo aur fir finally theek code ko upload karo.

Inn values ke liye aap test kar sakte hai

nayan => true
naina => false
anamana => true
ainaania => true
ainabnia => false

## Hints
Jab `index i` hai, tab `length - i -1` index par kya hoga.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]

| i     | places[i] | length - i| places[length - i] |
|-------|:---------:|:---------:|-------------------:|
|0      | "delhi"   |4          | "kerala"           |   
|1      | "gujrat"  |3          | "punjab"           |   
|2      |"rajasthan"|2          | "rajasthan"        |   
|3      | "punjab"  |1          | "gujrat"           |   
|4      | "kerala"  |0          | "delhi"            |