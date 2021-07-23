```ngMeta
task7_key1
```

task7_key2
task7_key3


task7_key4


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
task7_key5


```python
{
"Ankita gole": 2,
"Hrishikesh Mukherjee": 1,
"Sanjay Leela Bansali": 2
}
```
task7_key6



task7_key7
task7_key8


```python
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
director_analysis = analyse_movies_directors(movies_detail_list) # dekho kaise get_movie_list_details ki return value humne analyse_movies_directors function mein de di
```
