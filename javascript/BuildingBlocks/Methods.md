```ngMeta
name: Methods
```

# Methods

Hum programming language mein real life ko mirror karne ki kosish karte ha
in.

Real life mein humare aas paas sab kuch ek **Object** hota hai. Aur har **object** ki kuch khasiyat hoti hai aur wah kuch kar sakta hai.

Jaise, *spoon* ek real life object hai. *Spoon* se hum rice *pick* kar sakte hain.

Aam bhasha mein agar hume spoon se rice pick karna hai toh hum aise kahenge


```
Pick rice with spoon
```

Javacript ki bhasha mein hum isi ko aise kahenge:

```
> spoon.pick("rice");
```

Yahan par:
- *spoon* ek **object** hai
- *pick()* ek **method** hai. Methods se hum kuch kaam karte hain.
- *"rice"* pick method ka argument hai. Arguments optional hote hain. Inke baare mein hum baad mein janenge


Variables jinme *number* ya *string* stored hain, wo bhi objects ki tarah hi kaam karte hain. Unke paas bhi kuch *methods* hote hain jo javascript mein pre-defined hain.
Inhe **Built-in Methods** bhi kehte hain.

Example:

```
> var myName = "Rajeev"
> var myNameInCaps = myName.toUpperCase();
> myNameInCaps
```

toUpperCase() method myName mein stored value ko ALL CAPS mein bana deta hai. Iska output "RAJEEV" hoga.

Methods ka use karke hum variables mein stored values ko manipulate karte hain.

**Built-in Methods** ke baare mein aur janne ke liye aap [yahan](https://www.tutorialspoint.com/javascript/javascript_builtin_functions.htm) padhe.
*Number methods* bus numbers pe kaam karte hain aur *string methods* bus strings pe

**Homework**

- Number methods toFixed() and toString() console pe try karke dekho. Yaad rahe ki ye methods number objects ke saath hi kaam karenge.

- String methods charAt() and length() console pe try karke dekho. Yaad rahe ki ye methods string objects ke saath hi kaam karenge.

...
