```ngMeta
name: Task 3
submissionType:url
```

# Task 3

**Task 2** mein humne movies ko year ke hisaab se group karne ka code toh likh liya. Ab hum inn hi movies ko decade ke hisaab se group karenge. 10 saal se milakar ek decade banta hai. Jaise:

1. **1960 se 1969** tak ke beech ke saare saal 1960s ke decade mein aate hain.
2. **1970 se 1979** tak ke beech ke saare saal 1970s ke decade mein aate hain.
3. **1980 se 1989** tak ke beech ke saare saal 1980s ke decade mein aate hain.
4. **2000 se 2009** tak ke beech ke saare saal 2000s ke decade mein aate hain.

Ek function likho jiska naam hoga `group_by_decade`. Yeh function bhi `group_by_year` ki tarah ek `movies` naam ka parameter lega. Iss parameter mein same data hoga jo ki `scrape_top_list` wala function return karega. `movies` wale parameter ke data ka structure bhi kuch aisa hoga:

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
Yeh function pehle movies ko year se group kar sakta hai. Isse movies ko decade ke hisaab se group karna easy ho jayega. Iska code kuch aisa lagega:

```python
def group_by_decade(movies):
  # pehle hum group_by_year ka use kar ke movies ko year ke hisaab se group kar lenge pichla function use karke
  movies_by_year = group_by_year(movies)

  # iske aage hum apna code likhenge jismein hum movies_by_year wali dictionary ka use kar ke movies ko year ke hisaab se group karenge.

  # finally hum decade ke hisaab se grouped dictionary ko return kar denge
  return movies_by_decade
```

Iss function ki return value aisi dikhegi.

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

2000s wale section mein woh saari movies aayengi jo 2000 se 2009 ke beech mein release hui hain.
2010s wale section mein woh saari movies aayengi jo 2010 se 2019 ke beech mein release hui hain.
1970s wale section mein woh saari movies aayengi jo 1970 se 1979 ke beech mein release hui hain.


# Hint

1. Pehle yeh socho ki aap ke paas kaunse kaunse decades hain aur fir aap aapke paas ek year ineteger mein dia hua hai toh aap decade kaise nikaloge.

# Solution

@[youtube](video-id-here)

**TODO: Add the solution video here.**
