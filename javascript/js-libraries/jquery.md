```ngMeta
name: Jquery
completionMethod: facilitator
```

# Part I  fun with jquery

- Jquery ek javascript ki library hai, jiss ki help se hum javascript ka code easily aur kam lines mein likh sakte hai.

- Jquery ko apne page mein use karne ke liye page ke head tag mein ye likhe:

- [https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js](https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js)

- Hum jquery ka code likhne ke liye "$" symbol ka use karte hai. Generally, code aise likha jata hai,
	 _$("css_selector").property_ka_naam(uske_inputs);_

- Jaise:

- JavaScript mein,

_var body=document.getElementById("#page");_

_body.style.backgroundColor="blue";_

- Magar Jquery mein,

_$(‘#page’).css({ "backgroundColor":"blue" });_


# Bloody Nasreen with Jquery

- Ab hum bloody nasreen ke project ki  "**teen**" assignments ko jQuery se karenge.

- jQuery mein on **load event** ke baare mein padhne ke liye yeh [link](http://www.jquery-tutorial.net/introduction/the-ready-event/) use kare.

- Hum jQuery mein **animate**() ka use kar kar animation kar sakte hai. Jaise,

	- **$("#page").animate( { "left","100px" }, 1000);**	// iske bare mein padhne ke liye yeh [link](http://www.jquery-tutorial.net/introduction/the-ready-event/) use kare.

- JS mein hum  **addEventListener** use karte the. Magar jQuery mein hum bind ka use karte hai. Events kaise bind karte 	hai 	uske liye yeh [link](http://www.jquery-tutorial.net/events/introduction/) use kare.
- **$("#page").attr("src","xyz.png");** 	_// aise hum ek attribute ki value change karte hai._

- **$("#page").css("property_ka_naam")**	_// aise humein ek property ki value milti hai._
- Neeche nayi assignments ke link hai,
	- [Link1](http://codepen.io/navgurukul/full/ggGWyJ/)
	- [Link2](http://codepen.io/navgurukul/full/vgeZxq/)
	- [Link3](http://codepen.io/navgurukul/full/ZLXJWm/)