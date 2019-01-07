```ngMeta
name: Task 4
```

# Task 4

**TODO: Iski description ache se likhne ki zaroorat hai.**

Now we have to write a function to extract the indivual details of a movie. Yeh karke hum har movie ke page pe jake uski poori details nikaal sakte hain. The function should be called extract_movie_details and it should take a parameter called movie_url`. The `movie_url prameter will have the URL of IMDB which has all the details of a movie.
The function should return the following details about a movie. Example if I give https://www.imdb.com/title/tt0066763/ then it should return the following dictionary.

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
}


Upar waali dictionary mein har value ki data type ko gaur se dekho. Yeh data type same honi chaiye tumhari output ki bhi.

Genre mein ek strings ki list hai. Kyunki Anand ki sirf ek hi Genre hai toh usme sirf ek string hai. Kuch movies ki multiple genre hoti hai aur woh comma se seperated diye hote hain. Toh uss case mein genre waali list mein alag alag strings hone chaiye.

Kuch movies hain jinme ek se zyada director honge jisme comma seperated list di hogi. Jaise `Taare Zameen Par`. Isliye Director bhi ek list hogi.

Directors aur Genre ki tarah ek movie mein ek se zyada languages ka prayog hua ho sakta hai. Isliye woh bhi list honi chaiye. Jaise Nayakan https://www.imdb.com/title/tt0093603/

Runtime ko Technical Specs wale section mein se scrape karo. Wahan runtime sirf minutes mein dia hua hai.

# Hint



# Solution

@[youtube](video-id-here)

**TODO: Add the solution video here.**
