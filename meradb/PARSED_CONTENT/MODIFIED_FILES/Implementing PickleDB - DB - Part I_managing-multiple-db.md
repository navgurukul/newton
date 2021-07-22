managing-multiple-db_key1
managing-multiple-db_key2


managing-multiple-db_key3


```python
import meradb
db1 = meradb.load('pehla.db', True)
db2 = meradb.load('doosra.db', True)
db1.set('key', 'value1')
db2.set('key', 'value2')
db2.get('key')
db1.get('key')
```
managing-multiple-db_key4


managing-multiple-db_key5
