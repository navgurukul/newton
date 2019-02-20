```ngMeta
name: Ek saath zyada saari cheezon ki tulna?
```

- Explain them the concept of and/or and then ask them to enter three different numbers using prompt. After this it returns maximum of those three numbers //Operators like less than, greater than and boolean operators 
//Operators like less than, greater than and boolean operators

var a = Number(prompt('Pehle number likho', '12'))
var b = Number(prompt('Dusra number likho', '34'))
var c = Number(prompt('Teesra number likho', '-10'))

if (a >= b && a >= c) {
        console.log('sabse badha number: ' + a)
} else if(b >= a && b >= c) {
        console.log('sabse badha number: ' + b)
} else if(c >= a && c >= b) {
        console.log('sabse badha number: ' + c)
} 