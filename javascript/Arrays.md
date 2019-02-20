```ngMeta
name: Arrays
```

# Arrays

Humne javascript mein variable ka use dekha. Variable ko ek naam dekar hum usme koi value store kar sakte hain.

Agar javascript ko use karke aapko ek grocery list banani hai, toh humara approach kuch aisa ho sakta hai:

```javascript
var firstItem = "Rice";
var secondItem = "Pulses";
var thirdItem = "Vegetables";
....
....
....
```

Aapko realize hoga ki ye bahut tiring hain. Hume iske liye bahut saare variables chahiye. Har naye item ke liye hume ek naya variable add karna padega.

Javascript mein aise lists banane ka ek aasan tareeka hai. Ise hum **Arrays** kehte hain.

Arrays ko use karke aap bus ek variable declare karte hain aur uske andar sare items ki list dal sakte hain.

```javascript
var groceryList = ["Rice","Pulses","Vegetables","Eggs"];
```

Iss ek groceryList variable mein bahut saare values ki list stored hai. Agar hume pehle item ko access karna hai toh woh hum groceryList ke aage uska number(index) laga ke karte hai:

```
console.log(groceryList[0]);
```
*Hint*: Javascript mein counting hamesha 0 se shuru hoti hai. Toh pehla item 0 pe hai, doosra item 1 pe, teesra item 2 pe and so on.

Iss code ka output kya hona chahiye?


Javascript mein Arrays ke paas kuch pre-defined methods hote hain, jinka use aap kar sakte ho.
Jaise agar aapko apne groceryList mein koi naya item add karna hai toh .push() method ka use kar sakte hain.

```javascript
groceryList.push("Biscuits");
```
Isse aapke groceryList mein "Biscuits" item add ho jayega. Console par array ko print karke dekhiye ki array kahan add hua.

Aise hi, last item ko hatane ke liye
```javascript
groceryList.pop();
```

Isse aaple list ka last item hat jayega.


Array ke pre-defined methods ke baare mein aur janne ke liye aap [yahan](https://www.w3schools.com/js/js_array_methods.asp) se padh sakte hain.
Arrays ke pre-defined methods .foreach() and .map() ko specially dhyan se padhiye aur practice kijiye.

**Homework:**

- Ek chota sa To-do application banaiye jisme aap user se action item mang kar usey apne application mein display kar rahe hain.
- User chahe toh apne action item ko check kar sakta hai ya delete bhi kar sakta hai.
- Iss application ko banane ke liye aapko forms, arrays aur functions ke concepts use karne par sakte hain.


