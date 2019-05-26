```ngMeta
name: Task 13
submissionType:url
```

# Task 13

**Task 12** mein aapne ek movie ki cast ki details nikaalne ka function toh likh liya.

Lekin abhi tak humra `scrape_movie_details` wala function caste ki details nhi nikaal raha. Sirf movie ki details nikaal raha hai. Uss function edit kar ke aise change karo ki wahi function caste ke URL ke saath apne andar se `scrape_movie_cast` wala function call kar raha hai.

Toh finally aapke `scrape_movie_details` waale function ko yeh dictionary return karni hogi:

```python
{
	"name": "Anand"
	"director": ["Hrishikesh Mukherjee"],
	"country": "India",
	"language": ["Hindi"],
	"poster_image_url": "https://m.media-amazon.com/images/M/MV5BNmZkMTMzNmEtMWU5NC00MjEzLWE5MzktYzRlMmQyMzk0YmM1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
	"bio": "The story of a terminally ill man who wishes to live life to the full before the inevitable occurs, as told by his best friend.",
	"runtime": 183,
	"genre": [
		"Drama"
	]
  "cast": [
    {
      "imdb_id": "nm0004435",
      "name": "Rajesh Khanna"
    },
    {
      "imdb_id": "nm0000821",
      "name": "Amitabh Bachan"
    },
    {},
    {},
    {},
    {}
  ]
}
```

Dekho ki kaise `scrape_movie_cast` wale function ki returned list issi dictionary mein ek key ki value hai.

Finally apna `get_movie_list_details` wala function bhi chala ke test karo ki woh ab movie ki details aur cast saari ek list mein return kar raha hai.

Saath saath yeh bhi test kar lo ki aapka `scrape_movie_cast` aur `scrape_movie_details` wale function aapki caching functionality kaam karni chaiye.
