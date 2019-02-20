```ngMeta
name: Baar baar ek hi code kaise run karen?
```

- Introduce the concept of loops.

- A while loop to take in user input 10 times before it stops.

// while loop
while(true) {
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
        } else {
                break; // introduce concepts of break and continue
        }
}