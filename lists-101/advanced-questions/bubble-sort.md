```ngMeta
submissionType: url
```

**Sorting** bahut hi important process hai jo aap ko programming mei baar baar encounter hoga. Sorting (Sort is the **root word**) ka matlab hai - kisi order mei arrange karna - jaise height se, weight se, marks se, naam se etc. 

Jaise:
- Kam marks se jyada marks (**Ascending Sort**)
- Alphabetically naam sort karna (**Chronological Ascending Sort**)
- Kam height se jyada height (**Ascending Sort**)
- Jyada weight se kam weight (**Descending Sort**)

Bubble sort ek sort karne ka tareeka hai, jo kuch numbers ko leta hai, aur unko **ascending** ya **descending** order mei sort kar deta hai.

### Understanding Bubble Sort

Iss diagram ko dekhiye. Aap bubble sort ke baarein mei [yahan](https://medium.com/karuna-sehgal/an-introduction-to-bubble-sort-d85273acfcd8) se bhi padh sakte ho.

![bubble sort](../assets/bubble.jpg)

1. 1st and 2nd element ko compare karo
   - Agar bada wala element baad mei hai, toh kuch mat karo
   - Agar bada wala element pehle hai, toh swap kar do
    (**swap** matlab - **interchange** - yaani pehle element ko doosre se, aur doosre ko pehle se replace kar do)
2. Aise hi ab 2nd aur 3rd elements ko compare and swap karo
3. Aise hi karte chalo, isse. 
   - Sabse bada wala element ek **iteration** ke baad sabse right mei pahuch jayega
4. Yeh iterations jitne numbers hai, utni baar karo - isse array sort ho jayega

Pehle aap yeh apni **notebook aur pen** use kar kar karo, isse aapki understanding improve hogi.

Phir yeh **algorithm** aap code kar kar implement karo. Yeh ek mushkil question hai, agar ismei aap ko 4-5 ghante bhi lagte hai toh bhi theek hai.