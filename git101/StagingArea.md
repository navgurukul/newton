```ngMeta
name: Staging Area and difference
```

Apne file ko **git add** karte hi aapki file ki ek copy staging area mein ban jaati hai.

Aap abhi bhi Working directory mein apne file mein changes kar sakte hain. Apne txt file jisme aapne story ki beginning likhi hai -usme kuch edits kijye - maybe characters ke naam change kijiye.

Terminal mein apne directory mein navigate karke:

```
git diff <filename>
```

ye command run kijiye.

Output mein aap apne naye file aur purane file mein difference yani kya kya changes hue hai wo dekh payenge.

**Assignment**

- Git ke documentation mein **git diff** ke baare mein padhiye.

- Usi directory mein koi doosra file create kijiye. 
  Fir usey staging area mein add kijiye. 
  git command se apne directory ke *tracked* aur *untracked* files ka status dekhiye. 
  Iss file mein kuch changes kar ke **git diff** command run kijiye.
  Wapas se git status run karke output dekhiye.
  Apne working directory ke edited file ko wapas se Staging area mein add kijiye. "git diff" command run karke wapas se staging area aur working directory ke files ke beech ka difference dekhiye. Ideally abhi koi difference nahi hona chahiye.
