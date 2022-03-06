```ngMeta
name: Git Working Directory
```
Git humare working directory ke files mein kiye hue changes ko track karta hai. 

Lekin...

abhi git koi bhi files track nahi kar raha hai. Hume git ko batana hoga ki usey kaun si files track karni hai.


Terminal khol kar apne **stories** directory mein navigate kijiye

```
$ cd Stories

```

**ls** command use karke aap apne directory ke saare files ko dekh sakte hain.
Iss directory mein "git status" command run kijiye.

```
$ git status
```

"git status" command use karke aap apne directory ke saare *tracked* aur *untracked files* ko dekh sakte hain.

Directory ke kisi bhi file ko track karne ke liye

```
git add <filename>
```
 ka use kar sakte hain.

"git add \*" directory ke saare files ko track kar sakte hain.


**Assignment**
- Apne Story ki file ko "git add" use karke git ke through track hone dijiye.
- "git add" ka documentation padhiye aur uska use samajhiye
https://git-scm.com/docs/git-add

- "git add" use karke hum untracked files ko track karte hain. 
Tracked files ko wapas se untracked banane ke liye git kya use karta hoga. Pehle Sochiye!!
Fir git ka [documentation](https://git-scm.com/doc) khol kar pata lagane ki koiis kijiye.

