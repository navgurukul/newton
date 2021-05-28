```ngMeta
debugging-question3_key1
```
debugging-question3_key2`users.json`debugging-question3_key3

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
debugging-question3_key4`users.json`debugging-question3_key5

```python
import json
with open('user.json') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in data:
  counter = 0
  print ("users full name is " + user['firstName'] + ' ' + user['lastName'])
  while counter < len(user['details']):
    print ("users mobile number is " + user['details'][counter]['mobileNo'])
    print ("users age  is " + user['details'][counter]['age'])
    print ("users city is " + user['details'][counter]['city'])
```
`users.json`debugging-question3_key6`users.json`debugging-question3_key7

debugging-question3_key8

* debugging-question3_key9
* debugging-question3_key10
