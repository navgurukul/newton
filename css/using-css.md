```ngMeta
name: Using CSS
completionMethod: peer
```

## Using CSS

Ek "styles.css" naam ki file banao, jisme neeche diya hua code likho. Ab aap iss file ko uss folder mei save karo jaha apki HTML course ki index.html files stored hain.

```css
body {
    background-color: lightblue;
}
h1 {
    color: white;
    text-align: center;
}
p {
    font-family: verdana;
    color: darkgray;
    font-size: 20px;
}
```

_Dhyaan rakhe, agar file kisi aur folder mei hogi jaha index.html nahi hai toh aapka code sahi se nahi chalega._

Niche jo line di hain use index.html aur kindness.html ke "head" section mei add karo.

```css
<link rel="stylesheet" href="styles.css">
```

Ab agar aap index.html ya kindness.html ko browser mei khologe toh aapko CSS ke vajah se kuch colors, aur baaki style jo humne uss CSS file mei diye hai dikhenge.

Yeh gaur karne wali baat hai ki, aapne same CSS file se dono HTML mei style daal pa rahe ho. Aise hi aap kitni bhi files ko, same CSS file se style kar sakte ho.

- Apki website kuch [iss tarah](https://abhishekgupta92.github.io/equality2/) se dikhegi.
