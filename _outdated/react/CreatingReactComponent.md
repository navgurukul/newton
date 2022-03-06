```ngMeta
name: Creating A React Component
```

Aapne pichle lessons mein dekha ki kaise React Applications, **Components** se bane hote hain.
Hum iss lesson mein apne Nutrition Wizard Application ka  pehla react component banayenge - Uska Header jisme humare application ka naam likha ho.

.....

React Component banane se pehle, hume Javascript mein **classes** ki understanding jaroori hai.

Classes ke baare mein samajhne ke liye [iss link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) ko padhe aur usme diye hue examples ko dekhe.

[//]: # (This section may need better curation or further breakdown)

Link padhne ke baad aapko *class ka matlab*, *class create karna* aur *ek class ko **extend** karke doosra class banana aana chahiye*
.....

Hum ek <Header> naam ka React Component banayenge. Iske liye hum ek **Header** class banayenge jo React Library ke *React.component* class ko extend karta hai.

**NutritionWizard/index.js**
```javascript
class Header extends React.component {
  
}
```

Iss class ko <Header> ke andar aane waale HTML code ko return karna hai. Iske liye hum **Header** class ke andar ek **render** function define karte hain jo ye HTML ko return kare.


**NutritionWizard/index.jsx**
```jsx
class Header extends React.component {
  render() {
    return (
      <h2>Nutrition Wizard</h2>
    );
  }
}
```

Aapne dekha hoga ki hum iss code mein Javascript aur HTML dono ka use kar rahe hain. Isey hum JSX language kehte hain. Isse hume program likhne mein aasani hoti hai. Babel Library (jo humne pehle hi install kiya tha, iss JSX code ko Javascript mein convert kar degi :))
Humne file ka naam bhi **index.js** se **index.jsx** rakh diya hai.

[//]: # (I think I forgot to ask them to import Babel Library into their project previously)

Ab iss component ko render karne ke liye hum React-DOM mein pre-defined function **ReactDOM.render()** ka use karenge.
ReactDOM.render() function humare React Component ko kisi bhi HTML parent element me write kar sakta hai.

**NutritionWizard/index.html**
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>React Project</title>
</head>
<body>
  <div id="react-app"></div>
</body>
</html>
```

**NutritionWizard/index.jsx**
```jsx
class Header extends React.component {
  render() {
    return (
      <h2>Nutrition Wizard</h2>
    );
  }
}

ReactDOM.render(<Header />, document.getElementById('react-app'));
```

Iss application mein humne ek React Component <Header> create kiya hai.

Note: 
1. render() function bas ek *parent* HTML element ko hi return kar sakta. Iss parent ke aur bhi children ho sakte hain. Magar hum ek se jyada parent return nahi kar sakte.

Jaise:
```jsx
class Header extends React.component {
  render() {
    return (
      <div>
      	<h2>Nutrition Wizard</h2>
        <h4>Designed by NG Team</h4>
      </div>
    );
  }
}

ReactDOM.render(<Header />, document.getElementById('react-app'));
```

Upar likha hua program sahi hai, kyonki isme bas ek parent <div> return ho rahi hai.

Lekin

```jsx
class Header extends React.component {
  render() {
    return (
        <h2>Nutrition Wizard</h2>
        <h4>Designed by NG Team</h4>
    );
  }
}

ReactDOM.render(<Header />, document.getElementById('react-app'));

```

Upar likha hue program mein error hai kyonki yahan pe 2 parent elements h2 aur h4 return ho rahe hain.

2. JSX mein har HTML tag close hona chahiye. Jis elements mein bas ek hi tag use hote hain, uspe hum self closing tag use karte hain.

Jaise <br />, <img src="navgurukul.png" /> etc.

JSX ke baare mein aur janne ke liye aap [ye resource](https://learn.co/lessons/react-jsx) use kar sakte hain.
.....

**Assignment**

- Humne apne *Header* component mein bas ek h2 tag use karke App ka naam likha hai. Aap HTML elements use karke apne application ka ek complete header React component mein likhe.

Yaad rahi humara return statement ek se jyada parent HTML elements ko return nahi kar sakta. 
