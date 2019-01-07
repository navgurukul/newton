```ngMeta
name: States
```

Aapne <NutritionAnalyzer> naam ka component banaya hoga jo aapke nutrient display hone ka UI represent karti hai.

Aapne props use karke kuch iss tarah <NutritionAnalyzer> ko display karayahoga :

```jsx
import React from 'react';
import React-DOM from 'react-dom';

import App from '.components/App.jsx';

React-DOM.render(<App fat="137", protein="207", fat="6"/>, getElementById('react-root'));
```

**Note**: Yahan pe <NutritionAnalyzer> React component <App> component ke andar use ho raha hai. Aapka code upar likhe hue code se different dikh sakta hai.

Upar mein humne **props** karke <NutritionAnalyzer> component ko data transfer kiya. Ye tab tak sahi hai jab tak humara component change nahi hota hai. 

Lekin humare applications mein toh ye <NutrtitionAnalyzer> component hamesha (har user input ke baad) change hote rahega (dynamic rahega).

*Note* : React, Javascript ka hi part hai. Lekin React mein hum Javascript ki tarah DOM manipulate nahi karte hain!!

Apne <NutritionAnalyzer> component ko hum **states** de sakte hain. **States** change hote hi React component khud hi update ho jaata hai. React mein components ka *state* hona bahut khaas baat hai.

React component mein state add karne ke liye:

```jsx
import React from 'react';
import React-DOM from 'react-dom';

class NutritionAnalyzer extends React.component {

  constructor(props) {
    super(props);
    this.state = {
      fat: "137",
      protein: "207",
      carbs: "6"
    };
  }

  
  render() {
    return(
      <div>
        <h3>Fat : {this.state.fat}</h3>
        <h3>Protein: {this.state.protein}</h3>
        <h3>Carbs: {this.state.carbs}</h3>
      </div>
    );
  }

}

export default NutritionAnalyzer;
```

Upar mein humne **constructor()** function ke andar apne React component ko *state* assign kiya hai. **"this"** yahan par apne react component (yahan pe NutritionAnalyzer) ko hi refer karta hai. Kisi bhi component ko initial values dene ke liye hum constructor ka use karte hain.

upar mein:

**this.state.fat** mein "137" stored hai. Humne usey code mein {} ke andar use bhi kiya hai.

Aise hi aap kisi bhi react components ke kitne bhi __states__ define kar sakte ho aur unhe use kar sakte ho. 

Yahan par **state** ki fixed value hai jo humne constructor ke through assign ki hai. Lekin hum __this.setState()__ function use karke hum states ki value ko change bhi kar sakte hain.


**Assignment**

- this.setState() ke usage examples online dekhiye.
- Apne NutritionAnalyzer React Component mein ek updateAnalyzer() function likhiye. Ye function this.setState() ka use karke humare component ke state ko kisi doosra value deta hai.

**Note:** Baad mein hum iss updateAnalyzer() function ko har bar user ke "Analyze" button dabate hi call karenge. updateAnalyzer() function ke andar hi API call hogi jisse hume apne React component ke naye states milenge. Isi state ko hum this.setState() use karke apne react component ka state change kar denge.
