```ngMeta
name: Using Library
```

# Using Library

Internet pe javascript ki bahut saari libraries hai. Javascript ki library mein bahut saare functions, methods aur objects pre-defined hote hain. Inse humara kaam bahut aasan ho jaata hai. Hum inko apne projects mein directly use kar sakte hain. Ye javascript libraries khud javascript mein hi likhe hote hain. 

Kisi library ko apne source code mein include karne ke liye apne html file ke head tags ke beech mein apne library ka link include karna hota hai

```html
<script src="Library file ka link"=></script>
```

## Kisi bhi website par snowfall

Iss project mein hum kisi bhi website par snowfall karayenge.

1. Aap Codepen website pe koi sa bhi pen(page) chuniye. Maine [ye](https://codepen.io/rspilhaus/pen/OpWMPW) chuna 
2. Apne pen ke sabse upar aur <head> tag ke beech mein ye library include karein:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Snowstorm/20131208/snowstorm.js"=></script>
```
3. Check aapke page par snowfall ho raha hai ya nahi
4. Observer karein ki mouse pointer ka direction change hone se snowfall ka direction bhi change ho raha hai. 
5. Iss library mein Snowfall object define kiya gaya hai - jiski madad se aap Snowfall ki properties change kar sakte hain:
Apne javascript file mein
```javascript
snowStorm.snowColor = '#99ccff';   // blue-ish snow!?
snowStorm.flakesMaxActive = 96;    // show more snow on screen at once
snowStorm.useTwinkleEffect = true; // let the snow flicker in and out of view
```

**Homework**
1. Apne snow ko apne pasand ka color aur activity dijiye
2. Google karke javascript ke aur bhi libraries explore kijiye jinse aap mazedar chizen kar sake
  Aap [cornify.com] bhi explore kar sakte hain.

Aage hum Javascript mein Khud se Objects banana aur Events detect karna  (jaise click, mouse drag etc.) seekhenge. Abhi Library use karke kisi bhi site mein snowfall dal kar mazey kijiye. Cornify.com ki library bhi use karne ki kosish kijiye.

