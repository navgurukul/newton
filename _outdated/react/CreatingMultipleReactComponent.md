```ngMeta
name: Creating Multiple React Components
```
Aapne iss se pehle lessons mein ek <Header> naam ka React component banaya tha.

Iss <Header> component ko aap HTML element ki tarah kisi bhi doosre React Component ke andar use kar sakte ho.

Aise:

**NutritionWizard/index.jsx**
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

class App extends React.component {
  render() {
    return (
      <div>
        <h2>This is the main app</h2>
        <Header />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('react-app'));
```
Aap dekh sakte hain ki humne <Header /> ko aise use kiya ki jaise wo HTML element ho. Aap <Header /> aur <App /> ko bhi isi tarah doosre React components ke andar use kar sakte ho. React ki yahi "reusability" bahut powerful feature hai.

~                                                                         **Assignment**

- React Components ko use karte hue, apne Nutrition Wizard Application ko ek static design dijiye. Iss stage pe aapka page dikhne mein [aisa](https://www.edamam.com/website/wizard.jsp?ver=wizard-basic) ban sakta hai. Lekin ye static hoga aur isme user interactions nahi honge (jaise button pe hover karke color change hona etc.)

