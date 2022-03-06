```ngMeta
name: ReactIntro
```

Iss video ko dekhiye: https://youtu.be/Pc6Bm4Xgkj8

Aapne abhi tak Web Development mein - HTML, CSS aur Javascript seekha hai. Saath mein aapne Javascript ki Libraries use karna aur API calls karna bhi seekha hai.

Yaani - Aapne Web Development mein bahut kuch seekh liya hai!!

Mein aapke abhi tak ke learnings ko summarize karne ki kosis karoon toh:

1. Apne dekha ki website/webapp mein jo **content** hota hai, hum use display aur organize karne ke liye pre-defined **HTML elements** ka use karte hain (jaise <h2>,<div> etc.)

2. Har web application ka **style**/design component hota hai - usey hum **CSS** ke through design karte hain (jaise background color, font size etc.)

3. Har application mein hum kuch **user interaction** build karte hain. Aise user interactions build karne ke liye hum Javascript ke through DOM ko manipulate karte hain - jaise "click" karte hi browser mein kuch magically appear ho jana, ya "p" press karte hi kisi HTML element ka move karna etc
.

4. Javascript ke aise functions use karne ke liye jo kisi aur ne likhe hain lekin general use mein aa sakte hain, hum **Javascript libraries** ka use karte hain.

5. Kisi **API service** ko use karke external sources se data collect karne ke liye hum **API calls** karte hain.

Iss [web application](https://www.edamam.com/website/wizard.jsp?ver=wizard-basic) ko dekhiye aur aapne abhi tak jo bhi padha usme fit karne ki kosis kijiyei. 
Ye ek "Nutrition Wizard Application" hai - isme apne recipe ki ingredients daalne par ye us recipe me nutrition component batata hai.
 
Yahan pe HTML, CSS aur Javascript ka use kaise ho raha hai?
Iss web application ko build kaise karenge iske baare mein sochiye.
.....

Ye bahut simple application hai aur isme bahut limited user interaction hai. Lekin agar iski complexity jyada ho, toh hume bar-bar DOM ko manipulate karna hoga ....dheere dheere humare program ki complexity bhi badh jayegi. Baar baar DOM manipulation se humare web app ki speed bhi slow ho jati hai.

Kaash hum ek web application bas aise bana sakte:

```HTML
<App>
 
 <NavBar>
   Nutrition React App
 </Navbar>

 <UserInput>
  
   <RecipeTitleBox> 
     Enter the recipe title 
   </RecipeTitleBox>

   <RecipeIngredientList>
    Type or paste your recipe ingreditents here
   </RecipeIngredientList>

   <Servings>
     Input number
   </Servings>

   <AnalyzeButton>
     Analyze
   </AnalyzeButton>

 </UserInput>

</App>
```

Kaash humare paas HTML ke aise *components* hote jo hum define kar sakte aur un **components** ko pata hota ki unhe kya karna hai. Fir hum un elements ko kahin aur bhi use kar sakte hain.


Aise mein web development kitna aasan hota!!!
Bade complex applications ko bhi organize karna aasan hota!!
....

**React** ek Javascript ki Library hai jo kuch aisa hi karne ki kosish karti hai.

Iss React course mein hum React use karte hue aisa hi ek **Nutrition Wizard** banayenge aur iske through React ke baare mein aur janenge :)

**Assignment**

- Koi bhi 2 websites lijiye. Unko upar diye hue example ki tarah *components* mein break kijiye. Aap upar ki tarah apne app ke liye ek HTML pseudo-code bhi likh sakte hain.
Dhyan rahe ki har *Component* aisa ho jiski bas ek functionality ho.

- Apne HTML pseudo-code ko apne peers ko dikhaiye. Kya wo unhe samajh paa rahe hain? Unse iss baare mein feedback lijiye.
