## Managing Multiple DB

Kisi bhi database ko load karne ke liye, humei uss database ka naam `load` function mei dena hota hai. Aise hum ek saath multiple `databases` ke saath kaam kar sakte hai.

Jaise yeh code chala kar dekhe, python terminal mei:

```python
import meradb
db1 = meradb.load('pehla.db', True)
db2 = meradb.load('doosra.db', True)
db1.set('key', 'value1')
db2.set('key', 'value2')
db2.get('key')
db1.get('key')
```

Toh aap same file ko use kar kar, kitne bhi databases ko simultaneously (ek saath) use / load kar sakte ho.

Thodi der apne likhe hue functions ke saath khelo, before you move to the next course.
