```ngMeta
name: API Request
```

Apne browser ke address box mein "http://quotes.rest/qod.json?category=inspire" daale.

Aapko aisa kuch output dikhega

```json
{
    "success": {
        "total": 1
    },
    "contents": {
        "quotes": [
            {
                "quote": "Stop complaining. Start creating.",
                "author": "Dale Patridge",
                "length": null,
                "tags": [
                    "complain",
                    "create",
                    "inspire"
                ],
                "category": "inspire",
                "title": "Inspiring Quote of the day",
                "date": "2018-05-19",
                "id": null
            }
        ],
        "copyright": "2017-19 theysaidso.com"
    }
}
```

Ye output **JSON format** mein hai. JSON format data ko arrange karne ka ek tareeka hai. JSON format ke baare mein janne ke liye [yahan](https://www.w3schools.com/js/js_json.asp) padhe.
Data store karne ke liye JSON ek standard format hai.


Jab apne browser ke address mein "http://quotes.rest/qod.json?category=inspire" daala toh aapne quotes.rest/qod.json ko ek quote ki request bheji. Request mein aapne bola ki aapko *inspire* category ke quotes chahiye.

Quotes.rest ek service provide karti hai jo aapko quote of the day deti hai. Iss service ko hum **API service** kehte hain.
Aap Quotes.rest ke server ko request bhej kar quotes JSON format mein receive kar sakte hain.


Jaise aapne upar mein category supply ki, usi tarah kisi kisi API mein aapko apne aap ko authenticate(authorize, taaki service providers ko pata chale ki kaun request bhej raha hai) karna par sakta hai. Authenticate karne ke kayi tareeke hai - jasie API key(ek tarah ka passwork) supply karna ya OAuth(ek tarah ka account validation) use karna. Hum inko use karna aage seekhenge.

**Assignment**
- OpenWeatherMap.org/api pe "Current Weather Data" ke liye apne aap ko subscribe kijiye.
- API docs padh kar, browser ke through ek API request bhejiye jisse aap kisi city ka weather information JSON format mein dekh sake.
