```ngMeta
name: Firing Up React Application
```

Aapne abhi tak React application mein ye banaya hai:

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

Iss application ko aap agar directly browser mein run karoge toh ye theek se display nahi hoga.

Iske liye hume ek http-server install karna hoga, jahan hum apne application ko locally host kar paye.

```
npm install http-server -g

http-server <path to the application directory>
```


http-server par apne application ko run karne ke baad, aap browser mein http://localhost:8080 run kijiye aur apne app ko chalte hue dekhiye.

**Assignment**
- 8080 humare computer (jispe hamara application host hua hai) ka ek port hai. "http-server" ka [documentation](https://github.com/indexzero/http-server) padh kar, aap apne application ko kisi doosre port par host karein.
