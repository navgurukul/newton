```ngMeta
name: Binding Methods to Events
```

Hum chahte hain ki user ke *button* *click* hote hi ek function call karein jo humare React Component ka state change kar de.

Plain Javascript mein hum iske liye addEventListener() function use karte the. Leki React mein hum **props** ka use karke bahut aaram se events ko kisi bhi method (function) se attach (bind) kar sakte hain.


Example Code:
(button ke onclick event ko ek function se binding dikhate hue)
```jsx
import React from 'react';

class NutrtionAnalyzer extends React.component {
  ....
  ....

  updateAnalyzer() {
    //<Apne React comonent ke states update karne ke liye code>
  }

  render() {
    return (
      <div>
        ....
        ....
        <button onClick={this.updateAnalyzer}>Analyze</button>
      </div>
    );
  }
}

export default NutritionAnalyzer;
```

Upar mein humne Button ke **onClick** event ko **updateAnalyzer()** function se __bind__ kar diya hai.
Yaani button click hote hi updateAnalyzer function run hoga.

React mein Event Binding ke aur bhi tareeke hain. Aap [yahan](https://www.rithmschool.com/courses/react-fundamentals/react-events) se aur padh sakte hain.

**Assignment**
- React Event binding use karke apne App ko aur bhi interactive banaiye. Example ke liye button element pe aap onMouseMove event ke saath koi method binding create kar sakte hain jisse button ka background color change ho.
