task3_key1
task3_key2


1. task3_key3
2. task3_key4
3. task3_key5
4. task3_key6
task3_key7


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
task3_key8


```python
def group_by_decade(movies):
  # pehle hum group_by_year ka use kar ke movies ko year ke hisaab se group kar lenge pichla function use karke
  movies_by_year = group_by_year(movies)

  # iske aage hum apna code likhenge jismein hum movies_by_year wali dictionary ka use kar ke movies ko year ke hisaab se group karenge.

  # finally hum decade ke hisaab se grouped dictionary ko return kar denge
  return movies_by_decade
```

task3_key9


```python
{
  1950: [
    {'name': 'Koi movie ka naam', 'year_of_release': 1956, 'position': 1, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
    {'name': 'Kuch aur naam', 'year_of_release': 1956, 'position': 4, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
    {'name': 'Ek aur naam', 'year_of_release': 1956, 'position': 8, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
    {'name': 'Koi movie ka naam 2', 'year_of_release': 1959, 'position':34, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
    {'name': 'Kuch aur naam 2', 'year_of_release': 1959, 'position': 42, 'rating': 8.7, 'url': 'https://imdb.com/title/koi-title-ka-link'},
  ],
  1960: [
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {}
  ],
  1980: [
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {}
  ]
}
```

task3_key10



task3_key11
1. task3_key12
task3_key13
@[youtube](https://youtu.be/oC0n_oGJnQo)

task3_key14
