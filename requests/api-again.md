## It's me - API - again ;)

Ab aap yeh link - [http://saral.navgurukul.org/api/courses/74/exercises](http://saral.navgurukul.org/api/courses/74/exercises)
open karein. Iss link mei, iss particular course ki saari
exercises ki list hai. Aur `slug`, `parentExerciseId`, `githubLink` jaisi
kuch aur bhi information hai. Iss information ko bhi hum aage use karenge.

Jo `course_id` user ne select ki hai, uske corresponding aapko yeh API
call karni hai. Phir jab aap yeh API call kar lenge, toh aapko kuch
uss tarah ka data milega jaisa uppar wale link se mila tha. Ab aapko
yeh exercise print karni hai terminal par. Kuch baatein jo important hai:

1 - Agar `childExercises` hai kisi bhi exercise ki toh, unko bhi print karni
hai. Kyuki woh childExercise hai, toh woh thoda sa side mei print karo, spaces
dekara. Unki numbering ke liye, socho kaise kar sakte ho.

2 - Jaise aapne pehle `id` nikali thi, user_choice ke vajah se, aise hi iss baar bhi
aapko, exercise ka `slug` nikal kar rakhna hai. Toh aapki numbering aisa karna, ki
jo user input karein, usse aap guess kar payo, ki kaunsi `exercise` user ne select ki
hai, aur uska corresponding `slug` kya hai.

3 - Jab bhi `parentExerciseId` null hoga, toh python usse `None` ki tarah read karega.
