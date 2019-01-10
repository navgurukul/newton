```ngMeta
name: Task 10
submissionType:url
```

# Task 10

Ab humne saari 250 movies ki list toh scrape kar li hai. Iss task mein humne kuch aur analysis.

Abhi tak humne directors aur languages ka analysis alag alag se kia tha. Toh humare paas yeh data tha ki har director ki total kitni movies hain aur languages ke hisaab se bhi movies ki frequency thi. Ab humein in dono ko combine karna hai?

Ab humein yeh samajhna hai ki **Kaunse directors kaun kaun si languages mein movies banante hain? Aise kaunse diectors hai jo ek se zyada langauges mein movies direct karte hain?**

Iske liye aap ek function likhoge jiska naam hoga `analyse_language_and_directors`. Yeh function ek parameter lega called `movies_list`. Iss parameter mein woh list hogi jo `get_movie_list_details` wala function return karta hai. Matlab woh list kuch aisi dikhegi:

```python
[
	{
		"name": "Anand"
		"director": ["Hrishikesh Mukherjee"],
		"country": "India",
		"language": ["Hindi"],
		"poster_image_url": "https://m.media-amazon.com/images/M/MV5BNmZkMTMzNmEtMWU5NC00MjEzLWE5MzktYzRlMmQyMzk0YmM1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
		"bio": "The story of a terminally ill man who wishes to live life to the3 full before the inevitable occurs, as told by his best friend.",
		"runtime": 183,
		"genre": [
			"Drama"
		]
	},
	{},
	{},
	{},
	{},
	{},
	{}
]
```

**Yeh dhyan rakhna ki aapne yeh analysis saari 250 movies ki list pe run karna hai.**

Aapke function ka return value ek dictionary hoga. Yeh dictionary kuch aisi dikhegi:

```python
{
  "Hrishikesh Mukherjee": {
    "Hindi": 2,
    "Bengali": 1
  },
  "Director Name": {
    "Hindi": 2,
    "Malayalam": 2
  }
}
```

Kyunki har movies mein director aur languages dono lists hain aur ek string nahi hai. Agar ek movie ke 2 directors aur saath saath 2 languages bhi hai toh uss movie ki counting dono languages mein bhi hogi, aur dono directors mein bhi hogi.

## Hint

1. Nested loops ka use karo :)
