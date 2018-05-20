```
name: JSX
completionMethod: manual
```

Agar humein React use karte hue 4 elements render karne hain, toh aap pehle ki tarah aise kar sakte hain:

```
var heading = React.createElement('h1', {}, 'Organization Credentials');
var name = React.createElement('h3', {}, 'Navgurukul');
var location = React.createElement('h3', {}, 'Bangalore');
var state = React.createElement('h3', {}, "Karnataka");
var app = React.createElement('div', {}, heading, name, location, state);

ReactDOM.render(
  app,
  document.getElementById('react-container')
);
```
Upar likha hua code bahut repetitive lag raha hai. Ye DRY principle follow nahi karta.

Isi code ko DRY principles follow karte hue likhne ke liye, React Developers **JSX language** ka use karte hain. Ghabraiye mat JSX koi nayi language nahi hai - ye bas HTML aur Javascript ka mixture hai.

Upar likhe hue code ko hum JSX mein kuch aise likhenge.

```jsx
ReactDOM.render(
  <div>
    <h1>Organization Credentials</h1>
    <h3>Navgurukul</h3>
    <h3>Bangalore</h3>
    <p><em>Karnataka</em></p>
  </div>,
  document.getElementById('react-container')
);
```

Haina aasan!!

Lekin aap agar ye code abhi run karenge toh, aapka browser ise render nahi kar payega -- kyonki Browsers JSX language nahi samajhte hain :(
Ab kya kare!!

Thankfully, aise libraries/tools hain jo realtime mein JSX ko Javascript mein convert karte hain, taaki humare browser ko samajh aa jaye.
Aise tools ko hum *Transpilers* kehte hain. Ek Aisa transpiler jise hum abhi use karenge - Babel


Babel Transpiler ko use karne ke liye, apne HTML document mein ye script tag add karein:

```
<script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
```

Ab apne application ko run karke dekhe.

**Assignment**

- Apne ReactClock Application ko JSX use karke banaiye. 
