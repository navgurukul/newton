```ngMeta
name: Thinking about the Application
```


Humne React ke baare mein kaafi kuch seekh liya!! Phew!!

Abhi thora sa pause lete hain aur apne **Nutrition Wizard** application ke baare mein sochte hain.

Humara application kya karta hai?

1. User input mein apne Recipe ke **ingredients** likhega.

Aise:

```
2       eggs
1 tsp   butter
2 tbsp  water
1/8 tsp salt
```

2. User analyze button dabayega.

3. Analyze button dabane pe "ingredients ki list" humara application Nutrition API ko pass karega. Nutrition API hume iss tarah ka data (JSON format)mein send karega.

{
  fat: 137,
  protein: 220,
  carbs: 5
}

4. Humara Application upar ke data ko use karte hue, ek nutrition analyzer ka graphical representation karega.



Aapne [1] ke liye ek react component design kar liya hai jo user se input lete hain.

Aapne (shayad) ek react component design kar liya hai jo aapki nutrient data (dummy data) ko display kare. Agar aapne aisa nahi kiya hai toh aap javascript ki koi bhi graphic library use karke isey poora kar sakte hai. (example)

Humey iske aage 2 kaam karne hain:

1. Analyze button dabate hi hume Nutrition API ko request bhejna hai aur JSON data fetch karna hai jisme nutrition data ho.

2. Humey is data ko dynamically apne react component (jo nutrient data ka graphical display kar rahi hai) - usme display karwana hai.


**Assignment**

- Aap ek React Component banaiye <NutritionAnalyzer> jo **props** ke through nutrition data ko display kare (aap chart.js library use kar sakte hain)
- Aapne dekha ki kaise humne pure application ko chote-chote problem mein breakdown kiya hai. Complex problems ko chote aasan problems mein break karna ek skill hai. Ispe reflect karein aur apne thoughts peers se share karein.
