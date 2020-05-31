```ngMeta
name: Task 6
submission_type:url
```

# Task 6

Aapko `get_movie_details` function ne movies ki saari details ek list mein lake de di. Abhi ke liye hum pehli 10 movies ki baat kar rahe hain. Toh ab hum pehli 10 movies ki list pe kuch analysis run karenge. Iss analysis se hum data ke baare mein kuch cheezein jaanenge.

Pehli cheez mujhe yeh dekhni hai hai ki har langauge ki kitni movies hain. Jaise kitni movies Hindi ki hain top 250 mein aur kitni movie Malyalam ki hain etc. Kyunki langauge mein multiple langauge di hui hain, isliye agar ek movie mein English aur Hindi di hui hain, toh uss movie ki ginti dono languages mein hogi. Poori task padh ke aapko yeh dhang se samajh aa jayegi.

Ek `analyse_movies_language` naam ka function likho jo ek `movies_list` naam ki list ko parameter leta hai. Yeh movies naam ki list kuch aisi dikhegi:

```python
[
	{
		"name": "Anand"
		"director": ["Hrishikesh Mukherjee"],
		"country": "India",
		"language": ["Hindi"],
		"poster_image_url": "https://m.media-amazon.com/images/M/MV5BNmZkMTMzNmEtMWU5NC00MjEzLWE5MzktYzRlMmQyMzk0YmM1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
		"bio": "The story of a terminally ill man who wishes to live life to the3 full before the inevitable occurs, as told by his best friend.",
		"runtime": {
			"hours": 2,
			"minutes": 2
		},
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

`movies_list` basically `get_movie_list_details` wale function ki return value hai. Aapne  `analyse_movies_language` function ko `get_movie_list_details` return value `movies_list` parameter mein deni hain.

Iss function ko ek dictionary return karni hai jiska structure aisa hona chaiye.

```python
{
	"Hindi": 10,
	"English": 4,
	"Malyalam": 4
}
```

**Note: Agar ek movie mein English aur Malayalam dono dia hai, toh uski ginti dono heads mein hogi.**

Scraping mein ek aur important cheez hoti hai verify karna ki humara code sahi output de raha hai. Yeh yaad rakhne ki zaroorat hai ki HTML ka code kabhi bhi scrapers ke liye nahi likha but browsers ke samajhne ke liye likha hota hai. Isliye kabhi kabhi shayad humara code sahi na chale. Yeh karne ke liye aapko thoda data manually vefiy karne ki zaroorat hoti hai. Yeh karne ke liye aap pehli 10 movies ke URLs manually visit karke apne scraper ki output ko verify kar sakte ho. Agar sahi chal raha hai, toh hum shayad apna code safely saari 250 ki list pe chala sakte hain.


## Hint

Aapka code kuch aisa lagega:

```python
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
language_analysis = analyse_movies_language(movies_detail_list) # dekho kaise get_movie_list_details ki return value humne analyse_movies_language function mein de di
```
