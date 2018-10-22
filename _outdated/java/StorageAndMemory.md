```ngMeta
name: Storage and Memory
completionMethod: manual
```

Apne application mein social profile banane ke liye, hume logon ka name, age, profession etc. kahin pe store karna hoga.

Computers ki apni memory hoti hai jahan hum data store kar sakte hain. Iske liye hume computers ko instruction dena hoga.


Computer ki memory ko aap bahut saare boxes ki tarah imagine kar sakte hain. Koi bhi data store karne ke liye:

1. Hum ek box choose karte hain.
2. Uss box ko ek label dete hain.
3. Aur fir apni data ko uss box mein daal dete hain.

Data ko wapas se extract karne ke liye hum unn labels ko call karte hain.

Computers mein alag-alag tarah ke data ke liye, alag-alag tarah ki boxes hoti hain. Humein boxes ko label karne se pehle, wo kis tarah ki box hai, ye batana hota hai.

Jaise,

"int" type ka ek box hai jo integers(numbers) hold karta hai.

Mann lijiye ki humein kisi ki umar ko ek memory box mein store karna hai.

```java
int age;
// humne "int" type ka ek box choose kiya jispe "age" naam ka label dala hai

age = 23;
//humne "age" naam ke box mein "23" daal diya hai

System.out.println(age);
//Hum "age" label ko bula kar - usey print kar rahe hain
//Iska output 23 hoga 
```

Pura program kuch iss tarah hoga:

```java
public class Project{
  public static void main(String args[]){
    int age;
    age = 23;
    System.out.println(age);
    
  }
}
```
Java mein hum "age" ke label ko **variable** kehte hain. **age** variable ko hum apni program mein kabhi bhi koi doosri value assign kar sakte hain.

Jaise

```java
public class Project{
  public static void main(String args[]){
    int age;
    age = 23;
    System.out.println(age);
    age = 34;
    System.out.println(age);
  }
}
```
Iss program ka output guess kijiye.

Java mein aur bhi data types hote hain - jaise **char**,**bool**, **float**, **String etc.** 
Inke baare mein janne ke liye, niche diye hue links padhe:

https://www.w3schools.in/java-tutorial/data-types/
http://codingbat.com/doc/java-string-introduction.html

**Assignment**
- Codeacademy pe jakar Java ka [ye](https://www.codecademy.com/courses/learn-java/lessons/introduction-to-java/exercises/whats-your-name?action=resume_content_item) introductory tutorial complete karein. Isme 12 lessons hain aur ye aapke **Variables** aur **data types** ke concepts ko revise karega.
Saath mein hi ye aapko java mein numbers pe operate karna (Addition, Subtraction, Multiplication, Division, Greater Than, Less than, etc.) bhi seekhayega.

- Kisi 2 persons ka naam, age, gender aur professon apne program mein store karo (*Aap name1, name2 ...aise variables ka use kar sakte hain*)
  - Inn dono persons ke ages ko add karke (age1 + age2), computer par print karo
  - Dono persons  ke naame aur professions bhi print karo
