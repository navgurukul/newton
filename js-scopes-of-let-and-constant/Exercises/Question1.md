```ngMeta
name:Question1
```
#### hat is the output of the following code?

 ```javascript

function display(){
   var a=10;
   let b=13;
   if (true){
       console.log(a);
       console.log(b);
   }
}
display()
 ```
##### Feedback after submit:
10
13
 
##### Explanation:
A display named function is there, inside that we have 1 if block. Inside the function  block we defined two variables a and b with var and let keywords respectively. Here both a and b are working as function scoped variables aka local scoped to that function you can use them inside a function anywhere.
