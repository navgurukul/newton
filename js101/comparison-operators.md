```ngMeta
name: Aur cheezon ki tulna kaise karein?
```

- Explain them the concept of comparison operators and then ask them to enter two different numbers using prompt. After this it returns maximum of those two numbers //Operators like less than, greater than

var a = Number(prompt('Pehle number likho', '12'))
var b = Number(prompt('Dusra number likho', '34'))

if (a > b) {
        console.log('sabse badha number: ' + a)
} else {
        console.log('sabse badha number: ' + b)
}