```ngMeta
name: Task 5
submissionType:url
```

# Task 5

Pichli task mein humne ek function likh liya hai jo humein movie ke URL se uski saari details laake de deta hai. Iss function ka naam `scrape_movie_details`. Ab humein ek function likhna hai jisko hum movie ke URLs denge toh humein woh movies ki poori details ke saath ek list return karega. Function ka naam `get_movie_list_details` hona chaiye. Yeh function ko ek `movies_list` naam ka parameter lena hai jo ki list hogi. Iss list ka naam movies hoga. Movies ke naam ke saath saath kuch aur details bhi hongi.  

Basically yeh function woh list parameter ki tara lega jo ki `scrape_top_list` return karta hai. Abhi ke liye aapko iss function ko sirf pehli 10 movies deni hain. Agar aap zyada movies ek baar mein scrape karoge toh IMDB aapko block kar dega. Iske baare mein detail mein hum aage waali kuch tasks mein baat karenge.

`movies_list` parameter waali list ka kuch aisa structure hoga. Yeh woh same list hai jo aapka `scrape_top_list` function return karta hai.
```js
[
	{	
		'name': "Anand", 
		'year_of_release': 1971, 
		'position': 1, 
		'rating': 8.7, 
		'url': "https://www.imdb.com/title/tt0066763/", 
	} , 
	{...}, 
	{...}, 
	{...}, 
	{...}
]
```

Movies wali list ko leke tumhara function neeche di hui list return karega.

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

Aapka code kuch aisa dikhega:

```python
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
```

## Hint

1. Aapko `get_movie_list_details` details mein baar baar `scrape_movie_details` wala function call karna hai.
