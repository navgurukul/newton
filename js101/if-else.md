```ngMeta
name: Kabhi aise toh kabhi waise? Yaani Kabhi if, Kabhi else
```

- Explain them the concept of if else and multiple if statments

- Tell them how we would like the user to tell which operation he wants to do. That would result in writing this code:

//Conditionals
var operation = prompt('Kaunse operation karna chahenge', 'a:addition/s:subtraction/d:division/m:multiplication')
var a = Number(prompt('Pehle number likho', '12'))
var b = Number(prompt('Dusra number likho', '34'))

if (operation == 'a') {
        console.log(a+b)
} else if (operation == 's') {
        console.log(a-b)
} else if (operation == 'd') {
        console.log(a/b)
} else if (operation == 'm') {
        console.log(a*b)
}

- Maybe take another example?