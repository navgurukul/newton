```ngMeta
name: Insta Analyze
```

### Insta Analyze

Humein ek instagram ke liye `bot` banana hai, jo mere instagram followers ki posts ka sentiment analysis karega.

Iske liye aapko:

Instagram se data scrap karne ke liye aapko [InstaPy](https://github.com/timgrossmann/InstaPy) library use karni hai.
Sentiment analysis ke liye aapko - [NLTK](http://www.nltk.org/howto/sentiment.html) library use karni hai.

### Process
1. Aapko apne saare instagram followers ki saari descriptions download kar kar {username}.txt naame ki files mei dump karna hai. Har ek new line mei ek nayi post ka content store hoga.
   
Toh agar aapke 10 followers hai, toh 10 files hongi, jismei unki har ek instagram post ke liye ek nayi line hogi.
Jaisa agar mai aapko follow karta hu, toh abhishekgupta921.txt mei meri saari instagram posts ek ek line mei hogi.

2. Ab aapko sentiment analysis padh kar samajhna hai ki kya hota hai. Aap NLTK use kar kar ek simple sa sentiment analyser banaye jo [iss](https://www.kaggle.com/c/si650winter11) data par kaam karta hai. Dhyaan rakhein, ki simply Naive Bayes Classifier use karna, isse aapko kam efforts lagenge. Internet par bahut saare tutorials hai jo yeh karne mei aapki help karenge.

3. Ab iss code ko aise modify karo ki aap ka analyzer jo kaggle se jo data hai, uss par train ho, par instagram posts ko analyse karein. Iske baad aap aisa kuch print karoge:

```markdown
abhishekgupta921 23/41
rishabhverma21 10/14
anuradhadaswani 1/9
amar 1/18
```

Yaani
`{username} {number_of_positive_posts}/{number_of_total_posts}`

Kuch bhi clarifications ke liye, aap cliq par #diwaliProjects channel par pooch sakte hai. Par aapko aapke code ki har ek line clear honi chahiye, ki aapne kyu kya kiya hai. Uss ke basis par hi aapka interview hoga.

Good luck and happy coding.
