```ngMeta
name: Java Switch
```

<h1>Java Switch Statement</h1>
The Java switch statement executes one statement from multiple conditions. It is like if-else-if ladder statement. The switch statement works with byte, short, int, long, enum types, String and some wrapper types like Byte, Short, Int, and Long. Since Java 7, you can use strings in the switch statement.

In other words, the switch statement tests the equality of a variable against multiple values.

`
Example: Swicth Case Statement
`
```java
public class SwitchExample {  
public static void main(String[] args) {  
    //Declaring a variable for switch expression  
    int number=20;  
    //Switch expression  
    switch(number){  
    //Case statements  
    case 10: System.out.println("10");  
    break;  
    case 20: System.out.println("20");  
    break;  
    case 30: System.out.println("30");  
    break;  
    //Default case statement  
    default:System.out.println("Not in 10, 20 or 30");  
    }  
}  
}  
```

For more Information click <a href="https://www.javatpoint.com/java-switch">Here</a>