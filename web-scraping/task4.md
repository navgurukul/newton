```ngMeta
name: Task 4
submissionType:url
```

# Task 4

Ab humne movies ki list se ek ache se structure mein unki details nikalne ka scraper toh likh liya hai `scrape_top_list()` waale function mein. Aap agar notice karoge toh har **Top Rated Indian Movies** waali list mein har movie ka ek alag link diya hua hai. Iss linked page pe uss movie ki saari details depth mein likhi hui hain. Iss task mein humne ek aur function likhna hai jo uss movie ke saari indivual details nikalega.

![Anand IMDB](images/anand_imdb.png)

Iss function ka naam `scrape_movie_details` hoga. Yeh function ek parameter lega called `movie_url` jismein uss movie ka URL hai jiski details nikalni hai. Iss function ko ek dictionary return karni hogi. Iss dictionary ka structure neeche diya hua hai. Agar aap yeh code Anand movie (https://www.imdb.com/title/tt0066763/) ke liye chala rahe ho toh woh function neeche di hui dictionary return karega.

```
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
```

Kuch important cheezein aapko apne dimaag mein rakhni hai when writing the code for this function.

1. Upar waali dictionary mein har value ki data type ko gaur se dekho. Yahan dia hua data type aur aapki final dictionary ka output same hona chaiye.
2. Genre mein ek strings ki list hai. Kyunki Anand ki sirf ek hi Genre hai toh usme sirf ek string hai. Kuch movies ki multiple genre hoti hai aur woh comma se seperated diye hote hain. Toh uss case mein genre waali list mein alag alag strings hone chaiye. Aisi ek movie **Andhadhun** (https://www.imdb.com/title/tt8108198/) hai.
3. Anand ka toh ek hi director hai isliye uski `"director"` waali list mein sirf `["Hrishikesh Mukherjee"]` hai. Lekin kuch movies hoti hai jinme ek se zyada director hote hain. Unn movies mein saare directors ka naam comma seperated hona chaiye. **Taare Zameen Par** (https://www.imdb.com/title/tt0986264/) ek aisi movie hai jiske IMDB ke hisaab se 2 directors hain.
4. Directors aur Genre ki tarah ek movie mein multiple languages ka use bhi kia ho sakta hai. Isiliye `languages` waali dictionary key bhi list of strings ki honi chaiye. Nayakan ek aisi movie hai jismein multiple languages hain. (https://www.imdb.com/title/tt0093603/)
5. Notice karo `"runtime"` key mein bas ek integer hain. Waise runtime jo hai woh **2h 13m** jaise format mein dia hota hai. Aapko iss format ko sirf minutes mein convert karna hoga. Jaise **2h 13m** 133 minutes ban jayega kyunki **(2*60) + 13 = 133**. Isliye 133 minutes.

Submit karne se pehle apne code ko at least 10 movies ke alag alag pages ke test karke dekho ki aapka code sahi results return kar raha hai.

# Solution

@[youtube](https://youtu.be/hpUASoRqA_Q)

**Created by Vishal Gaddam**(vishal18@navgurukul.org)
