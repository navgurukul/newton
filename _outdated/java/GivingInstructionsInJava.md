```ngMeta
name: Giving Instructions In Java
```

Iss lesson mein hum Computer ko ek simple instruction denge aur Java language ke through instruction dena seekhenge.

Hume Java language ke through computer ko "Hello World!" print karwana hai.

Koi sa bhi editor (like gedit ya atom) kholiye aur usme ye likhiye:
*Apne file ko javaPrograms naam ke folder mein save kijiye. File ka naam HelloWorld.java rakh sakte hain*

**javaPrograms/HelloWorld.java**
```java
System.out.println("Hello World!");
```

Ye statement java language mein computer ko instruction de raha hai ki wo screen par "Hello World!" print kare.

Aap (" ") ke andar koi aur bhi text daal sakte hain.


Lekin abhi Java upar diya hua instruction follow nahi karega. Uske liye humein kuch aur cheezen add karni parengi.

**javaPrograms/HelloWorld.java**
```java
public class HelloWorld {
  public static void main(String[] args){
    System.out.println("Hello World!");
  }
}
``` 

Humne jo code abhi add kiya hai, uske baare mein hum baad mein seekhenge. Abhi itna samajh lijiye ki java program "public static void main" ko dhoondta hai aur uske andar likhe hue saare instructions ko follow karta hai.

Upar likhe hue program ko hume *compile* karke machine code mein conver karna hoga. Uske baad hum apne program ko run kar sakte hain.

**Assignment**

- Apne java program ko neeche diye hue resource ko use karke :
1. Program ko Compile kijiye
2. Program ko run kijiye

*Resource*
https://askubuntu.com/questions/145748/how-to-compile-a-java-file-on-ubuntu

