```ngMeta
name: Using Libraries In Javascript
```

Abhi tak aapko jab bhi javascript ki libraries use karni hoti hai, toh aapapne HTML file mein ek script tag add kar dete ho. 

Asie:

**NetworkWizard/index.html**
```HTML
<script src="Path to the library here"></script>
```

Isse aapke Javacript file mein yeh library import ho jaati hai aur aap us library mein defined variables aur functions ka use kar sakte ho.

Hum React bhi isi tarah se apne application mein import kar sakte hain.

**NetworkWizard/index.html**
```HTML
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/0.14.6/react.js"></script>

```
LEKIN

Javascript ke ek naye convention se (jise hum ES6 khete hain), javascript libraries ko import karne ka ek better tareeka hai jise hum javascript file ke andar se hi kar sakte hain.

**NetworkWizard/index.js**
```javascript
import React from 'react'
```

Iss statement se 'react' library import ho kar React naam ke variable mein store ho jaati hai.

Aap **import** statement ke baare mein [yahan](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) se padh sakte hain.


**Assignment**

- Apne javascript file mein 'react-dom' library ko import kijiye.




