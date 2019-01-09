```ngMeta
name: Props
```

HTML padhte samay aapne har elements ke kuch pre-defined **attributes** use kiye the

Jaise:

```HTML
<img src="navgurukul.png" alt="navgurukul logo" width="500">
```

Yahan par **src**, **alt** aur **width**  <img> element ke pre-defined attributes hain jo ek pre-defined kaam karte hain.

jaise - *alt* attribute image load hone tak ek alternate text display karta hai.


React jo custom HTML elements ki tarah hi hote hain) mein bhi HUM khud se hi apne react components ke attribute define kar sakte hain. Hum inhe react mein props (short for properties) kehte hain.

Aapne React Dev tool use karte hue "React Componets ke prop" dekhe the?
example:

```jsx
....
....
....

ReactDOM.render(<App name="Nutrition Wizard"/>, document.getElementById('react-app'));

```

yahan par humne <App> react component ke liye ek custom(khud se define ki hui) prop define kiya hai - jiska naam "name" hai

Iss prop ko hum use kaise karein??

"name" prop **App** class ke andar **props** mein stored hai - usey hum this.props.name se likhte hain. 

**Note:** "this" jis class mein hum hain use refer karta hai - yani yahan par App class ko.
this.props.name ka matlab **App** class ke **props** mein se **name** naam ka prop
Aise multiple props aap define kar sakte hain aur this.props.<prop-ka-naam> use kar ke usey use kar sakte hain.
this.props.name yahan pe ek Javascript variable hai - jiske andar "Nutrition Wizard" stored hai.

Isey apne code mein use karne ke liye:


```jsx
class App extends React.component {
  render() {
    return (
      <div>
        <h2>{this.props.name}</h2>
      </div>
    );
  }
}

ReactDOM.render(<App name="Nutrition Wizard"/>, document.getElementById('react-app'));
```

Humne this.props.name ko curly bracket mein likha hai kyonki wo ek Javascript variable hai aur hum usey HTML return code block ke andar likh rahe hain.

**Assignment**

- Apne react component ke liye multiple props define kijiye aur usey apne code block mein use kijiye
- Apne application mein ek react component banaiye jo recipe ka nutrition data display kare. iss react component ko props ke through data pass karke nutrition data display karwaiye.
