## /usr/bin folder
`/usr/bin` folder in linux isn't the `recycle bin` jo shayad aapne kabhi windows mei dekha hoga

`bin` ka yaha matlab `binary files` se hota hai. jo aapke programs hai, jo execute kiye ja sakte hai linux ke alawa, woh yaha par store hote hai.

```bash
cd /usr/bin
ls
```

Dekhiye kya aapko koi familiar names dikhayi de rahe hai?

Iss folder mei jo bhi `executable` files hongi, woh aap kahi se bhi sirf uss file ka naam likh kar execute kar sakte ho. Hum aage aisa ek program banayenge.

Aise hi

```bash
cd /bin
ls
```

ke contents ko samajh kar, observe kariye, ki kya contents hai, aur in mei se koi `commands/programs/executables` aapne kabhi use kiye hai kya?

Note:
Jo bhi file `executable` hogi, uss file ki permission mei aapko 'x' character dikhega `ls -l` karnei par.