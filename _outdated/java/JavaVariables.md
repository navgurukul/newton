```ngMeta
name: Java Variables
```
<h2>What is Variables?</h2>
Variable ek memory location ke name hota hai jisme values; variable ko diya jata hai aur wo uss location par store ho jata hai.

<h2>Syntax for Variable Declaration</h2>

```
data_type_name variable_name;
data_type_name variable_name1, variable_name2;
```

For example,
```java
  int a;
  int b,c;
```

<h2>Syntax for Variable Definition</h2>

```
data_type variable_name = variable_value;
```
 <br>

 For Example,
```java
int a = 5;
int b =10, c = 15;
```

Java mein 3 type ke Variable hote hai<br>

1. Local Variable
2. Instance Variable
3. Static Variable

<h3>Local Variable</h3>
Local Variable block, method aur constructor ke andar hota hai.
Local Variable ka scope; local hota hai. Ye sirf method aur constructor ke andar visible hota hau.
Aur jab Local Variable; method aur constructor ke bahar ho jata hai to tab wo distroy ho jata hai.<br><br>

Example,
```java
class Sample{
    
   void display(){
       int a = 5;   //Local Variable
       System.out.println("Value of a : " + a);
    }
    public static void main(String arg[]){
        Sample s = new Sample();
        s.display();
    }
}
```

<h3>Instance Variable</h3>
Instance Variable; class ke andar hota hai aur method aur constructor ke bahar hota hai.
Instance Variable non-static variable hota hai.<br><br>

Eaxample,
```java
class Sample{
    int a = 5;  //Instance Variable
   void display(){
       System.out.println("Value of a : " + a);
    }
    public static void main(String arg[]){
        Sample s = new Sample();
        s.display();
    }
}
```

<h3>Static Variable</h3>
Static Variable ko hum Class Variable bhi khtai hai.
Ye Instance Variable ke trah class ke andar aur method aur constructor ke bahar hota hai.
'static' keyword ke sath inka use kiya jata hai.<br><br>

Example,
```java
class Sample{
    static int a = 5;  //Static Variable
   void display(){
       System.out.println("Value of a : " + a);
    }
    public static void main(String arg[]){
        Sample s = new Sample();
        s.display();
    }
}
```
