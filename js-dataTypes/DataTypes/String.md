```ngMeta
name: String
```

## Example:

```javascript
var greet1 = 'Hi Nayak!';  
// using single quotes
```

```javascript
var greet2 = "Hi Nayak!";  
// using double quotes
```

### Expalanation

In the above example the variable a contains a greeting which is saying **Hi Nayak**, if you see the saying that is actually a **string**. 
 
The string data type is used to represent textual data (i.e. sequences of characters). Strings are created using 'single' or "double quotes" surrounding one or more characters, as shown below:


```javascript
var name='kumar'
console.log(name);
// output : kumar
```
```javascript
var name="kumar"
console.log(name);
// output : kumar
```

### Note:

You can include quotes inside the string as long as they don't match the enclosing quotes.

### Example:

```javascript
var a = "I’m going to the classroom"; 
// single quote inside double quotes
```
### Expalanation

If you observe the above example, in variable named **a** we have a sentence that is **I’m going to the classroom**, in this sentence if you see a single quote is there after **I** , it won’t create a problem untill that is not matching with enclosing quotes because enclosing quotes are double quotes.

```javascript
var b = 'He said "bye" and went out.';  
// double quotes inside single quotes
```

### Expalanation

If you observe the above example, in variable named **b** we have a sentence that is **He said "bye" and went out**.  In this sentence if you see a double quote for **bye** inside a single quote, it won’t create a problem until that is not matching with enclosing quotes because enclosing quotes are single quotes.

```javascript
var c = 'We\'ll never leave you.';     
// escaping single quote with backslash
```

### Expalanation

If you observe the above example, if we have single quotes inside single quotes then it will create a problem for you to resolve that issue you need to use an escape sequence.
