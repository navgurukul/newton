```ngMeta
name: Decision Making
completionMethod: manual
```

Aapne computers ko __instructions__ de kar, unhe __variables__ mein store hone wale values ko print karna seekha.
Aapne **int** data type pe arithmetic operations (+,-,\*,/,% etc) bhi seekha.

Abhi tak aapne computers ko jo jaise kaha, waise hi usne kiya.
Ab hum dekhenge ki hum computers ko kaise khud se hi decisions lene ko keh sakte hain.

Computers ko decision lena seekhane se pehle, hum dekhenge ki hum real life mein decisions kaise lete hain.

Example:
 Aapki mummy ne aako 50 rupye diye aur kaha - "beta, gas stove ke liye lighter le aa. Agar lighter 50 rupye se mehga hai toh machis le aa"
 Ye aapke mummy ka aapke liye instructions hai.
 
 Isko thora sa programming jargon mein likhne ki kosish karte hain.
 *Note*: Niche likha hua program ek asli program nahi hai - Yaani isey hum computer pe *compile* nahi kar sakte. Lekin ye program jaisa hi deekhta hai - isey hum pseudo-program kehte hain.

 
```
//Aapki mummy ne aapko 50 rupye diye

money = 50;

//Aap check karenge ki lighter ka price 50 se jyada hai ya nahi
//agar ligher ka cost 50 se kam hai, toh aap lighter khareedenge

Agar LighterCost < 50
    Buy a Lighter;

//Nahi toh aap machis khareedenge
Nahi Toh
    Buy Matches;
```

LighterCost < 50 ek **Condition** hai jisey aap check karte hain. __Agar__ wo sahi hota hai toh aap *kuch* karte hain, __Nahi toh__ , *kuch aur* karte hain.
Iss tarah **conditions** ke help se hum decisions lete hain.

Java mein hum Agar...nahi toh ki jagah par **if/else** ka use karte hain. **If** condition sahi hai, toh hum computer ko *kuch* karne ko kehte hain, else unhe hum *kuch aur* karne ko kehte hain.

Java mein **if/else** ke use se computers ko decisions lene ke baare mein aur janne ke liye - [yahan](https://www.codecademy.com/courses/learn-java/lessons/conditionals-control-flow/exercises/decisions?action=resume_content_item) se kuch tutorials complete karein. Iss link mein 11 tutorials hain jinhe complete karke aapke computers decision lena seekh jaayenge.

**Assignment**
- 2 persons ke name, age, gender aur profession store karo. 
	- Agar unke age 40 se jyada hai, toh unke profession mein "retired" value daal do. Dono ke professions ko print karo. Aapko iske liye if-else ka use karna hai.
	- Agar dono ka gender male hai, toh dono ke gender ko female kar do - nahi toh kuch mat karo. Unke genders print karo.
- Dono persons ke alag-alag age aur gender daal kar, apne program ko check karo.
