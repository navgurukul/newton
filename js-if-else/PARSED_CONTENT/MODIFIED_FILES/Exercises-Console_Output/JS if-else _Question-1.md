Question-1_key1


```javascript
var day = "TUeSday".toLowerCase();

if (day == "monday") {
  console.log("Dhanwantari\nSiddhi\Kritika\Salon\nMayuri\Gauri");
}
else if (day == "tuesday") {
  console.log("Keemaya\nRoshni\nPooja\Priyanka\nnalini\nManisha");
}
else if (day == "wednesday") {
  console.log("Shrusti\Karuna\Parveen\Sandhya\nLeena\Karishma");
}
else if (day == "thursday") {
  console.log("Nikita\nMona\nPriyanka\Tejashree\nLovely\Mehzebin");
}
else if (day == "friday") {
  console.log("Pihu\Sejal\nChaya\Shrestha\nMonali\nAardhangya");
}
else if (day == "saturday") {
  console.log("Gunjan\nShweta\nRani\nIsha\nKusu\Madhu\n");
}
else if (day == "sunday") {
  console.log("Swati\nKhusboo\nidhi\Preeti\nDipti\nAnamika");
}
else {
  console.log("Please enter valid week day")
}

```

```solution

Output:
keemaya
roshni 
pooja
priyanka
nalini
Manisha

**Explanation:**

toLowercase() function is used to convert any letters into small lowercase.
 
The day is tuesday and at first it will check for if condition when it fails, so it will check for another else if condition when it is true it will go to the body of that particular else if and if it fails it will go to check one more conditional expression.

Because first else if correct and it enters into the body of else if and it console the given text to it.
```