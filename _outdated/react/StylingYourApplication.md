```ngMeta
name: Styling your Application
```

Apne React App ko hum CSS file ke through usi tarah style kar sakte hain - jaise hum normally web applications ko karte hain.
Aap apne react application mein apne HTML elements ko *class* ya *id* ya koi aur identifier de sakte hain. Aur un identifiers ko css file mein style kar sakte hain.

Note: Javascript mein "class" ek keyword hai. (Aapne dekha ki hum class create karne ke liye "class" keyword ka use karte hain) Isiliye class ka name assign karne ke liye hum JSX mein "className"

Example :

```jsx
class Header extends React.component {
  render() {
    return (
      <div className="myAppHeader">
        <h2>Nutrition Wizard</h2>
        <h4>Designed by NG Team</h4>
      </div>
    );
  }
}

ReactDOM.render(<Header />, document.getElementById('react-app'));
```

```css
.myAppHeader {
    font-size: 15px;
    text-align: center;
    background-color: lightgray;
}
```
**Assignment** 

- Aapne last class assignment mein <Header> component complete kiya tha aur uski HTML rendering ki thi. Iss assignment mein aap apne <Header> component ki styling complete kijiye.

Aapke application ka header UI iss assignment ke baad complete dikhna chahiye. Apne kaam mein apne peers se feedback lijiye.

