```ngMeta
name: Day-1-Task-2-3
completionMethod: manual
```

### Reading Material
**Leap Year** har 4 saal me ek baar ahta hai aur woh bi ush saal me joh `4 se divisible hota hai`. Lekin saat hi agar woh saal `100 se divisible hai` magar `400 se divisible nhi hai`.
Toh woh **Leap Year** nhi kehlata hai.

Eg:
  1800 **Leap Year** nhi hai kyunki yeh `100 se divisible hai` magar `400 se divisible nhi hai`
  2000 **Leap Year** hai kyunki yeh `100 se divisible hai` aur `400 se divisible hai`

### Question
Apko ish Task me input ke torh pe saal diya jayega aur apko ush saal ke 3 pichle **Leap Year** print karne hai.

Aur Jab 3 pichle **Leap Year** nikal jaye toh uske baad aap 3 ane wale **Leap Year** nikalne hai apko.


```
Eg:
  Apko ek saal di jayegi jese 1998.
  Toh apko ush saal ke piche aye hue 3 leap year nikalne hai 1996, 1992, 1988
  aur Jab nikal jaye toh apko aage ane wale 3 leap year nikalne hai 2000, 2004, 2008
```

### Test
#### Apne program ko test karne ke liye ish input ko dale ke uske output check kare

```
Test Case 1:
  Input: 1000
  Output:
    Pichle 3 Leap Year : 996 992 988
    Agle 3 Leap Year : 1004 1008 1012
```

```
Test Case 2:
  Input: 1460
  Output:
    Pichle 3 Leap Year : 1456 1452 1448
    Agle 3 Leap Year : 1464 1468 1472
```

```
Test Case 3:
  Input: 1570
  Output:
    Pichle 3 Leap Year : 1568 1564 1560
    Agle 3 Leap Year : 1572 1576 1580
```

```
Test Case 1:
  Input: 2000
  Output:
    Pichle 3 Leap Year : 1996 1992 1988
    Agle 3 Leap Year : 2004 2008 2012
```

### Hint  
Aap 3 leap year (aage yeah pichle wale) aye usko pata karne k liye ek alag varibale rakh sakte ho.Joh apki madad karega yeh jane meh 3 leap year nikal gaye ya nhi.
