```ngMeta
name: DOM
```

# DOM

Humara HTML page ek Document Object hai. <html>, is Document object ka child hai. Isi tara <head> aur <body> , <html> ke children hai.

Pure HTML khandan ko hum iss [tree](https://www.w3schools.com/js/js_htmldom.asp) mein dekh sakte hai. Ise hum Document Object Model ya DOM kehte hain..

Javascript ka use karke aap DOM ke andar kisi bhi object ki property ya value modify/ change kar sakte hain.

Mann lijiye ki koi html page ka ye snippet hai:

```html
<div class="selectThis"> Change this text </div>
```

Hum iss div ke andar ke text ko change kar sakte hain.

```javascript
//modify karne se pehle, hume uss div ko select karna padega
var textToChange = document.querySelector('.selectThis');
```
Yahan par humne div ke *class* ko use karke apne desired element ko select kiya hai. Aap *class* ke bajay *id* ya kisi bhi aur [CSS selector](https://www.w3schools.com/cssref/css_selectors.asp) ka use kar sakte hain.

```javascript
//andar ke text ya innerHTML ko modify karne ke liye
textToChange.innerHTML = "This text has changed";

//text ke style mein fontSize change karne ke liye
textToChange.style.fontSize = "50px";
```

**Homework**

Is [codepen](https://codepen.io/rajeev-artha/pen/odwQrO) ko kholiye. Iske javascript mein code add kijiye taki buttons click hone par greybox mein text change ho aur bataye ki kaun sa button click hua hai.

