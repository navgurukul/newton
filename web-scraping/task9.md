```ngMeta
name: Task 9
submission_type:url
```

# Task 9

Generally jab hum koi bhi data scrape karte hain uss website se toh uss website ke servers pe bahot load padta hai. Abhi toh aap sirf bahot thodi si requests maar rahe ho IMDB ke servers pe. Lekin aap yeh socho ki agar aapko IMDB ki saari movies scrape karni hai. IMDB pe duniya bhar ki movies ka data hai. Matlab kuch crore movie hongi. Agar aap 10 crore movies ka data scrape kar rahe ho toh yeh karna padega:

1. Har movie ka main page khol ke uska data scrape karna.
2. Uss movie ka cast wala page khol ke saare actors aur actresses ki list scrape karna.

Matlab agar 10 crore movies scrape ho rahi hai, toh around 20 crore requests kar rahe hoge aap IMDB ke servers pe. Itni saari requests se IMDB ki servers pe load padega aur iss chakar mein IMDB ke servers humein block kar denge. 

Saare computer attacks ke baare mein janne ke liye ye video dekhein:

@[youtube](AuYNXgO_f3Y)

Bahot important hai yeh samjhna ki websites scrapers ko kyun block karti hai aur hum isko kaise prevent kar sakte hai. You should spend some time researching and understanding this. Aur better hoga ki aap yeh apne kuch friends ke saath padh ke samjho. Akele karke utni clarity nahi milegi. Google karke samjho :) Neeche main kuch links de raha hun jahan se aap apni research shuru kar sakte ho.

1. https://www.quora.com/I-was-scraping-a-website-and-they-blocked-me-How-can-I-get-around-this
2. https://www.quora.com/How-do-you-prevent-yourself-from-being-blocked-when-scraping-a-websites-data-like-Oodle-does-to-craigslist
3. https://www.octoparse.com/blog/scrape-websites-without-being-blocked

Yeh links padhte hue aapko bahot saari new terms milegi. Aapko unn saari terms ke baare mein ache se research kar ke samjhna padega.

Generally jab bhi websites aapke scrapers ko block karte hain toh woh aapke computers ya laptop ke public IP ko block karte hain. Best yeh hai ki aap apne phone ke hotspot se internet ka use kar ke scraping karo. Phones apna assigned IP har baar internet on/off karne pe change kar dete hain. Toh agar aap kabhi b lock hue bhi toh jaldi se IP change kar sakte hain. Jab aapko ek website block karegi toh aap request maaroge toh kuch error aane lagegi.

Abhi blocking ko prevent karne ke liye humein IMDB ko dikhane ki zaroorat hai ki hum ek human user hain aur scraper nahi hai. Generally jab bhi human users website ka use karte hain toh har request mein (page khulne mein) alag alag time hota hai. Lekin yahan humara `get_movie_list_details` ek loop mein ek baad baad ek request maar raha hai. Iss task mein aapko apni har request ke beeche mein ek 1 se 3 ke beech mein kuch random seconds ka sleep timer lagana hai.

Iske liye aapko `random.randint` ka use kar ke ek random integer choose karo 1 aur 3 ke beech mein. Fir `time.sleep` ka use kar ke apne program ko utni der ke liye sleep karvao.

Yeh task complete kar ne ke baad aapko `get_movie_list_details` wala function saari 250 movies ki list ke saath call karna hai. Yeh bhi ensure kar lena ki aapka `scrape_movie_details` wala function aapke data ko cache kar raha hai. Aur ek baar apna code chala ke saari 250 movies ki poori details cache mein store kar lo ki aage wala saara code likhna asaan ho.

## Hint

Python ke sheel mein ek `help` function hota hai. Aap uss function mein koi bhi object ya dusra function doge toh woh uski documentation dikha dega. Documentation woh hoti hai jo programmers apna code likhte hue dusre programmers ke liye likhte hai. Kisi bhi function ki documetation dekh ke woh function use karna asan ho jayega.

`random.randint` ka documentation dekhne ke liye aapko apne shell mein yeh code chalana padega:

```python
import random
help(random.randint)
```

Isko try karo. Aise hi aap neeche waale code chala ke `time.sleep` ki documentation dekh sakte ho.

```python
import time
help(time.sleep)
```

Agar aapko ek function ki documentation dekhni hai toh uss function ko call kare bina `help` mein pass karo. Agar call kar ke pass kar do toh woh uss function ki return value ki documentation dikhayega. Basically `help` ko jo bhi object milta hai woh uski documentation dikhata hai.

### Solution Video :-

@[youtube](https://youtu.be/5FIPLIXWmtQ)

**Created by Vishal Gaddam** (vishal18@navgurukul.org)
