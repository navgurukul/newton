```ngMeta
name: Running JS code inside JSX
```

Aapne abhi tak JSX mein dekha ki:

1. Hum classes, functions etc. ka use apne code mein karte hain jo bilkul Javascript ki tarah hai.
Jaise humne render() **function** ka use kiya YA App **class** ko define kiya.

Actually, hum JSX mein Javascript ke baaki concepts ko bhi implement kar sakte hain - jaise variables, if-else, while, JS events etc.

Example:
```jsx
class Header extends React.component {
  render() {
    
    const isLoggedIn = true;
    
    if (isLoogedIn) {
      return (
        <div>
          <h2>Nutrition Wizard</h2>
          <h4>Designed by NG Team</h4>
        </div>
      );
    }
    
    else {
      return (
        <h2>Please Login first</h2>
      );
    }
  }
}
```

Upar mein maine ek **isLoggedIn** naam ka variable banaya hai jiski value true hai. *true* ya *false* condition par ye code alag-alag HTML block return karta hai.


2. Hum JSX mein HTML elements aur React Components ko *return* karte hain. Return statment mein hum HTML type ka code likhte hain.

Agar iss HTML code ke andar aap Javascript ka koi code run karna chaho tohaap {} ke andar apna JS code likh sakte ho.

Example:

```jsx
class Header extends React.component {
  render() {
    return (
      <div>
        <h2>Nutrition Wizard</h2>
        <h4>Rendered at {new Date().toLocaleTImeString()}</h4>
      </div>
    );
  }
}
```

Upar mein maine JS ke Date Object aur uske pre-defined functions ko JSX ke HTML return statements mein {} ke andar use kiya.


Iska matlab ye ki aap apne JSX code mein kahin bhi Javascript use kar sakte ho. 

JSX mein JavaScript ka use janne ke liye [yahan](https://reactjs.org/docs/introducing-jsx.html) aur padh sakte hain.

Ab pichle lesson mein banaye hue static application ko aap JS ka use karke dynamic bana sakte ho.

**Assignment**

- Apne application mein "Analyze" button pe *hover* (mouse button place karne par) karte hi, uska color change karo.

Isme aapko JS event - onmouseover - ka use karna par sakta hai.
