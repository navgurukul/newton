```ngMeta
name: Refactoring React Code
```

Abhi tak humara code aisa kuch hai:

**NutritionWizard/index.js**
```jsx
import React from "react";
import React-DOM from "react-dom";

class Header extends React.component {
  render(){
    return (
      <h2>This is the Application Header</h2>
    );
  }
}


class App extends React.component {
  render() {
    return (
      <div>
        <Header />
        <h2>{this.props.name}</h2>
      </div>
    );
  }
}

React-DOM.render(<App name="Nutrition Wizard" />, document.getElementById('react-app'));
```

Agar aapne apne web application ka pura UI design kiya hai (aur hum ummed karte hain ki aapne aisa kiya hoga), toh aapke paas bahut saare components honge aur **index.js** file unreadable bante jaa rahi hogi. 

Programming mein hum chahte hain ki:
1. humara code ki readability hamesha achi ho
2. hum existing code ko aise likhe taaki hum usey aaram se re-use kar sake

React mein har components re-usable hote hain. Hum inko alag-alag files mein bhi store kar sakte hain.

Aise:
Apne application folder "NutritionWizard" ke andar ek "components" naam ka folder banaiye. Iss folder mein hum saare components ko alag-alag file mein store karenge.

**NutritionWizard/components/Header.jsx**
```jsx
import React from 'react';

class Header extends React.component {
  render(){
    return (
      <h2>This is the Application Header</h2>
    );
  }
}

export default Header;
```

Iss file mein Header component stored hai.

**NutritionWizard/components/App.jsx**
```jsx
import React from 'react';
import Header from './components/Header.jsx'

class App extends React.component {
  render() {
    return (
      <div>
        <Header />
        <h2>{this.props.name}</h2>
      </div>
    );
  }
}

export default App;
```

Iss file mein App component stored hai. Aapne dekha ki humne App.jsx ke andar Header component ko import kiya hai taaki hum usey use kar sakte

Ab hum isi tarah index.js file mein inn components ko import karke use kar sakte hain.

**NutritionWizard/index.jsx**
```jsx
import React from 'react';
import React-DOM from 'react-dom';

import App from './components/App.jsx'

React-DOM.render(<App name="Nutrition Wizard">, document.getElementById("react-app"));
```

Ab humara code simple aur elegant lag raha hai. Iski functionality mein koi change nahi hua. Aisey code ko readable aur re-usable banane ke liye re-arrangement ko hum 'code re-factoring kehte hain'.

Hum periodically apne code ko **re-factor** karte rehenge.

**Assignment**

- Apne pure code ko re-factor kijiye taaki har components alag-alag file mein store ho. Uske baad unhe import karke apne index.jsx file mein use kijiye.

Code run kar ke dekhiye. Kya aapke code ke functionality mein koi change hui hai? 
