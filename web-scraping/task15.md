```ngMeta
name: Task 15

```

# Task 15

Ab humne cast ke basis pe kaafi saare analysis bhi kar liye. Iss task mein hum ek bahot simple sa analysis karenge. Iss analysis mein hum log woh actors/actresses ki list nikalenge jinka naam ek se zyada movies mein aata hai. Yeh analysis hum har movie ki saari cast pe karenge aur na ki top 5 pe.

Ek function likho jiska naam `analyse_actors` ho. Yeh function ek `movies_list` naam ki list ko parameter ki tarah lega. Iss list mein woh list hogi jo `get_movie_list_details` wala function return karta hai. Yeh `movies_list` aisi dikhegi:

```python
[
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
  },
  {},
  {},
  {},
  {}
]
```

Humare function ko yeh batana hai ki kaun kaun se actors hain jo ek se zyada movies mein aate hain. Toh yeh function ek dictionary return karega jiska yeh structure hoga:

```python
{
  "nm0004435": {
    "name": "Rajesh Khanna",
    "num_movies": 2
  },
  "nm0000821": {
  "name": "Amitabh Bachan",
  "num_movies": 4
  }
}
```

Dhayn di jiye kaise iss dictionary mein bhi humne actors ko unki IDs se reference kara hai aur na ki unke names se. Aap apna code likhte hue bhi IDs ke basis pe code likhna.
