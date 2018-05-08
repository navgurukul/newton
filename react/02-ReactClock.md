```
name: Javascript Philosophy
completionMethod: peer_file_submission
```

React ek Javascript Library. Apne project mein React use karne ke liye aap pehle ki tarah CDN ke through React library add kar sakte hain.

React Library 2 files se bana hai- react.js aur react-dom.js
Inko apne javascript file mein include karne ke liye apne html file header mein inn tags ko add kar sakte hain.

```html
<script src="https://unpkg.com/react@15/dist/react.js"></script>
<script src="https://unpkg.com/react-dom@15/dist/react-dom.js"></script>
```
- Iss project mein hum in libraries ko use karke ek chota sa project - React Clock banayenge jo kuch [iss](https://codepen.io/Dafrok/full/OVdQWq/) tarah dikhega.

**Project Instructions**

1. Apne html page mein boilerplate code daaliye

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First React Project</title>
    <script src="https://unpkg.com/react@15/dist/react.js"></script>
    <script src="https://unpkg.com/react-dom@15/dist/react-dom.js"></script>
  </head>
  <body>
  </body>
  <script src="src/index.js"></script>
</html>
```

2. <body> tag ke andar ek div declare kijiye jiski id "react-container" ya "app-root" ya aur kuch rakh sakte hain. Hamara react code , iss div ke andar ke content ko manage karega.
```html
<body>
  <div id="react-container">
  </div>
</body>
```
3. React apps, React elements se banta hai. Ek react element banane ke liye .createElement() ka use hota hai. Niche code mein hum ek Header react element bana rahe hain.

```javascript
var firstElement = React.createElement('h1',{}, 'This is a react element');
```

Isme .createElement() ko 3 arguments paas hue hain:
* 1st argument: HTML tag jo hum create karna chahte hain
* 2nd argument: props; iske baare mein hum baad mein dekhenge
* 3rd argument: HTML tag ke children jo uske andar aayenge

4. Upar wale react element ko browser mein render karne ke liye hum ReactDOM.render() function ka use karte hai:
* 1st argument: HTML tag jo hum create karna chahte hain
* 2nd argument: props; iske baare mein hum baad mein dekhenge
* 3rd argument: HTML tag ke children jo uske andar aayenge

4. Upar wale react element ko browser mein render karne ke liye hum ReactDOM.render() function ka use karte hain.

```javascript
ReactDOM.render(
  firstElement,
  document.getElementById('react-container')
);
```
ReactDOM.render() 2 arguments leta hai:

* 1st argument -> React element jise hum render karna chahte hain
* 2nd argument -> div block jisme React element render hoga

5. Apne code ko run kijiye aur dev tools use kar ke  check kijiye ki browser mein kaun sa HTML tag run hua hai.

6. firstElement ke h1 mein "This is react element" ke bajay aaj ka Time display karaiye.
Yaad rahe ki agar quote ke andar koi javascript code run karna chahte hain toh [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) ka use hota hai.

```
`It runs this $(javascript expression)`
```
7. Aap dekhenge ki aapka clock har second pe update nahi ho raha hai. Kisi function ko agar periodically run karana hai toh hum kaun se function ka use karte hain?

React bhi javascript hai. Toh aap ab take likhe saare code ko kisi function mein dal kar use har second run karwa sakte hain. 

7. Apne React application ke css file mein styling karke aap usey stylish bana sakte hain. Chahe toh aap ek se jyada React element render kar sakte hain.

**Homework**
- Iss code mein ek aur React element <h2>Digital Clock</h2> render karwaiye
- Code run hone par Dev tools use karke DOM tree ko dekhiye. Kaun se elements update ho rahe hain. Kaun se nahi

