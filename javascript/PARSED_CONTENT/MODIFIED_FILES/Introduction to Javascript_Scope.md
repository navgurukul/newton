Scope_key1
Scope_key2


Scope_key3


Scope_key4


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

Scope_key5



Scope_key6[Scope_key7](https://www.w3schools.com/js/js_scope.asp)
Scope_key8

Scope_key9
- Scope_key10
- Scope_key11
```javascript
function f1(){
  var a = 1;
  return f2();
}

function f2(){
  return a;
}
```
- Scope_key12
