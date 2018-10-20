```ngMeta
name: Day-1-Task-3
completionMethod: manual
```

### Reading Material
**Armstrong** Number
Ek number **Armstrong** Number tab khelata hai jab uske har ek digit khudse 3 bar guna karke agar
hum add kare toh hume wapas wahi number mil jata hai.

Jese 153 **Armstrong** Number hai.
Kyunki 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 153 hi ahta hai.


### Question
Apko ish sawal me ek program likhna hai jishme ek value di jayegi manlo `1000` toh apko jitne bi number **Armstrong** Number hai `0` se `1000` ke bich me ushe *print* karna ha.

```
Eg:
  Input: 1000
  Output:
      1
    153
    370
    371
    407

```

### Test
#### Apne program ko test karne ke liye ish input ko dale ke uske output check kare

```
Test Case 1:
  Input: 120
  Output:
      1
```

```
Test Case 2:
  Input: 1000
  Output:
      1
    153
    370
    371
    407
```

```
Test Case 3:
  Input: 300
  Output:
      1
    153
```

```
Test Case 4:
  Input: 400
  Output:
      1
    153
    370
    371  
```

### Hint

No Hints

**2<sup>3</sup>** ko app python meh `2**3` likh sakte ho aur

Digit app ese nikal sakte hai
**123%10 = 3** dega
**12%10 = 2** dega
**1%10 = 1** dega
