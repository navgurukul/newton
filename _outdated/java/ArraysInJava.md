```ngMeta
name: Arrays In Java
```
Humne pichle lessons mein data ko store karne ke liye bahut saare **variables** banaye the ......

name1
name2
age1
age2
gender1
gender2
profession1
profession2
.......
.......
.......


Java mein data ko store karne ke kai tareeke hote hain. Pichle lessons mein humne ek variable mein bas ek hi data store karna seekha hai.
Jaise - 

```java
String name1 = "Sandeep Sharma"
```

Java mein hum ek variable mein ek se jyada data values bhi store kar sakte hain. Iske liye hum Java mein **Arrays** ka use karte hain.
**Arrays** ek tarah ka list hota hai, jisme hum bahut saare values store kar sakte hain.

Ek string **array** (ek list jisme string values store hote hai) bana kar usme value store karne ke liye:

```java
String[] person1 = {"Megha Kumari", "21", "Female", "Astronaut"}
```

Iss statement se humne computer ne 4 memory boxes use kiye jinme upar diye hue data ko store kiya.

Pehle box ka naam person1[0] hai.
Doosre box ka naam person1[1] hai.
Teesre box ka naam person1[2] hai.
Fourth box ka naam person1[3] hai.

*Note: Computer mein counting hamesha 0 se shuru hoti hai*

Humein agar person1 ka profession print karna hai toh:

```ngMeta
System.out.println(person1[3]);
``` 

Arrays ke baare mein aur padhne ke liye [yahan](https://www.tutorialspoint.com/java/java_arrays.htm) padhe.

**Assignment**

- Array ko use karte hue, 3 persons ka data bas 3 variables mein store karo.
- Teeno persons ka social profile (name, age, gender and profession) print karo.
