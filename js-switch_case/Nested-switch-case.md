### Nested-Switch Statement:
Nested-Switch statements refers to Switch statements inside of another Switch Statements.
### Syntax
```javascript
switch(condition) {
  case x:
    // code block
    Break;
    switch(condition) {
	 case y:
    	 // code block
    	 break;
     default:
     // code block
    }
 default:
    // code block
}
```
