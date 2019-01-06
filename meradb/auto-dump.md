## Auto Dumping

```python
import meradb
db = meradb.load('ektha.db')
db.set('key1', 'value1')
db2.get('key1')
db.set('key2', 'value2')
db1.get('key2')
```

Yeh code execute karo. Kya iss code ko execute karne ke baad `ektha.db` file ke contents change hue?
Agar haa, kya yeh theek hai?
Agar naa, toh aisa kyu hua?

Kya woh changes important hai?

Agar hum chahte hai, ki hamare changes, hamari file (yaani Hard Disk mei) **persistently** jaaye, toh hum `dump` function abhi tak call kar rahe the.

Par hum ab kuch aisa karenge, ki bina `dump` function call karein bhi, jaise jaise, hum values set karte jaye, toh woh changes hamari `hard disk` yaani `file` mei bhi write ho jaye.

## Task
Humein `load` function ko aise modify karna hai, ki agar second argument `True` ho toh - file mei `auto dumping` enable ho jaye.

Iska matlab hai ki, jaise hi koi bhi value `set` ki jaye, toh woh database mei `write` ho jaye.

Sochiye, agar aap aisa nahi karenge toh kya hoga.
To hum jo bhi `set` operations karenge, jab tak database mei `dump` nahi karenge, tab tak hamari file mei write nahi honge.

Par `auto dumping` enable karne se, hamara code har `set` operation ke baad automatically update kar dega. Par yeh update sirf tab hi karega jab `load` ko `True` as an argument milega. Agar usse ya toh

- koi second argument nahi milega
- ya `False` argument milega

toh code pehle ki tarah hi chalega. Yaani agar `dump` function call nahi kiya hoga, toh database mei koi change nahi hoga.