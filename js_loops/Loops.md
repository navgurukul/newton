```js
console.log("Hello World")
console.log("Hello World")
console.log("Hello World")
console.log("Hello World")
console.log("Hello World")
 
Output :-
Hello World
Hello World
Hello World
Hello World
Hello World

```

> In the above example, I am printing Hello World 5 times by using console.log().

> But if one of our friends asks us to print Hello World 100 times, it will be really difficult  for us  to write or copy and paste Hello World 100 times.

> To resolve this issue in the programming loop comes in the picture. Loop helps us to do work again and again until the condition gets false. 

```js
var a = 1;
while(a <= 100){
  console.log("Hello World")
  a = a + 1
 
Output: - 
Hello World
Hello World
Hello World
Hello World
Hello World
.
.
.
Hello World

```

> The above program will print Hello World a 100 times.

> We defined,  a =1, it will check while condition a<=100 (1<=100) that is true, so it will go to run the inside block of code  and console the Hello World first time, and increment a to 2.

> Now a =2, it will check for a while condition a<=100 (2<=100) that is true, so it will go to run the inside block of code  and console the Hello World second time, and increment a to 3.

> Now a =3, it will check for a while condition a<=100 (3<=100) that is true, so it will go to run the inside block of code  and console the Hello World third time, and increment a to 4.

> Now a =2, it will check for a while condition a<=100 (4<=100) that is true, so it will go to run the inside block of code  and console the Hello World fourth time, and increment a to 5.
…
….
….
….
……

…….

> It will go upto 100, and print Hello World 100 th time and a is incremented to 101.

> Now a =101, it will check for a while condition a<=100 (101<=100) that is clearly false, so it won't run inside code and it will end.






