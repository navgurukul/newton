```ngMeta
name: Calculator-Part II
completionMethod: peer
```

# Part II

- [Link](http://codepen.io/navgurukul/full/wgMBRR) ~ Ab hum sabse pehle **onclick** functions daalenge. onClick function mei hum display jo bhi user ne button press kiya hai, aa jayega. Functions ke naam ache se likhna. Similar tareeke wale functions ko ek saath likh sakte ho - jaise kisi bhi number par click karne

par **onNumClick** function bana sakte ho aur usme number ko
 
**argument** ki tarah paas kar sakte ho.  Functions ke liye yeh naam use karo:


- AC par **onACClick** - click karne se display par 0 aana chahiye

CE par **onCEClick** - click karne se display par 0 aana chahiye

Kisi bhi number par **onNumClick**(number). Ek hi function mei sab number handle karne hai. Iske liye
**onNumClick ek** number naam ki value ko **parameter** accept karega.
Aise hi kisi bhi operator par applyOperator(operator) function. 
Operator ki value x, +, -, /, = ho sakti hai. Operator ki value jaha par calculator mei **x** likha hai, waha par hogi.
- . par **onDecimalAdded** function call karna hai
