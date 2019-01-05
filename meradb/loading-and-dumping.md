# Loading and Dumping Database

Agar dekha jaye, toh yeh database ek simple json file hi hai.

Database load karna - simply - uss file ko json mei padh kar ek json object mei load karna ke barabar hoga.

Aise hi, dump karna uss file ko json.dumps use kar kar, uss file mei dump karne ke barabar hoga. 

Iske liye hum python ki [json](https://docs.python.org/2/library/json.html) library use karenge.

## Starting Code
Iss code ko implement karne ke liye, maine classes use ki hai. Aap kisi aur tarah se bhi yeh kar sakte hai. Classes ke introduction ke liye, aap yeh [padhein](https://www.w3schools.com/python/python_classes.asp).

```python
import json

def load(fileName='hello.db'):
    ```
    Yeh ek fileName leta hai, jiska content yeh load karta hai
    By default yeh hello.json file ko load karta hai
    Content load kar ne ke liye, yeh ek MeraDB class ka object
    create karta hai. Ussi object ko yeh return kar deta hai
    jisse ki hum uss object par set, get, aur dump jaise
    functions call kar sakein.
    ```
    meraDB = MeraDB(fileName)
    meraDB.load_file()
    return meraDB

class MeraDB():
    ```
    Yeh main class hai, jaha saara magic hoga!
    ```
    fileName = ""
    jObject = {}

    def __init__(self, fileName):
        ```
        Yeh constructor function hai, jo object declare karne par
        call hoga
        ```
        self.fileName = fileName

    def load_file(self):
        ```
        Yeh file ko load karne ke liye function hai
        ```
        print "Loading Database from ", self.fileName, " !"
        content = open(self.fileName).read()
        self.jObject = json.loads(content)
        print "DB loaded successfully!"
        return self.jObject

    def dump(self):
        ```
        Iss function ko use kar kar, aap content ko dump kar satke hai
        ```
        print "Dumping database to ", self.fileName, " !"
        open(self.fileName, 'w').write(json.dumps(self.jObject))
        print "DB dumped successfully!"
        return "OK"
```

Save this file as meradb.py. Isse hum `import meradb` kar payenge.

You can use by writing the following content in your `usedb.py` file.

```python
import meradb
db = meradb.load("table.db")
db.dump()
```

Ek `table.db` file banao jismei yeh content daalo.
```json
{}
```
Isse aapka code `table.db` se ek empty database ko load kar payega.

Agar aap dekhenge toh humne jaise pickleDB use kiya jaata hai, ussi ki tarah ki basic implementation kar di hai. Yeh implementation samajhne ke liye aap ko thoda time spend karna chahiye.

Uske baad iss code ko khud likhiye, aur koshish karein ki `ek hi baar` mei chal jayein. Copy and paste kar kar chalane ka fayda nahi hai.

## FAQs
Humne teen **`files`** kyu banayi hai?
- Jo hum database bana rahe hai - uska code ek file mei **`meradb.py`** hai, jisse ki koi bhi usse use kar payein.
- **`usedb.py`** woh code hai, jo koi bhi user likh sakta hai - hamare database ko use karne ke liye.
- **`hello.db`** woh code hai, jo ek empty database initialise karta hai.
Hum aagein **`Exercise`** mei dekhenge ki kaise bina hello.db file banaye, yeh code likha ja sakta hai.

Note: Iss program mai hum ek file se data nikal ke dusre file mai store kar rhe hai, par diye gai program mai hum ek hi file se data nikal ke usmai hi store kar rhe hai , aap chahe toh do file bana sakte hai or ek file se data nikal kar dusre mai store kar ke dekh sakte hai.

## Exercise
### Edge Case 1
Agar `table.db` ek empty file hogi, toh code mei kya error aayegi? Aap kaise code ko modify kar sakte hai, jisse ki ek empty file hone se bhi database load ho jaye aur error throw na ho.

Kya aap code ko padh kar samajh gaye the ki - yeh case sahi se handled nahi hai?

### Edge Case 2
Agar `table.db` file exist nahi karegi, toh code kya error throw karega? (Koshish kara karein, ki bina run guess kar payein, aise questions ka answer. Phir chala kar apna answer verify aur discuss karein. Aise hi aap acche se programming mei apna confidence build kar payenge.)

Kya yeh error throw ki jaani chahiye?

Agar aap chahe ki yeh error na throw ho toh - toh aap kya modifications kar sakte hai jisse ki agar file na bhi exist karein toh bhi aapka code sahi chalein aur koi error throw na karein?

Kya aap yeh edge case soch payei the?
