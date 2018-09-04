```ngMeta
name: Bloody Nasreen-Part I
completionMethod: facilitator
```
# Part I

- [link](http://codepen.io/navgurukul/full/PWbvPb/)

- **Bloody Nasreen** ki image use karne ke liye ye [link](http://navgurukul.org/bloodynasreen/front.png) copy kare.

- Background image ke liye ye [link](http://navgurukul.org/bloodynasreen/explosion.jpg) use kare.

- Aapko body ki **background image** kaise lagate hain wo yaad hoga. Agar nhi yaad to w3schools par search kare.

- Ab hum bloody nasreen ko apne page mein layenge.
	- Ek **<img>** tag body mein use kare aur uska **src =** "[link](http://navgurukul.org/bloodynasreen/front.png)"  set kar de.

	- Page ko reload kare aur dekhe. Bloody nasreen **top left me corner** aa jaegi. 

	- bloody nasreen ki hum ab **position** property set karenge.

	- Position property kaise kaam karti hai uske liye next slide padhe.

	- bloody nasreen ko page mein kaha position karna hai wo hum **top,bottom,left aur right** attribute 
	se set kar sakte hai.

# Position  continued

- Position property chaar values le sakti hai : **static**, **relative**, **absolute** aur **fixed**.

- By default yaani ki pehle se har element ki position **static** hoti hai.

	- Position static hone ka matlab yeh hai ki elements jasie normally page par load hote hai wasie honge.

- Position **relative** set karne se hum element ke **top**, **left**, **right** aur **bottom** attribute set kar sakte hai.

	- Inn attributes ki value change kar kar hum apne element ko unki normal position se move kar sakte hai.

	- Position relative karne se aap **z-index** property ki value bhi set kar sakte hai. Z-index ke bare mein aur jaanne ke liye google ka use kare.

- Position **absolute** set karne par aapka element apni normal position par load nhi hota. Aur uski position hum **top**, **left**,  **bottom** aur **right** se set kar sakte hai

- Position **fixed** ke bare mein aapne sticky headers mein padha hoga.

# OnLoad

- Ab hum **onLoad**event par bloody nasreen ko upar di gayi chaar properties ka use 
karke hilayenge.

	- Aap dekhenge ki bloody nasreen aapne jo position set kari thi uss par phonch gayi.

	- Aur jahan wo shuruwat mein thi waha ab nhi hai. Socho aisa kyun ho raha hai ? 

	- Aur apne instructor ko slack par bataye.

- Kabhi kabhar slow internet connection ke kaaran aapke page ki javascript, html se 
pehle load ho jata hai.

- Aisa hone par javascript ke functions Html ke elements ko use nahi kar paate.

- Isliye hum javascript events ko html load hone ke baad call karte hai.