```ngMeta
name: Task 7
submissionType:url
```

# Task 7

Abhi tak humne movies ko Languages ke basis pe analyse kara hai aur yeh dekha hai ki kaunsi language ki kitni movies hain top 250 ki list mein. Ab hum same cheez directors ke saath karenge. Yeh wala task bhi abhi ke liye humne pehli 10 movies ke liye karna hai.

`analyse_movies_directors` naam ka ek function likho. Yeh function movies naam ki ek list lega. Yeh woh list hogi jo `get_movie_list_details` wala function return karta hai. Kuch aisi dikhegi:

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

Iss function ka output yeh hoga:

```python
{
"Rishabh Verma": 2,
"Hrishikesh Mukherjee": 1,
"Sanjay Leela Bansali": 2
}
```

Jaise agar Sanjay Leela Bansali ka naam do movies mein aa raha hai, toh uski ginti 2 baar hogi. Aur agar kisi movie ka ek se zyada directors hain, toh unn dono ki ginti hogi.


## Hint

Iska code kuch aisa dikhega:

```python
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
director_analysis = analyse_movies_directors(movies_detail_list) # dekho kaise get_movie_list_details ki return value humne analyse_movies_directors function mein de di
```
