loading-and-dumping_key1
loading-and-dumping_key2


loading-and-dumping_key3


loading-and-dumping_key4


loading-and-dumping_key5[loading-and-dumping_key6](https://docs.python.org/2/library/json.html)
loading-and-dumping_key7

loading-and-dumping_key8
loading-and-dumping_key9[loading-and-dumping_key10](https://www.w3schools.com/python/python_classes.asp)
loading-and-dumping_key11

```python
import json

# fileName = "hello.db"
# Default argument dena ek acchi coding practice hai.
# Isse agar user koi argument nahi bhi de, toh bhi code sahi chalega
def load(fileName='hello.db'):
    ```    Yeh ek fileName leta hai, jiska content yeh load karta hai
    By default yeh hello.json file ko load karta hai
    Content load kar ne ke liye, yeh ek MeraDB class ka object
    create karta hai. Ussi object ko yeh return kar deta hai
    jisse ki hum uss object par set, get, aur dump jaise
    functions call kar sakein.
    ```
    meraDB = MeraDB(fileName)
    meraDB.load_file()
    return meraDB

loading-and-dumping_key12


    Humne yeh class isliye banayi jisse ki hum meradb object bana kar
    uss par koi bhi functions call kar sake

    Jaise list_a = [1,2,4] kar kar aap list_a naam ki list create karte ho
    Phir aap list_a object par functions call kar sakte ho, jaise
    list_a.append(another_list), list_a.pop()

    aise hi jab aap meradb ka object declare karoge, toh class use karne ke
    vajah se, hum meradb object par functions call kar payenge, jaise:

    mdb = MeraDB("dbfile.json")
    mdb.load_file()
    mdb.dump()
    
    class ke ander variable ko property bolte hai aur function ko method.

    ```
    fileName = ""
    jObject = {}

    def __init__(self, fileName):
        ```
        Yeh constructor function hai, jo object declare karne par
        call hoga. Jo bhi fileName isse milega, yeh woh apni 
        fileName property mei store kar lega. Isse yeh property
        object mei kahi bhi self.fileName kar kar, available hogi.
        Isliye jab hum dump_file function aage call karenge
        toh apne aap iss code ko pata hoga, ki kis file mei content
        dump karne hai. Woh bas self.fileName file mei jakar contents
        save/dump kar dega. Aise hi aap aur bhi properties bana sakte
        hai. Jaise humne jObject kar kar ek property banayi hai. Iss
        property mei, jab bhi database load karte hai, woh dictionary
        hum jObject store kar lete hai. Jab bhi koi value set ya get karni
        hoti hai, toh hum jObject se hi karte hai. Aakhir mei, dump karte 
        hue hum jObject ko dump kar dete hai, jab bhi dump function call
        hota hai.
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
        ```
        You can also write the above line as:
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()
        ```

        print "DB dumped successfully!"
        return "OK"
```

Save this file as meradb.py. Isse hum import meradb kar payenge.

You can use by writing the following content in your usedb.py file.

```
```python
import meradb
db = meradb.load("table.db")
db.dump()
```

loading-and-dumping_key13
```json
{}
```
loading-and-dumping_key14


loading-and-dumping_key15


loading-and-dumping_key16


loading-and-dumping_key17
loading-and-dumping_key18
- loading-and-dumping_key19
- loading-and-dumping_key20
- loading-and-dumping_key21
loading-and-dumping_key22


loading-and-dumping_key23
loading-and-dumping_key24
loading-and-dumping_key25


loading-and-dumping_key26


```python
if edge_case:
    kuch_jugaad_karo
```

loading-and-dumping_key27


loading-and-dumping_key28
loading-and-dumping_key29


loading-and-dumping_key30


loading-and-dumping_key31


loading-and-dumping_key32
