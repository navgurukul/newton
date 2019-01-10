```ngMeta
name: Task 8
submissionType:url
```

# Task 8

@[youtube](https://www.youtube.com/watch?v=n__c7xY1ZcI)

Upar wale video mein humne samjha caching kya hota hai. Jab bhi humara code ek kaam karne mein bahot time leta hai aur hum uss kaam ko baar baar karna chahte hain, toh hum uss code ka output kahin save kar ke rakh lete hain jahan se hum usko jaldi nikaal sake aur itna time na lage.

Jaise aapne notice kara hoga agar humara `scrape_movie_details` function ko jab ek movie ka url dete hain toh woh 1 ya 2 second leta hai uss page se movie ki details lane mein. Yeh isliye hota hai kyunki ek page ko kholna aur uska data nikalne mein time lagta hai. Isko fast karne ka ek tareeka hai.

Iss code ko refactor karo (*Bonus: Understand the meaning of `refactoring code` by using google*) ki ismein hum caching implement kar sakein.

Iska matlab jab bhi hum iss function ko call karenge woh movie ki details nikaalne ke saath saath movie ki details ko ek file mein save kar lega. Aur agar usko movie ki corresponding file offline stored milegi toh woh page ko khol ke uska data parse nahi karega, directly cache se file ko padh ke result de dega. Iss file ka data JSON mein hoga. Neeche wale paragraphs mein isko ache se explain kia hua hai.

Abhi jab bhi hum `scrape_movie_details` function ko call karte hain, toh woh requests ka use kar ke page kholta hai aur fir uska data BeautifulSoup ka use kar ke parse karta hai. Fir uss data ko store karta hai. Humein iss function mein yeh changes karni hai:

1. Data parse karke dictionary mein return karne se pehle uss dictionary ko JSON mein convert kar ke ek file mein store karna hai. Agar aap URL ko dhyaan se dekhoge toh har movie ke URL uss movie ki IMDB ke hisaab se ek ID hoti hai. Jaise yeh Anand (https://www.imdb.com/title/tt0066763/) ka URL hai. Ismein `tt0066763` ID hai. Humein humesha URL se yeh ID nikaalni hai aur iss ke naam se ek file banani hai jismein `scrape_movie_details` ki final dictionary ko JSON mein convert kar ke save karenge. Anand ki cache file ka naam `tt0066763.json` hoga.

**#TODO: Add how to convert dictionary to JSON or paste a relevant link for it.**

2. Aapko function ka flow aise change karna hai ki woh pehle dekhe ki kya humare cache mein (matlab movie ki ID ke hisaab se ek JSON file exist karti hai kya?) yeh movie exist karti hai. Agar karti hai toh cache se details lake de deni hain. Nahi toh uss movie ki details IMDB se nikaalni hain.


##TODO: Add a solution video.
