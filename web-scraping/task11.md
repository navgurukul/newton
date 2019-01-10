```ngMeta
name: Task 11
submissionType:url
```

# Task 11

Iss task mein humein ek aur chota sa anlysis run karna hai. Ab hum movies ko by genre analyse karenge.

![Anand IMDB](images/anand_imdb.png)

Yahan dekho ki Anand ka Genre mein **Drama** likha hua hai. Bahot saari movies ke ek se zyada genres bhi hote hain.

Ek `analyse_movies_genre` naam ka function likho. Yeh function ek `movies_list` naam ka parameter lega jisme mein woh list hogi jo `get_movie_list_details` wala function return karta hai. Matlab `movies_list` ka structure aisa hoga:

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

Aapke function ko ek dictionary return karni hai jismein har genre ka naam keys mein hoga aur genre ki number of movies uski value mein hoga.

**Note: Yeh keys aur values ko kaise refer kara hai ispe khaas dhyaan di jiye. Issi tareeke se dictionaries ki baat karte hain :)**

`analyse_movies_genre` wali return value ki dictionary ka neeche dia hua structure dia hua hai.

```python
{
  "Comedy": 133,
  "Drama": 23
}
```

Yeh function aapko saari 250 movies pe run karna hai.

## Hint

Ab kya hint ki zaroorat hai? Bahot baar kar lia aapne yeh :)
