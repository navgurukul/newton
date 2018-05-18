```ngMeta
name: Javascript Philosophy
completionMethod: peer_file_submission
```
# Looping

Jab hum ek set of instructions bar-bar run karna chahe toh hum aise kar sakte hain:

```javascript
alert("Hi, I am 1");
alert("Hi, I am 2");
alert("Hi, I am 3");
alert("Hi, I am 4");
alert("Hi, I am 5");
```

Programming ka ek basic convention hai DON'T REPEAT YOURSELF (DRY)
Upar likha hua program DRY follow nahi karta. Dekhne mein bhi ye bahut sundar nahi lagta hai.

Isi ko hum javascript mein *loop* ka use karke likh sakte hain.

Aise:

```javascript
for (var index=1; index<=5; index +=1){
	alert("Hi, I am " + index);
}
```

Upar likhe code ka wahi output hoga jo humne pehle dekha tha. Upar likha hua code apne aap ko repeat bhi nahi karta yani DRY hai.

Loops ke baare mein aur jaane ke liye [yahan](https://www.w3schools.com/js/js_loop_for.asp) padhe.

Humne yahan pe *for* loop ka use kiya hai. Javascript mein loops use karne ke aur bhi tareeke hote hain.

**Self-practice**

- 4 alag-alag program likhe jo ek hi kaam ko *for* loop, *while* loop, *for-in loop* aur *do-while* loop se kare. In saare programs ka output same hona chahiye.



