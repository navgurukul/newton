```ngMeta
name:Questtion2
```
#### What is the output of the following code?

```javascript 
function display(){
   if (true){
       var a=10;
       let b=13;
   }
    if (true){
       console.log(a);
       console.log(b);
   }
}
display()
```
 
##### Feedback after submit:
10
ReferenceError: b is not defined
 #### Explanation:
A display named function is there, inside that we have 2 if blocks. In the first if we defined two variables a and b with var and let keywords respectively.  After that in the second if block we are asking to print a and b.. Because var is defined inside a function, it has function scope and it is going to print its value 10, but in the case of let, let is declared in inside first if block because of let is a block scoped we are not able to access it in another if block, it given us reference error b is not defined.
