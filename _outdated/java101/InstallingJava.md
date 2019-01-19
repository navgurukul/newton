```ngMeta
name: Installing Java
```

Ab hum apne system pe Java install karenge. Jab humare system pe java hoga woh humein java ke saare programs ko run karne mein help karega.

Neeche di hui command ko apne terminal pe run karo. Agar koi errors aati hain toh apne peers ke saath debug karne ki koshish karo.

```sh
sudo apt-get install default-jdk
```

Isse aapke system mein java install ho jayegi.

Java install karne ke baad apne text editor (Atom) mein ek nayi file banao aur isme neeche diya hua code likho.

```java
public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hi from NavGurukul!");
    }

}
```

1. Ab iss code ko ek file mein save karo jiska naam "HelloWorld.java" ho.
2. Apne terminal mein jao.
3. Uss directory mein `cd` karo jisme aapka code hai.
4. Fir neeche di hui command ko execute karo.

```sh
javac HelloWorld.java
```

Ab aapki directry mein ek `HelloWorld.class` naam ki ek file ban gayi honi chaiye. Yeh aapka compiled java ka code hai. Isko run karne ke liye neeche di hui command ko run karo.

```sh
java HelloWorld
```

Aapke terminal pe `Hi from NavGurukul!` print hua hona chaiye. Agar hua hai toh matlab aapki java sahi se install ho gayi hai. Nahi toh apne peers se help karke isko sahi karo.

Agle chapters se java ke baare mein dhang se samajhne shuru karte hain :)

Course mein aage har chapter mein aapko bahot saare videos dikhaye jayenge. Videos dekh ke normally lagta hai ki humein ache se samajh aa gaya. But jab tak hum ache se apne aap code chala ke nahi dekhte tab tak samajh nahi aata. Isliye bahot important hai ki hum code ko saath saath chalaye aur jahan thodi si bhi confusion hai apne friends ke saath discuss karein aur concepts ko clear karein. Jab tak concepts ache se clear nahi ho jaate tab tak humein aage nahi badna chaiye.
