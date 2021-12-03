```ngMeta
name: Object destructuring
```


Example:
```javascript
var navgurukul = {
   mentor: 'Priya',
   mentee: 'Sapna'};

var mentor     = navgurukul.mentor;
var mentee = navgurukul.mentee;
console.log(mentor);     // => 'Priya',
console.log(mentee); // => 'Sapna'

```
 
This is what you do for extracting values from an object writing navgurukul two times for getting values, Here you have created two new variables, mentor and mentee, and used dot notation for getting values from an object.


Here navgurukul.mentor is referring to Priya and that is assigning to name a new variable.
And one navgurukul.mentee is referring to Sapna and it is assigned to mentee another new variable.

A neater code for that is rather than create new variables

```javascript
var navgurukul = {
   mentor: 'Priya',
   mentee: 'Sapna'
 };
 
({mentor,mentee} = navgurukul);
console.log(mentor);     // => 'Priya',
console.log(mentee); // => 'Sapna'

```

Here is where the concept of destructuring the object introduced for, To write a neater and structured code like this and for removing the extra variables from the program.

As you can see in the above example, the object from the Left hand side has the properties mentor and mentee with the values Priya and Sapna respectively. Note that you need to give the same property names in ({mentor,mentee} = navgurukul); , so that mentor’s value from navgurukul will store into mentor in curly braces and same for mentee. If you do not do so it will throw a reference error that the property name you have mentioned is not defined.

( ) why we are using the parenthesis around ({mentor,mentee} = navgurukul);  that may be a question to you is right. If I am not taking parenthesis it will give me an error as SyntaxError: Unexpected token '='.

Why the error is coming is because when the code will see {} curly braces it will feel it as block code. That's why for avoiding this error we used () parenthesis.

You can extract properties from an object.

Without parenthesis you can do like also:

```javascript
var navgurukul = {
   mentor: 'Priya',
   mentee: 'Sapna'};
 
const {mentor,mentee} = navgurukul;
console.log(mentor);     // => 'Priya',
console.log(mentee); // => 'Sapna'
```

By putting const you are declaring them and you are destructuring (formatting the data in the structured manner)the mentor and mentee from the navgurukul object. It is important to maintain the data in the code by using less space and it helps to write the code neatly as well.
