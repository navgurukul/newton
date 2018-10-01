```ngMeta
name: Read the JSON
completionMethod: peer
```

Iss program ko attempt karne ke liye pehle ek `users.json` naam ki file mein neeche diye hue text ko save karein.

```json
{
    "users": [{
            "firstName": "vidur",
            "lastName": "singla",
            "details": {
                "age": 21,
                "mobileNo": 1234567890,
                "City": "Delhi"
            }
        },
        {
            "firstName": "rishabh",
            "lastName": "verma",
            "details": {
                "age": 22,
                "mobileNo": 12345678320,
                "City": "Chandigarh"
            }
        },
        {
            "firstName": "abhishek",
            "lastName": "gupta",
            "details": {
                "age": 25,
                "mobileNo": 12332567890,
                "City": "Gurgaon"
            }
        }
    ]
}
```

Uske baad aapne jiss directory mein `users.json` save kiya hai, usse directory mein yeh python ka code save kariye ek dusri file mein.

```python
import json
with open('user.json') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in data:
  counter = 0
  print "users full name is " + user['firstName'] + ' ' + user['lastName']
  while counter < len(user['details']):
    print "users mobile number is " + user['details'][counter]['mobileNo']
    print "users age  is " + user['details'][counter]['age']
    print "users city is " + user['details'][counter]['city']
```

`users.json` file mein users ka data padha hai. Yeh program `users.json` file ko read kar kar usmein se users ka data print karega. Iss file ko debug kar kar run karo.

Topics covered:

* Key error
* loop iterates over the wrong list.
