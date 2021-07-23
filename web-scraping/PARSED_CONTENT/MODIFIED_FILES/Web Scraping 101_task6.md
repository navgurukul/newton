```ngMeta
task6_key1
```

task6_key2
task6_key3


task6_key4


task6_key5


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
task6_key6


task6_key7


```python
{
    "Hindi": 10,
    "English": 4,
    "Malyalam": 4
}
```
task6_key8


task6_key9



task6_key10
task6_key11


```python
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
language_analysis = analyse_movies_language(movies_detail_list) # dekho kaise get_movie_list_details ki return value humne analyse_movies_language function mein de di
```
