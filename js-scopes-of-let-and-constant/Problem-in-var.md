```ngMeta
name:Problem-in-var
```
Imagine you are writing a code for storing and displaying someone's aadhar card number.As you can imagine an aadhar card number cannot change for a person. But if you declare a variable with var you can change its content.

```javascript
var aadharCardNumber= "abcd1234"
var aadharCardNumber="xyz0987"
console.log(aadharCardNumber); // xyz0987
```
 #### explantion
Now programmatically there is no problem in this code, you can declare a variable aadharCardNumber you can store a value in it like abcd1234 and you can redeclare it like xyz0987. But your program should not be changing people's aadhar card numbers because those numbers are constant. This is where const and let can be used for.

#### Example:

```javascript
isHeUsingAtm = true
if (isHeUsingAtm){
   var secretPin=1234
   console.log('please use Atm');
   console.log('while using Atm :'+secretPin);
   console.log('Thank you for using Atm');
 
}
console.log('After using Atm :'+ secretPin);
 ```
 ##### output
// please use Atm
// while using Atm :1234
// Thank you for using Atm
// After using Atm :1234
 

Think of a situation where you want to use atm, while using atm, machine ask you to enter pin or  store your atm pin for only sometime and not let it to remember even after using the atm, well it is not secure if it is storing your atm pin after you are using also.

#### Explantion:
In the above example, think of a block as an atm, and you entered it because you have to use atm, after entering it took your atm pin and stored it into a variable which is declared with var. And you also felt that it is safe only but actually which is not. You can clearly see in the above example that after coming out of a block or after using atm still it knows your atm pin which is not secure. That happened only because of keyword var. So, we want something which holds your values for a particular block. This is where let can be used for.

