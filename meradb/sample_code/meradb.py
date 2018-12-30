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