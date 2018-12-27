# Loading and Dumping Database

Agar dekha jaye, toh yeh database ek simple json file hi hai. Database load karna - simply - uss file ko json mei padh kar ek json object mei load karna ke barabar hoga.

Aise hi, dump karna json.dumps ke barabar hoga. 

Iske liye hum python ki [json](https://docs.python.org/2/library/json.html) library use karenge.

## Solution
```python
import json

def load(fileName='hello.json'):
    meraDB = MeraDB(fileName)
    meraDB.load_file()
    return meraDB

class MeraDB():
    fileName = "hello.json"
    jObject = {}

    def __init__(self, fileName):
        self.fileName = fileName

    def load_file(self):
        content = open(self.fileName).read()
        self.jObject = json.loads(content)
        return self.jObject

    def dump(self):
        open(self.fileName, 'w').write(json.dumps(self.jObject))
        return "OK"
```

Save this file as meradb.py

You can use by writing the following content in your `usedb.py` file.

```python
import meradb
db = meradb.load()
db.dump()
```

