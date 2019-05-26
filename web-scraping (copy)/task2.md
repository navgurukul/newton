```ngMeta
name: Task 2
submissionType:url
```

# Task 2

Humne **Task 1** mein `scrape_top_list()` function likh ke saari movies ki list nikaal li hai. Iss task mein humein `group_by_year` naam ka ek naya function likhna hai jo ki movies ko by year group karega. Yeh function ek `movies` naam ka variable parameter ki tarah lega.

```python
def group_by_year(movies):
  # do something with the movies parameter
```

Yeh movies parameter basically `scrape_top_list` ki return value ki tarah hoga. Jo aapka `scrape_top_list` function return karega woh hi aap iss naye `group_by_year` function mein paas karoge.

`movies` wala parameter aisa dikhega:

```python
movies = [
  {
    "name": "Anand",
    "year": 1971,
    "position": 1,
    "rating": 8.7,
    "url": "https://www.imdb.com/title/tt0066763/"
  },
  {
    "name": "Drishyam",
    "position": 2,
    "year": 2013,
    "rating": 8.6,
    "url": "https://www.imdb.com/title/tt3417422/"
  },
  {
    "position": 3,
    "name": "Andhadhun",
    "year": 2018,
    "rating": 8.6,
    "url": "https://www.imdb.com/title/tt8108198/"
  }
]
```

Group by year method saari same saal wali movies ko ek saath group karega. Aapke iss function ko ek aisa data structure return karna hai.


```python
{
  1956: [
    {'name': 'Koi movie ka naam', 'year': 1956, 'position': 1, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
    {'name': 'Kuch aur naam', 'year': 1956, 'position': 4, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
    {'name': 'Ek aur naam', 'year': 1956, 'position': 8, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'}
  ],
  1959: [
    {'name': 'Koi movie ka naam 2', 'year': 1959, 'position':34, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
    {'name': 'Kuch aur naam 2', 'year': 1959, 'position': 42, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
  ],
  2000: [{}, {}, {}, {}, {}],
  2002: [{}, {}, {}, {}, {}],
  2001: [{}, {}]
}
```

Notice karo ki kaise iss data structure mein ek dictonary hai aur years uss dictionary ki keys hain. Har key mein ek list hai jismein firse movies ki individual dictionaries hain. Har movie ki dictionary ka structure waisa hi jaise `scrape_top_list` function mein ek movie ki dictionary ka structure tha.

# Hint

1. `movies` wale parameter pe ek nested loop chala ke aap yeh question solve kar sakte ho.

# Solution

@[youtube](https://youtu.be/V5dsZjjD1Jc)

**Created by Akhil Rawat (akhil18@navgurukul.org)**

