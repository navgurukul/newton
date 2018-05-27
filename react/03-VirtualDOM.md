```ngMeta
name: Virtual DOM
completionMethod: manual
```

# Virtual DOM

Aapne Javascript mein DOM ka concept padha tha. Agar aap bhool gaye hain toh dubara [yahan](https://www.w3schools.com/js/js_htmldom.asp) se padh sakte hain. Revision mein aapko 10-15 minute lagega.

Hum Javascript ko use karke DOM ko manipulate (yani change karte hain). DOM mein hum kuch elements ko add, ya remove ya aur kisi tarah ka manipulation karte hain.

Hum jitni bar DOM ko manipulate karte hain, utni baar DOM fir se re-draw hota hai. Iski wajah se DOM rendering (yani DOM jo aapko apne browser pe dikhta hai), wo kaafi slow hota hai. 

Iss problem ko solve karne ke liye React mein hum DOM ko directly manipulate karne ke bajay, ek DOM ki copy ko manipulate karte hain - isey hum **Virtual DOM** kehte hain. Virtual DOM ko hum jitni bar chahe change kar sakte hain - ye Real DOM se kaafi fast process hai.

Saari changes hone ke baad hum Virtual DOM aur Real DOM ke difference ko redraw kar ke render karte hain. **Virtual DOM** use karne ki wajah se React Applications jyada fast render karte hain.


Agar aap React mein use hone wale Virtual DOM ke baare mein aur padhna chahe toh [yahan](https://medium.com/@hidace/understanding-reacts-virtual-dom-vs-the-real-dom-68ae29039951) se padh sakte hain. Isko padhne ke liye aap 20-30 min spend kar sakte hain.

Agar aap React ka Virtual DOM use dekhna chahe toh, last clock wali exercise ko edit kijiye taaki aap ek ke bajay do elements ko render karein. Aise:

```javascript
function reactClock(){
	var firstElement = React.createElement('h1',{}, 'This is a react clock');
	var secondElement= React.createElement('h2',{}, '${new Date().toLocaleTimeString()}');
	var app = React.createElement('div',{}, firstElement, secondElement);

	ReactDOM.render(
  	app,
  	document.getElementById('react-container')
	);
}

setInterval(reactClock, 1000);
```

Upar code mein humne do elements h1 aur h2 create kiya, aur fir inn dono ko ek div element mein daal diya. Fir hum ise Virtual DOM mein render karte hain. Hum wapas se reactClock function ko har 1 second(1000ms) pe call karte hain.

Ideally, dono elements h1 aur h2 bar-bar har ek second pe DOM mein redraw ho kar render hone chahiye. Kya aisa hota hai??

Apne browser mein Dev tools khol kar dono elements ki rendering observe karo.

Aap dekhenge ki bas h2 element har ek second mein render hoga. Ye React ke virtual DOM ka kamal hai.


