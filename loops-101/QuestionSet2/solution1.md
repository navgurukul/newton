```ngMeta
name: Solution 1
```

# Solution 1
Yeh pattern print karo.

```
#
##
###
####
#####
######
#######
```

## Question

## Solution

Iss question ke saath solution di hui hai. Yeh aapko samjhane ke liye hai ki hum iss type ke questions kaise solve kar sakte ho. Better yeh hoga ki aap solution na dekho aur pehle khud solve karne ki try karo.

Solution se pehle ek chota sa concept samajhte hain. Jaise agar hum `4*3` karte hain toh hum 2 integers ko multiply kar rahe hain aur humara result `12` aayega. Aise hi agar hum ek string aur integer ko different behaviour hoga. Jaise

```
>>> 'navgurukul' * 3
'navgurukulnavgurukulnavgurukul'
```

Dekho kaise `"navgurukul"*3` karke `navgurukul` 3 baar aa gaya. Aise hi `'hello'*5` `hello` 5 baar ayega. Jaise:

```
>>> 'hello' * 5
'hellohellohellohellohello'
```

Yeh program likhne se pehle upar wale pattern mein kuch cheezein dekhte hain.

1. Pehli, iss pattern mein total `7` lines hain.
2. Pehli line mein ek `#` hai, dusri line mein 2 `#` hain, teesri line mein 3 `#` hain.
3. Matlab number of `#` bhi line number ke saath badte jaa rahe hain.

Iska solution kuch aisa hoga.

```
i = 1 # counter 1 se shuru karo
while i <= 7: # kyunki humare program mein 7 lines hain isliye loop tab hi band karna hai jab woh 7 baar chal jaye. Har baar line print karne pe loop chalega.
  print('#'*i)
  i = i + 1
```
