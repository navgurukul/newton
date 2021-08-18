Write a function that takes 2 strings as parameters and prints whose length is bigger, if both lengths are equal print two strings.

#### Hint :Use len() builtin function.

Input:

is_equal_lenth(“hello”,”welcome”)

is_equal_lenth(“sonu”,”monu”)

Output :

welcome
 
sonu

Monu

```javascript
// write code here
```
 
```solution

function is_equal_lenth(str1,str2){
   if(str1.length === str2.length){
       console.log(str1);
       console.log(str2);
   }
   else if(str1.length > str2.length){
       console.log(str1);
   }
   else{
       console.log(str2);
   }
}
 
is_equal_lenth("hello","welcome");

```