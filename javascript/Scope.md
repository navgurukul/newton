```ngMeta
name: Scope
```

# Scope

Variables ko logon ki tarah imagine kijiye - log jinke dimaag me kuch memory hai - aur wo iss memory mein kuch values store karte hain.
Ek program ko ek country ki tarah imagine kijiye jahan ye variables rehte hain.

Iss program ki duniya mein variables bahut strangely behave karte hain. Kuch variables (global variables) ki memory program ke har hisse mein kaam karti hai aur usme stored values ko hum kahin bhi access kar sakte hain. Leki kuch variables (local variables) program ke ek hisse se bahar nikalte hi apni yaddast (memory) kho dete hain aur usme stored values ko hum use nahi kar sakte.

Example: 

```javascript
var iAmGlobal = "You can access me anywhere:";
function (){
  var iAmLocal = "I lose my memory outside this function";
}

console.log(iAmGlobal);
//expected string output
console.log(iAmGlobal);
//expected undefined output
```

*iAmGlobal* ek Global Variable hai aur use kahin bhi use kar sakte hain.
*iAmLocal* ko aap bas function() ke andar hi use kar sakte hai. Uske bahar wo undefined hai.


Global aur local variables ke baare mein aur janne ke liye aap [yahan](https://www.w3schools.com/js/js_scope.asp) padh sakte hain.

**Homework**
- Apne pichle programs mein jo aapne variables use kiye hain, unki scope identify kijiye.

- Niche diye hue program ko run kijiye aur usme error identify kijiye
```javascript
function f1(){
  var a = 1;
  return f2();
}

function f2(){
  return a;
}
```
- Upar likhe hue program ka correct form kya hoga?
