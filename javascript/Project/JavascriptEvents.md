```ngMeta
name: Javascript Events
```

# Javascript Events

Aapne pehle dekha ki aapa webpage user ke mouse pointer move karne se snowfall ka direction change kar raha tha.
Mouse pointer move hona ek user event hai.

User webpage pe bahut sare events produce kar sakta hai, jaise:
* click (jab user kahin click karta hai)
* keypress 
* scroll 

Poori list aapko [yahan](https://developer.mozilla.org/en-US/docs/Web/Events) mil jayegi.

Aapka webpage bhi inn user events ko sunn sakta hai aur kuch action le sakta hai. Agar aap apne webpage ke *window* mein *click* event sunna chahte hain toh apne javscript mein:

```javascript
window.addEventListener("click", function(){
  //define your function here
});
```

Yeh code "click" event ko listen karta hai aur "click" hone par, function ke andar jo bhi instructions hain use execute kar deta hai.
*Note*: ""window" javascript mein ek pre-defined Object hai. Aur "addEventListener" ek pre-defined method hai. Hum iske baare mein aage aur padhenge.

**Homework**
1. Pichle example project (creating snowfall) mein, ek click listener add karo. User ke click karne se snowfall ka color change kar do.
2. "click" ke alawa doosre events ke saath experiment kijiye jaise "keypress", "resize" etc.
...
