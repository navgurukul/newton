```ngMeta
name: Task 1
submissionType:url
```

# Task 1

Ab hum apna project karna shuru karenge. Pehli task mein humein **Top Rated Indian Movies** wale IMDB page se saari top rated movies ki list nikaalni hai.

Page ka link yeh hai: https://www.imdb.com/india/top-rated-indian-movies/

Humein ek function likhna hai called `scrape_top_list()` jo movies ki list ko return karega. Yeh function movies ki list ko iss format mein return karega.

```json
[
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
  },
  {...},
  {...},
  {...},
  {...}
]
```

Notice kariye ki yeh ek dictionaries ki list hai. List mein multiple dictionaries hain aur har dictionary mein ek movie ki details hain. Dictionary ki keys ka exactly same naam hona chaiye aur unki values mein upar diye gaye format ke hisaab se data types hone chaiye.

1. `name` movie ka naam hai. Yeh ek string mein hona chaiye.
2. `year` should be an integer. Yeh movie ki release date hai.
2. `positon` movie ka position in the list hai. Yeh ek integer hona chaiye.
3. `url` movie ke indivual page ka link hona chaiye.
4. `rating` movie ke rating honi chaiye. Yeh ek float hoga.

# Hint

1. Saari movies ki list ek tabular format mein hai. `<tbody class="lister-list">` wali table body mein saari movies hain. Iss `<tbody>` mein bahot saare `<tr>` elements hain. Har `<tr>` element mein ek ek movie ki details hain.
2. `<tr>` element ke andar kuch kuch `<td>` elements hain. Notice karo ki kaise har `<td>` element ki ek alag alag class hai.
3. `<td class="titleColumn">` wale `<td>` element mein movie ka naam, year aur position. Iss element pe `get_text()` laga ke hum movie ka naam aur year nikaal sakte hain. Fir humein thodi si string manupilation kar ke position, naam aur year ko alag karna hoga.
4. `<td class="ratingColumn imdbRating">` wale element mein movie ki rating hai.
5. `<td class="titleColumn">` ke andar hi ek `<a>` tag hai. Iss `<a>` tag ke `href` attribute mein movie ka poora link hai. Wahan se movie ka link nikaal sakte hain.

Pehle poori task ko khud karne ki koshish karo. Agar bahot zyada issue aata hai toh aap solution video dekh sakte ho.

# Solution

@[youtube](https://www.youtube.com/watch?v=PNv9cD-ene8)

**Created by Vishal Gaddam (vishal18@navgurukul.org)**

