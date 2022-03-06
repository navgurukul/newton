objects-destructuring_key1
```javascript
var navgurukul = {
   mentor: 'Priya',
   mentee: 'Sapna'};

var mentor     = navgurukul.mentor;
var mentee = navgurukul.mentee;
console.log(mentor);     // => 'Priya',
console.log(mentee); // => 'Sapna'

```
 
objects-destructuring_key2



objects-destructuring_key3


objects-destructuring_key4


```javascript
var navgurukul = {
   mentor: 'Priya',
   mentee: 'Sapna'
 };
 
({mentor,mentee} = navgurukul);
console.log(mentor);     // => 'Priya',
console.log(mentee); // => 'Sapna'

```

objects-destructuring_key5


objects-destructuring_key6


objects-destructuring_key7


objects-destructuring_key8


objects-destructuring_key9


objects-destructuring_key10


```javascript
var navgurukul = {
   mentor: 'Priya',
   mentee: 'Sapna'};
 
const {mentor,mentee} = navgurukul;
console.log(mentor);     // => 'Priya',
console.log(mentee); // => 'Sapna'
```

objects-destructuring_key11
